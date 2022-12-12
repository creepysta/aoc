package main

var charIntMap = map[string]int{ }

func setup() {
  for i:=0; i <= 25; i++ {
    charIntMap[string(i + 97)] = 1 + i
  }
  for i:=0; i <= 25; i++ {
    charIntMap[string(i + 65)] = 27 + i
  }
}


func main() {
  setup()
  p1()
  p2()
}

