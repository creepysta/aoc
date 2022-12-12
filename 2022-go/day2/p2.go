package main

import (
	"fmt"
)



func scoreP2(line []string) int {
  opp := oppMove[line[0]]
  expectedOutcome := p2Rel[line[1]]
  me := rules[opp][expectedOutcome]
  left, right := shapeScore[rules[me][expectedOutcome]], outComeScore[expectedOutcome]
  //fmt.Println(opp, me, expectedOutcome, rules[me][expectedOutcome], left, right)
  ans := left + right
  return ans
}


func P2() {
  var ans int = 0
  for _, line := range parseInp("p1.in") {
    ans += scoreP2(line)
  }
  fmt.Println(ans)
}
