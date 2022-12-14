package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Move struct {
  num int
  from int
  to int
}


func parseInp(fname string) ([][]string, []Move) {

  readFile, err := os.Open(fname)

  if err != nil {
    fmt.Println(err)
  }
  fileScanner := bufio.NewScanner(readFile)
  defer readFile.Close()

  fileScanner.Split(bufio.ScanLines)

  // parse top stacks
  stacks := make([][]string, 0)
  moves := make([]Move, 0)
  //fmt.Println("Parsing Stacks")
  for fileScanner.Scan() {
    line := fileScanner.Text()
    if len(line) == 0 {
      break
    }
    // check for blocks of 3
    currentLevel := make([]string, 0)
    for i:=0; i <= len(line); i+=4 {
      if line[i] != '[' {
        currentLevel = append(currentLevel, " ")
      } else {
        currentLevel = append(currentLevel, string(line[i+1]))
      }
    }
    stacks = append(stacks, currentLevel)
    //fmt.Println(currentLevel)
  }
  stacks = stacks[:len(stacks)-1]
  //fmt.Println("Stacks: ", stacks)

  //fmt.Println("Parsing moves")
  r := regexp.MustCompile(`move \d+ from \d+ to \d+`)
  for fileScanner.Scan() {
    line := fileScanner.Text()
    ret := r.FindAllString(line, -1)
    ret = strings.Split(ret[0], " ")
    num, _ := strconv.Atoi(ret[1])
    from, _ := strconv.Atoi(ret[3])
    to, _ := strconv.Atoi(ret[5])
    currMove := Move{
      num: num,
      from: from-1,
      to: to-1,
    }
    moves = append(moves, currMove)
    //fmt.Println(currMove)
  }
  //fmt.Println("Moves: ", moves)

  return stacks, moves
}
