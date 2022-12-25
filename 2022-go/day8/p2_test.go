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
    {fpath: "inp.in", expected: 8},   //bvwbjplbgvbhsrlpgdmjqwftvncz 5
  }
  for _, tt := range tests {
    got := p2(tt.fpath)
    assert.Equal(tt.expected, got, "fpath: %v", tt.fpath)
  }
}
