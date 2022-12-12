package main

import "fmt"

func p1() {
  ans := 0
  for _, line := range parseInp("p1.in") {
    var seen = map[string]int{}
    var take = map[string]int{}
    mid := len(line) / 2
    for i:=0; i < len(line); i++ {
      char := string(line[i])
      if i < mid {
        seen[char] = charIntMap[char]
      } else {
        if seen[char] != 0 {
          take[char] = 1
        }
      }
    }
    for key, _ := range take {
      ans += charIntMap[key]
    }
    fmt.Println(take)
  }
  fmt.Println(ans)
}
