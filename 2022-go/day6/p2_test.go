package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestP2(t *testing.T) {
  assert := assert.New(t)
  tests := []struct {
    fpath string
    expected int
  }{
    {fpath: "inp.in", expected: 23},   //bvwbjplbgvbhsrlpgdmjqwftvncz 23
    {fpath: "inp1.in", expected: 19},  //mjqjpqmgbljsphdztnvjfqwrcgsmlb 19
    {fpath: "inp2.in", expected: 23},  //nppdvjthqldpwncqszvftbrmjlhg 23
    {fpath: "inp3.in", expected: 29}, //nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg 29
    {fpath: "inp4.in", expected: 26}, //zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw 26
  }
  for _, tt := range tests {
    got := sol(tt.fpath, 14)
    assert.Equal(tt.expected, got, "fpath: %v", tt.fpath)
  }
}
