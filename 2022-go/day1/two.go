package main

import (
	"fmt"
)

type top_k struct {
  size_t int
  items []int64
}

func (t top_k) init(size_t int) top_k {
  t.size_t = size_t
  t.items = make([]int64, size_t)
  return t
}

func (t top_k) fix(pos int) {
  for i:=t.size_t-1; i > pos; i-- {
    t.items[i] = t.items[i-1]
  }
}

func (t top_k) push(x int64) {
  var pos int = -1;
  var val int64 = -1;
  for idx, item := range t.items {
    if x >= item {
      pos = idx
      val = x
      break
    }
  }
  if pos > -1 {
    t.fix(pos)
    t.items[pos] = val
  }
}

func (t top_k) pop(x int64) int64 {
  return 0
}

func (t top_k) top(x int64) int64 {
  return 0
}

func (t top_k) sum() int64 {
  var sum int64
  for _, item := range t.items {
    sum += item
  }
  return sum
}


func TwoRun() {
  var sum int64 = 0

  lines := parseInp("p1.in")
  var bucket top_k
  bucket = bucket.init(3)
  for _, sublines := range lines {
    sum = 0
    for _, num := range sublines {
      sum += num
    }
    bucket.push(sum)
  }
  fmt.Println(bucket.sum())
}
