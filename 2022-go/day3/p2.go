package main

import "fmt"

func p2() {
  ans := 0
  lines := parseInp("p1.in")
  // lines := parseInp("inp.in") // 70
  var seen = map[string]int{}
  var take = map[string]int{}
  for i:=0; i<=len(lines); i++ {
    if i == len(lines) || i % 3 == 0 {
      for key, val := range take {
        if val == 3 {
          ans += charIntMap[key]
        }
      }
      take = map[string]int{}
      if i == len(lines) {
        break
      }
    }
    for _, char := range lines[i] {
      seen[string(char)] = 1
    }
    for key, _ := range seen {
      take[key] += 1
    }
    seen = map[string]int{}
  }
  fmt.Println(ans)
}
