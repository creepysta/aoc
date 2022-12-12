package main

const (
  WIN   string  = "win"
  DRAW          = "draw"
  LOSE          = "lose"
  ROCK          = "rock"
  PAPER         = "paper"
  SCISSOR       = "scissor"
)

var oppMove = map[string]string{"A": ROCK, "B": PAPER, "C": SCISSOR}
var myMove = map[string]string{"X": ROCK, "Y": PAPER, "Z": SCISSOR}
var shapeScore = map[string]int {ROCK: 1, PAPER: 2, SCISSOR: 3}
var outComeScore = map[string]int{WIN: 6, DRAW: 3, LOSE: 0}

var p2Rel = map[string]string{"X": LOSE, "Y": DRAW, "Z": WIN}

var rules = map[string]map[string]string {
  ROCK: {WIN: SCISSOR, LOSE: PAPER, DRAW: ROCK},
  PAPER: {WIN: ROCK, LOSE: SCISSOR, DRAW: PAPER},
  SCISSOR: {WIN: PAPER, LOSE: ROCK, DRAW: SCISSOR},
}



type move struct {
  opp string
  me  string
}

func main() {
  P1()
  P2()
}

