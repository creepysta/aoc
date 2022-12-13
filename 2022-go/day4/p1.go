package main

import "fmt"

func span(e slot) int {
  return e.end - e.start
}

func p1() {
  ans := 0
  // inp.in // 2
  for _, elvs := range parseInp("in1.in") {
    e1, e2 := elvs.e1, elvs.e2
    if span(e2) > span(e1) {
      e1, e2 = e2, e1
    }
    if e1.start <= e2.start && e1.end >= e2.end {
      ans ++
    }
  }
  fmt.Println(ans)
}
