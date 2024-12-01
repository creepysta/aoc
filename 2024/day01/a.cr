def read(fname : String) : String
  content = File.open("./#{fname}") do |file|
    file.gets_to_end
  end
end

def parse(content : String) : Array(Array(Int32))
  lines = content.split("\n")
  nums = lines
    .select { |x| x.split(/ +/).size == 2 }
    .map { |el| el.split(/ +/).map { |x| x.to_i32 } }
  transpose = [0, 1].map { |colIdx| nums.map { |row| row[colIdx].as(Int32) } }

  transpose
end

def part1(input : String) : Int32
  parsed = parse(input)
  # p parsed
  a, b = parsed.map { |iter| iter.sort }
  # p! transpose, a, b

  ans = a.zip(b).reduce(0) { |acc, e| acc + (e[0] - e[1]).abs }

  ans
end

def part2(input : String) : Int32
  parsed = parse(input)
  # p! parsed
  ans = parsed[0].reduce (0) { |acc, i| acc + i*parsed[1].count(i) }
  ans
end

def main
  p1 = part1(read("in.txt"))
  p2 = part2(read("in.txt"))

  p! p1, p2
end

main()

require "spec"

describe "day01" do
  input = "3   4
4   3
2   5
1   3
3   9
3   3"
  it "part1" do
    parsed = parse(input)
    got = part1(input)
    got.should eq 11
  end
  it "part2" do
    parsed = parse(input)
    got = part2(input)
    got.should eq 31
  end
end
