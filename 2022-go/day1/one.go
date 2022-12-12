package main

import (
	"fmt"
	"math"
)

func OneRun() {
  var sum int64 = 0
  var maxCal int64 = math.MinInt64

  lines := parseInp("p1.in")
  for _, sublines := range lines {
    sum = 0
    for _, num := range sublines {
      sum += num
    }
    maxCal = max(sum, maxCal)
  }
  fmt.Println(maxCal)
}
