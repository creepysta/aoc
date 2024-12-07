def read(fname : String) : String
  content = File.open("./#{fname}") do |file|
    file.gets_to_end
  end
end

def parse(content : String) : Tuple(Array(Tuple(Int32, Int32)), Array(Array(Int32)))
  groups = content.split("\n\n")

  order = groups[0]
    .split("\n")
    .select { |x| x.size > 0 }
    .map do |x|
      splt = x.split("|").map { |x| x.to_i32 }
      {splt[0], splt[1]}
    end

  updates = groups[1]
    .split("\n")
    .select { |x| x.size > 0 }
    .map { |x| x.split(",")
      .map { |x| x.to_i32 } }

  {order, updates}
end

def part1(input : String) : Int32
  order, updates = parse(input)

  grouped = {} of Int32 => Array(Int32)
  order.each do |x|
    key, val = x
    grouped.put_if_absent(key) { Array(Int32).new } << val
  end

  valid = updates.select do |arr|
    valid_poss = arr.map_with_index do |x, i|
      before = arr[...i].to_set
      options = grouped[x]?
      ok = options == nil
      if options != nil
        ok = !before.intersects?(options.as(Array(Int32)).to_set)
      end
      ok ? 1 : 0
    end

    c_valid = valid_poss.reduce { |acc, x| acc + x }
    c_valid == arr.size
  end

  rv = valid
    .map do |arr|
      mid = arr.size // 2
      arr[mid]
    end
    .reduce { |acc, x| acc + x }

  rv
end

def part2(input : String) : Int32
  order, updates = parse(input)

  grouped = {} of Int32 => Array(Int32)
  order.each do |x|
    key, val = x
    grouped.put_if_absent(key) { Array(Int32).new } << val
  end

  invalid = updates
    .select do |arr|
      invalid_poss = arr.map_with_index do |x, i|
        before = arr[...i].to_set
        options = grouped[x]?
        ok = options == nil
        if options != nil
          ok = before.intersects?(options.as(Array(Int32)).to_set)
        end
        ok
      end

      invalid_poss.find { |x| x == true } != nil
    end
    .map do |arr|
      rv = [] of Int32
      in_deg = {} of Int32 => Int32
      present = arr.to_set

      arr.each do |x|
      end

      rv
    end

  rv = invalid
    .map do |arr|
      mid = arr.size // 2
      arr[mid]
    end
    .reduce { |acc, x| acc + x }

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

describe "day05" do
  input = "47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"

  it "part1" do
    parsed = parse(input)
    got = part1(input)
    got.should eq 143
  end
  it "part2" do
    parsed = parse(input)
    got = part2(input)
    got.should eq 123
  end
end
