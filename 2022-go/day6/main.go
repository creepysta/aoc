package main

import "fmt"


func sol(fpath string, numUniq int) int {
  line := parseInp(fpath)
  seen := map[string]int{}
  // a s f a g
  // i i i
  // j
  ans := -1
  for i, j :=0, 0; i<len(line) && j<len(line); i++ {
    char := string(line[i])
    prev := string(line[j])
    seen[char] += 1
    if i - j > numUniq-1 {
      seen[prev] -= 1
      j++
    }
    ones := 0
    if i - j == numUniq-1 {
      for k:= j; k <= i; k++ {
        ones += seen[string(line[k])]
      }
      if ones == numUniq {
        ans = i
        break
      }
    }
  }
  ans = ans + 1
  fmt.Println(ans)
  return ans
}

func main() {
  p1("in1.in", 4)
  p2("in1.in", 14)
}

