package main

import "fmt"

func processP2(move Move, stack [][]string) [][]string {
  items := make([]string, 0)
  // get items from src stack `move.from`
  required := move.num
  for i:=0; i < len(stack); i++ {
    //stack[i][stackId]
    item := stack[i][move.from] 
    if item == " " || required == 0 {
      continue
    }
    stack[i][move.from] = " "
    items = append(items, item)
    required--
  }
  // put items in dest stack `move.to`
  dest := make([]string, 0)
  for _, item := range items {
    dest = append(dest, item)
  }
  // reverse items in dest
  for i:= 0; i < len(stack); i++ {
    if stack[i][move.to] == " " {
      continue
    }
    dest = append(dest, stack[i][move.to])
  }
  toPad := len(dest) - len(stack)
  if toPad < 0 {
    toPad = 0
  }
  sizeT := len(dest)
  if sizeT < len(stack) {
    sizeT = len(stack)
  }
  // to pad left and right side of move.to
  // left of `move.to`
  //fmt.Println("current move:", move)
  //fmt.Println("items:", items)
  //fmt.Println("dest:", dest)
  //fmt.Println("toPad:", toPad)
  //fmt.Println("stack:", stack)
  retStack := make([][]string, 0)
  for i:=0; i < sizeT; i++ {
    currRow := make([]string, 0)
    for j:=0; j<len(stack[0]); j++ {
      currRow = append(currRow, " ")
    }
    retStack = append(retStack, currRow)
  }
  //fmt.Println("Prev retStack:", retStack)
  destIdx := len(dest) - 1
  for i:=sizeT - 1; i >= 0; i-- {
    if destIdx >= 0 {
      retStack[i][move.to] = dest[destIdx]
    }
    destIdx--
  }
  for j:=len(stack[0]) - 1; j >= 0; j-- {
    if j == move.to {
      continue
    }
    stackRIdx := len(stack) - 1
    for i:=sizeT - 1; i >= 0; i-- {
      if stackRIdx >= 0 {
        retStack[i][j] = stack[stackRIdx][j]
      }
      stackRIdx--
    }
  }
  //fmt.Println("Modified retStack:", retStack)
  return retStack
}

func p2() {
  //stacks, moves := parseInp("inp.in") // M C D
  stacks, moves := parseInp("in1.in") // TCGLQSLPW

  tempStack := make([][]string, 0)
  //copy stack into tempStack
  for _, row := range stacks {
    currStack := make([]string, 0)
    for _, item := range row {
      currStack = append(currStack, item)
    }
    tempStack = append(tempStack, currStack)
  }

  for _, move := range moves {
    // go down in a given column
    ret := processP2(move, tempStack)
    tempStack = ret
    //break
    //fmt.Println("ret: ", ret)
  }

  ans := make([]string, 0)
  for j:=0; j < len(tempStack[0]); j++ {
    for i:=0; i < len(tempStack); i++ {
      if tempStack[i][j] != " " {
        ans = append(ans, tempStack[i][j])
        break
      }
    }
  }
  fmt.Println("ANS:", ans)
}
