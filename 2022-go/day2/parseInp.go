package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func parseInp(fname string) [][]string {
  readFile, err := os.Open(fname)

  if err != nil {
    fmt.Println(err)
  }
  fileScanner := bufio.NewScanner(readFile)
  defer readFile.Close()

  fileScanner.Split(bufio.ScanLines)

  lines := make([][]string, 0)
  for fileScanner.Scan() {
    line := strings.Split(fileScanner.Text(), " ")
    lines = append(lines, line)
  }
  return lines
}
