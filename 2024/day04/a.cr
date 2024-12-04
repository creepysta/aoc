def read(fname : String) : String
  content = File.open("./#{fname}") do |file|
    file.gets_to_end
  end
end

def parse(content : String) : Array(Array(String))
  lines = content.split("\n").select { |x| x.size > 1 }
  lines.map { |x| x.split("") }
end

def get_ch(grid : Array(Array(String)), row : Int32, col : Int32, dy : Int32, dx : Int32, xmul : Int32) : String?
  py, px = row + xmul*dy, col + xmul*dx
  if 0 <= py < grid.size && 0 <= px < grid.first.size
    return grid[py][px]
  end
  nil
end

def check_for_word(grid : Array(Array(String)), row : Int32, col : Int32, dy : Int32, dx : Int32) : Int32
  to_check = ["X", "M", "A", "S"]
  m = to_check
    .map_with_index { |ch, i| get_ch(grid, row, col, dy, dx, i) == ch }
  # p! m
  # puts "#{row}, #{col}, #{dy}, #{dx}"

  m.select { |x| x }.size == to_check.size ? 1 : 0
end

def part1(input : String) : Int32
  grid = parse(input)
  dirs = [1, 0, -1]
    .cartesian_product([1, 0, -1])
    .select { |x| x[0] != 0 || x[1] != 0 }
  rv = (0...grid.size).reduce(0) { |racc, row| racc + (0...grid[row].size)
    .reduce(0) { |cacc, col| cacc + dirs
      .reduce(0) { |dacc, dir| dacc + check_for_word(grid, row, col, dir[0], dir[1]) } } }

  rv
end

def check_for_x(grid : Array(Array(String)), row : Int32, col : Int32) : Int32
  pdiag = [
    {row - 1, col - 1},
    {row, col},
    {row + 1, col + 1},
  ]
  odiag = [
    {row - 1, col + 1},
    {row, col},
    {row + 1, col - 1},
  ]

  pstr, ostr = nil, nil
  if pdiag.select { |x| 0 <= x[0] < grid.size && 0 <= x[1] < grid.first.size }.size == 3
    pstr = pdiag.map { |x| grid[x[0]][x[1]] }.join
  end

  if odiag.select { |x| 0 <= x[0] < grid.size && 0 <= x[1] < grid.first.size }.size == 3
    ostr = odiag.map { |x| grid[x[0]][x[1]] }.join
  end

  checks = ["MAS", "SAM"]
  pcheck = checks.find { |x| x == pstr } != nil
  ocheck = checks.find { |x| x == ostr } != nil

  return 1 if pcheck && ocheck

  0
end

def part2(input : String) : Int32
  grid = parse(input)
  rv = (0...grid.size).reduce(0) { |racc, row| racc + (0...grid[row].size)
    .reduce(0) { |cacc, col| cacc + check_for_x(grid, row, col) } }
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

describe "day04" do
  input = "MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"
  it "part1" do
    parsed = parse(input)
    got = part1(input)
    got.should eq 18
  end
  it "part2" do
    parsed = parse(input)
    got = part2(input)
    got.should eq 9
  end
end
