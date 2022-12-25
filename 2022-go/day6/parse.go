package main

import (
	"bufio"
	"fmt"
	"os"
)

func parseInp(fname string) string {

  readFile, err := os.Open(fname)

  if err != nil {
    fmt.Println(err)
  }
  fileScanner := bufio.NewScanner(readFile)
  defer readFile.Close()

  fileScanner.Split(bufio.ScanLines)

  var lines string
  for fileScanner.Scan() {
    lines = fileScanner.Text()
  }

  return lines
}
