package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type PartNumbers struct {
	value int
	start int
	end   int
	row   int
}

type Symbol struct {
	value string
	start int
	row   int
}

type Schematic struct {
	PartNumbers []PartNumbers
	Symbols     []Symbol
}

func (s *Schematic) getAdjacentPartNumbers(sym Symbol) []PartNumbers {
	adjacent := []PartNumbers{}
	// seen := map[int]bool{}
	// for _, part := range s.PartNumbers {

	// }
	return adjacent
}

func parseInput(input []byte) Schematic {
	schematic := Schematic{}
	lines := strings.Split(string(input), "\n")
	for row, line := range lines {
		nums := regexp.MustCompile("[0-9]+").FindAllString(line, -1)
		for _, num := range nums {
			index := strings.Index(line, num)
			n, _ := strconv.Atoi(num)
			schematic.PartNumbers = append(schematic.PartNumbers, PartNumbers{n, index, index + len(num), row})
		}

		symbols := regexp.MustCompile("[^.0-9]").FindAllString(line, -1)
		for _, symbol := range symbols {
			// println(symbol)
			index := strings.Index(line, symbol)
			schematic.Symbols = append(schematic.Symbols, Symbol{symbol, index, row})
		}
	}
	return schematic
}

func part1(s *Schematic) int {

	return 0
}

func part2(input []byte) int {
	fmt.Println("Hello World")
	return 0
}

func main() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	// fmt.Println(input)
	s := parseInput(input)
	part1_sum := part1(&s)
	part2_sum := part2(input)
	fmt.Printf("Part 1: %d\n", part1_sum)
	fmt.Printf("Part 2: %d\n", part2_sum)
}
