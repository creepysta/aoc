package main

import "fmt"

func p2() {
  ans := 0
  // inp.in // 4
  for _, elvs := range parseInp("in1.in") {
    e1, e2 := elvs.e1, elvs.e2
    if e1.start > e2.start {
      e1, e2 = e2, e1
    }
    if e1.end >= e2.start {
      ans ++
    }
  }
  fmt.Println(ans)
}
