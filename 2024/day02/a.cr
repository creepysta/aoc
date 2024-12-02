def read(fname : String) : String
  content = File.open("./#{fname}") do |file|
    file.gets_to_end
  end
end

def parse(content : String) : Array(Array(Int32))
  lines = content.split("\n")
  parsed = lines
    .select { |x| x.size > 0 }
    .map { |x| x.split(" ")
      .map { |x| x.to_i32 } }

  parsed
end

def _check_monotone(list : Array(Int32)) : Bool
  rv = list[...list.size - 1].zip(list[1..]).select { |x| x[0] < x[1] }
  rv.size == list.size - 1
end

def check_monotonic(list : Array(Int32)) : Bool
  inc = _check_monotone(list)
  dec = _check_monotone(list.reverse)
  inc || dec
end

def is_valid(a, b : Int32) : Bool
  diff = (a - b).abs
  1 <= diff && diff <= 3
end

def check_diff(list : Array(Int32)) : Bool
  if (list.size <= 2)
    puts "check_diff: #{list}"
  end
  rv = list[...list.size - 1].zip(list[1..])
    .reduce(true) { |acc, x| acc && is_valid(x[0], x[1]) }

  rv
end

def part1(input : String) : Int32
  parsed = parse(input)
  filtered = parsed
    .select { |x| check_monotonic(x) }
    .select { |x| check_diff(x) }
  filtered.size
end

def valid_arr(list : Array(Int32)) : Bool
  check_monotonic(list) && check_diff(list)
end

def make_good(arr : Array(Int32)) : Tuple(Bool, Array(Int32))
  if valid_arr(arr)
    return {true, arr}
  end

  valid_idx = (0...arr.size)
    .select { |idx| valid_arr(
      arr[...idx] + arr[idx + 1..]
    ) }
    .first?
  if valid_idx == nil
    return {false, arr}
  end
  idx = valid_idx.as(Int32)
  {true, arr[..idx - 1] + arr[idx + 1..]}
end

def part2(input : String) : Int32
  parsed = parse(input)
  valids = parsed
    .map { |x| make_good(x) }
    .select { |x| x[0] }
    .map { |x| x[1] }

  valids.size
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

describe "day02" do
  input = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"
  it "part1" do
    parsed = parse(input)
    got = part1(input)
    got.should eq 2
  end
  it "part2" do
    parsed = parse(input)
    got = part2(input)
    got.should eq 4
  end
end
