def read(fname : String) : String
  content = File.open("./#{fname}") do |file|
    file.gets_to_end
  end
end

def parse(content : String) : Array(String)
  lines = content.split("\n").select { |x| x.size > 1 }
  lines
end

def part1(input : String) : Int32
  parsed = parse(input)
  mul_pat = /mul\((\d+,\d+)\)/
  filtered = parsed.map { |line| line.scan(mul_pat)
    .map { |match| match[1].split(",")
      .map { |x| x.to_i32 } } }

  calc = filtered.map { |line| line.reduce(0) { |acc, tup| acc + (tup[0] * tup[1]) } }
  all_calc = calc.reduce(0) { |acc, x| acc + x }
  all_calc
end

def parse_str(line : String) : Int32
  mul_pat = /(mul\((\d+,\d+)\)|do\(\)|don't\(\))/
  matches = line.scan(mul_pat)
  dont = false
  consider = matches
    .select do |match|
      captures = match.captures
      if (captures[0] == "don't()")
        dont = true
      elsif (captures[0] == "do()")
        dont = false
      end

      !dont && captures[1] != nil
    end
    .map do |match|
      captures = match.captures

      captures[1].as(String).split(",").map { |x| x.to_i32 }
    end

  ans = consider.reduce(0) { |acc, tup| acc + (tup[0] * tup[1]) }
  ans
end

def part2(input : String) : Int32
  parsed = parse(input)
  calc = parsed.map { |x| parse_str(x) }
  rv = calc.reduce(0) { |acc, x| acc + x }
  rv
end

def main
  p1 = part1(read("in.txt"))
  p2 = part2(read("in.txt"))

  p! p1, p2
end

# ---------------
# ENTRYPOINT
# ---------------
main()

# ---------------
# TESTS
# ---------------

require "spec"

describe "day03" do
  it "part1" do
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    parsed = parse(input)
    got = part1(input)
    got.should eq 161
  end
  it "part2" do
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    parsed = parse(input)
    got = part2(input)
    got.should eq 48
  end
end
