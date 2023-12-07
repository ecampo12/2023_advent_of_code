package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var Color_max = map[string]int{
	"blue":  14,
	"red":   12,
	"green": 13,
}

func checkGame(game string) bool {
	rounds := strings.Split(strings.Split(game, ":")[1], ";")
	for _, round := range rounds {
		colors := regexp.MustCompile("[0-9]+ (blue|red|green)").FindAllString(round, -1)
		for _, color := range colors {
			c := strings.Split(color, " ")
			num, _ := strconv.Atoi(c[0])
			if num > Color_max[c[1]] {
				return false
			}
		}
	}
	return true
}

func getFewest(game string) []int {
	rounds := strings.Split(strings.Split(game, ":")[1], ";")
	f_blue, f_red, f_green := 0, 0, 0
	for _, round := range rounds {
		colors := regexp.MustCompile("[0-9]+ (blue|red|green)").FindAllString(round, -1)
		for _, color := range colors {
			c := strings.Split(color, " ")
			num, _ := strconv.Atoi(c[0])
			if c[1] == "red" && num > f_red {
				f_red = num
			} else if c[1] == "blue" && num > f_blue {
				f_blue = num
			} else if c[1] == "green" && num > f_green {
				f_green = num
			}
		}
	}
	return []int{f_red, f_blue, f_green}
}

func part1(input []byte) int {
	correct := 0
	games := strings.Split(string(input), "\n")
	for i, game := range games {
		if checkGame(game) {
			correct += i + 1
		}

	}
	return correct
}

func part2(input []byte) int {
	power := 0
	games := strings.Split(string(input), "\n")
	for _, game := range games {
		vals := getFewest(game)
		power += vals[0] * vals[1] * vals[2]
	}
	return power
}

func main() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	part1_sum := part1(input)
	part2_sum := part2(input)
	fmt.Printf("Part 1: %d\n", part1_sum)
	fmt.Printf("Part 2: %d\n", part2_sum)
}
