package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)


func TestP1(t *testing.T) {
  assert := assert.New(t)
  tests := []struct {
    fpath string
    expected int
  }{
    {fpath: "inp.in", expected: 5},   //bvwbjplbgvbhsrlpgdmjqwftvncz 5
    {fpath: "inp1.in", expected: 7},  //mjqjpqmgbljsphdztnvjfqwrcgsmlb 7
    {fpath: "inp2.in", expected: 6},  //nppdvjthqldpwncqszvftbrmjlhg 6
    {fpath: "inp3.in", expected: 10}, //nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg 10
    {fpath: "inp4.in", expected: 11}, //zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw 11
  }
  for _, tt := range tests {
    got := sol(tt.fpath, 4)
    assert.Equal(tt.expected, got, "fpath: %v", tt.fpath)
  }
}
