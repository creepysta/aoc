package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)


func TestP1(t *testing.T) {
  assert := assert.New(t)
  tests := []struct{
    fpath string
    expected []int
  }{
    {fpath: "inp.in", expected: []int{9, 12}},   //bvwbjplbgvbhsrlpgdmjqwftvncz 5
  }
  for _, tt := range tests {
    p1(tt.fpath)
    got := p1(tt.fpath)
    assert.Equal(tt.expected, got, "fpath: %v", tt.fpath)
  }
}
