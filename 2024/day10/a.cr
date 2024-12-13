def read(fname : String) : String
  content = File.open("./#{fname}") do |file|
    file.gets_to_end
  end
end

def parse(content : String) : Array(String)
  lines = content.split("\n").select { |x| x.size > 1}
  lines
end

def part1(input : String) : Int32
  parsed = parse(input)
  0
end

def part2(input : String) : Int32
  parsed = parse(input)
  0
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

describe "day10" do
  input = "__SAMPLE__"
  it "part1" do
    parsed = parse(input)
    got = part1(input)
    got.should eq -9999999
  end
  it "part2" do
    parsed = parse(input)
    got = part2(input)
    got.should eq -9999999
  end
end