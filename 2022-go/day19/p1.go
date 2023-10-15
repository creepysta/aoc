package main

import (
  "fmt"
  "time"
)

const LIMIT = 24

var lookUp map[string]int

func processBp(s State, bp BluePrint) int {
  // fmt.Printf("Current Step: %+v\n", s)
  if (s.Time >= LIMIT) {
    // fmt.Printf("Current Step: %+v\n", s)
    rv := s.Geode
    lookUp[s.hash()] = rv
    return rv
  }

  if val, contains := lookUp[s.hash()]; contains {
    // fmt.Printf("Returning state from cache %+v\n", s)
    return val
  }
  rv := 0
  if s.canBuildGeodeRobot(bp) {
    rv = max(rv, processBp(s.step().buildGeodeRobot(bp), bp))
  }
  if s.canBuildObsidianRobot(bp) {
    rv = max(rv, processBp(s.step().buildObsidianRobot(bp), bp))
  }
  if s.canBuildClayRobot(bp) {
    rv = max(rv, processBp(s.step().buildClayRobot(bp), bp))
  }
  if s.canBuildOreRobot(bp) {
    rv = max(rv, processBp(s.step().buildOreRobot(bp), bp))
  }
  rv = max(rv, processBp(s.step(), bp))
  lookUp[s.hash()] = rv
  return rv
}


func p1(fpath string) []int {
  bps := parseInp(fpath)
  rv := make([]int, 0)
  // state := State{ OreRobot: 1 }
  // rrv := processBp(state, bps[1])
  // fmt.Println("ANS: ", rrv)
  // return []int{rrv}
  for i, bp := range bps {
    lookUp = make(map[string]int)
    state := State{ OreRobot: 1 }
    fmt.Printf("%v) Current BluePrint: %+v", i+1, bp)
    from := time.Now()
    res := processBp(state, bp)
    fmt.Printf(" | Ans: %v (Took %v)\n", res, time.Since(from))
    rv = append(rv, res)
  }
  finalAns := 0
  for i, res := range rv {
    finalAns += res * (i+1)
  }
  fmt.Println("Calc: ", rv)
  fmt.Println("Final Ans: ", finalAns)
  return rv
}
