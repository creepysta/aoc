package main

import "fmt"

func p2(fpath string) int {
  matrix := parseInp(fpath)
  ans := 0
  for i:=0; i<len(matrix); i++ {
    for j:=0; j<len(matrix[i]); j++ {
      element := matrix[i][j]
      right, down, left, up := 0, 0, 0, 0
      //check left
      for k:=j-1; k >= 0; k-- {
        left++
        if element <= matrix[i][k] {
          break
        }
      }
      // check up
      for k:=i-1; k >= 0; k-- {
        up++
        if element <= matrix[k][j] {
          break
        }
      }
      // check right
      for k:=j+1; k < len(matrix[i]); k++ {
        right++
        if element <= matrix[i][k] {
          break
        }
      }
      // check down
      for k:=i+1; k < len(matrix); k++ {
        down++
        if element <= matrix[k][j] {
          break
        }
      }
      calc := right * up * down * left
      if calc >= ans {
        ans = calc
      }
    }
  }
  fmt.Println(ans)
  return ans
}
