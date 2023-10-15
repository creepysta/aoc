package main

import (
  "fmt"
  "reflect"
)

type BluePrint struct {
  Ore struct { Ore int }
  Clay struct { Ore int }
  Obsidian struct {
    Ore int
    Clay int
  }
  Geode struct {
    Ore int
    Obsidian int
  }
}


type State struct {
  Time int

  OreRobot int
  ClayRobot int
  ObsidianRobot int
  GeodeRobot int

  Ore int
  Clay int
  Obsidian int
  Geode int
}

func (s State) canBuildOreRobot(bp BluePrint) (bool) {
  return s.Ore >= bp.Ore.Ore
}

func (s State) canBuildClayRobot(bp BluePrint) (bool) {
  return s.Ore >= bp.Clay.Ore
}

func (s State) canBuildObsidianRobot(bp BluePrint) (bool) {
  return s.Ore >= bp.Obsidian.Ore && s.Clay >= bp.Obsidian.Clay
}

func (s State) canBuildGeodeRobot(bp BluePrint) (bool) {
  return s.Ore >= bp.Geode.Ore && s.Obsidian >= bp.Geode.Obsidian
}

func (s State) buildOreRobot(bp BluePrint) (State) {
  s.OreRobot += 1
  s.Ore -= bp.Ore.Ore
  return s
}

func (s State) buildClayRobot(bp BluePrint) (State) {
  s.ClayRobot += 1
  s.Ore -= bp.Clay.Ore
  return s
}

func (s State) buildObsidianRobot(bp BluePrint) (State) {
  s.ObsidianRobot += 1
  s.Ore -= bp.Obsidian.Ore
  s.Clay -= bp.Obsidian.Clay
  return s
}

func (s State) buildGeodeRobot(bp BluePrint) (State) {
  s.GeodeRobot += 1
  s.Ore -= bp.Geode.Ore
  s.Obsidian -= bp.Geode.Obsidian
  return s
}

func (s State) step() (State) {
  s.Time += 1
  s.Ore += s.OreRobot
  s.Clay += s.ClayRobot
  s.Obsidian += s.ObsidianRobot
  s.Geode += s.GeodeRobot
  return s
}

func (s State) hash() string {
  hash := ""
  typ := reflect.TypeOf(s)
  val := reflect.ValueOf(s)
  n := typ.NumField()
  for i := 0; i < n; i++ {
    fieldVal := val.Field(i).Interface()
    fieldName := typ.Field(i).Name
    if fieldName == "Time" {
      continue
    }
    hash += fmt.Sprintf("%s=%v", fieldName, fieldVal)
    if i < n-1 {
      hash += ";"
    }
  }
  return hash
}
