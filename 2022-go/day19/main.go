package main

import (
  "fmt"
  "flag"
)


func main() {
  inpFptr := flag.String("input", "inp.in", "input file name")
  flag.Parse()
  fmt.Println("Running: ", *inpFptr)
  p1(*inpFptr)
  // p1("in1.in")
  // p2("in1.in")
}

