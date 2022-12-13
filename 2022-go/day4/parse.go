package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type elves struct {
  e1 slot
  e2 slot
}
type slot struct {
  start int
  end int
}

func parseInp(fname string) []elves {
  readFile, err := os.Open(fname)

  if err != nil {
    fmt.Println(err)
  }
  fileScanner := bufio.NewScanner(readFile)
  defer readFile.Close()

  fileScanner.Split(bufio.ScanLines)

  lines := make([]elves, 0)
  for fileScanner.Scan() {
    line := fileScanner.Text()
    split := strings.Split(line, ",")
    slot1Splits := strings.Split(split[0], "-")
    slot2Splits := strings.Split(split[1], "-")
    slot1Start, _ := strconv.Atoi(slot1Splits[0])
    slot1End, _ := strconv.Atoi(slot1Splits[1])
    slot2Start, _ := strconv.Atoi(slot2Splits[0])
    slot2End, _ := strconv.Atoi(slot2Splits[1])
    e1 := slot{start: slot1Start, end: slot1End}
    e2 := slot{start: slot2Start, end: slot2End}
    elvs := elves{e1: e1, e2: e2}
    lines = append(lines, elvs)
  }
  return lines
}
