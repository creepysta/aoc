package main

import (
	"bufio"
	"os"
  "regexp"
  "strconv"
)

func parseInp(fname string) []BluePrint {

  readFile, err := os.Open(fname)

  if err != nil {
    panic(err)
  }
  fileScanner := bufio.NewScanner(readFile)
  defer readFile.Close()

  fileScanner.Split(bufio.ScanLines)

  bpRe := regexp.MustCompile(`Blueprint (?P<bp>\w+): Each ore robot costs (?P<ore>\d+) ore. Each clay robot costs (?P<clayOre>\d+) ore. Each obsidian robot costs (?P<obsOre>\d+) ore and (?P<obsClay>\d+) clay. Each geode robot costs (?P<gOre>\d+) ore and (?P<gObs>\d+) obsidian.`)
  bps := make([]BluePrint, 0)
  for fileScanner.Scan() {
    line := fileScanner.Text()
    // groupNames := bpRe.SubexpNames()
    bp := BluePrint{}
    for _, match := range bpRe.FindAllStringSubmatch(line, -1) {
      // for groupIdx, group := range match {
      //   name := groupNames[groupIdx]
      //   if name == "" {
      //     name = "*"
      //   }
      //   fmt.Printf("#%d text: '%s', group: '%s'\n", matchNum, group, name)
      // }
      ore, _ := strconv.Atoi(match[2])
      clayOre, _ := strconv.Atoi(match[3])
      obsidianOre, _ := strconv.Atoi(match[4])
      obsidianClay, _ := strconv.Atoi(match[5])
      geodeOre, _ := strconv.Atoi(match[6])
      geodeObsidian, _ := strconv.Atoi(match[7])
      bp.Ore.Ore = ore
      bp.Clay.Ore = clayOre
      bp.Obsidian.Ore = obsidianOre
      bp.Obsidian.Clay = obsidianClay
      bp.Geode.Ore = geodeOre
      bp.Geode.Obsidian = geodeObsidian
    }
    bps = append(bps, bp)
  }
  return bps
}


/*
  #0 text: '1', group: 'bp'
  #0 text: '4', group: 'ore'
  #0 text: '2', group: 'clayOre'
  #0 text: '3', group: 'obsOre'
  #0 text: '14', group: 'obsClay'
  #0 text: '2', group: 'gOre'
  #0 text: '7', group: 'gObs'
*/
