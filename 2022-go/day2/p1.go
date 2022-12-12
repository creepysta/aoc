package main

import (
	"fmt"
)


func score(line move) int {
  me, opp := line.me, line.opp
  var ans int = -1
  if rules[me][DRAW] == opp {
    ans = outComeScore[DRAW]
  } else if rules[me][WIN] == opp {
    ans = outComeScore[WIN]
  } else if rules[me][LOSE] == opp {
    ans = outComeScore[LOSE]
  }
  ans += shapeScore[me]
  return ans
}


func P1() {
  var ans int = 0
  for _, line := range parseInp("p1.in") {
    parsedLine := move{opp: oppMove[line[0]], me: myMove[line[1]]}
    ans += score(parsedLine)
  }
  fmt.Println(ans)
}
