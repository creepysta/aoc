package main

import "fmt"

func p1(fpath string) int {
  matrix := parseInp(fpath)
  heightMap := make([][]int, len(matrix))
  for i:=0; i < len(matrix); i++ {
    heightMap[i] = make([]int, len(matrix[i]))
  }
  for i:=0; i < len(matrix); i++ {
    heightMap[i][len(matrix[i])-1], heightMap[i][0] = 1, 1
  }
  for i:=0; i < len(matrix[0]); i++ {
    heightMap[0][i], heightMap[len(matrix)-1][i] = 1, 1
  }

  for i:=1; i < len(matrix); i++ {
    curr := matrix[i][0]
    for j:=1; j < len(matrix[i]); j++ {
      element := matrix[i][j]
      if element > curr {
        heightMap[i][j] = 1
        curr = element
      }
    }
  }
  for i:=len(matrix)-2; i >= 0; i-- {
    curr := matrix[i][len(matrix[i])-1]
    for j:=len(matrix[i])-2; j >= 0; j-- {
      element := matrix[i][j]
      if element > curr {
        heightMap[i][j] = 1
        curr = element
      }
    }
  }

  for i:=1; i < len(matrix[0]); i++ {
    curr := matrix[0][i]
    for j:=1; j < len(matrix); j++ {
      element := matrix[j][i]
      if element > curr {
        heightMap[j][i] = 1
        curr = element
      }
    }
  }
  for i:=1; i < len(matrix[0]); i++ {
    curr := matrix[len(matrix)-1][i]
    for j:=1; j < len(matrix); j++ {
      element := matrix[len(matrix)-1-j][i]
      if element > curr {
        heightMap[len(matrix)-1-j][i] = 1
        curr = element
      }
    }
  }

  ans := 0
  //for i:=0; i < len(matrix); i++ {
  //  //fmt.Println(matrix[i])
  //}
  //fmt.Println("/////////////")
  for i:=0; i < len(matrix); i++ {
    //fmt.Println(heightMap[i])
    for j:=0; j < len(matrix[i]); j++ {
      ans += heightMap[i][j]
    }
  }
  fmt.Println(fpath, ans)
  return ans
}
