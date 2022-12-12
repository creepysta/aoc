package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func parseInp(fname string) [][]int64 {
  readFile, err := os.Open(fname)

  if err != nil {
    fmt.Println(err)
  }
  fileScanner := bufio.NewScanner(readFile)
  defer readFile.Close()

  fileScanner.Split(bufio.ScanLines)

  lines := make([][]int64, 0)
  subLines := make([]int64, 0)
  for fileScanner.Scan() {
    line := fileScanner.Text()
    if len(line) == 0 {
      lines = append(lines, subLines)
      subLines = make([]int64, 0)
    } else {
      num, _ := strconv.ParseInt(line, 10, 64)
      subLines = append(subLines, num)
    }
  }
  lines = append(lines, subLines)
  return lines
}
