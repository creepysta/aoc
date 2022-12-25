package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func parseInp(fname string) [][]int {

  readFile, err := os.Open(fname)

  if err != nil {
    panic(err)
  }
  fileScanner := bufio.NewScanner(readFile)
  defer readFile.Close()

  fileScanner.Split(bufio.ScanLines)

  matrix := make([][]int, 0)
  for fileScanner.Scan() {
    row := make([]int, 0)
    line := fileScanner.Text()
    tokens := strings.Split(line, "")
    for _, num := range tokens {
      num, _ := strconv.Atoi(num)
      row = append(row, num)
    }
    matrix = append(matrix, row)
  }
  return matrix
}
