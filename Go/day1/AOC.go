package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part1(input []byte) int {
	lines := strings.Split(string(input), "\n")
	sum := 0
	for _, line := range lines {
		nums := regexp.MustCompile("[0-9]").FindAllString(line, -1)
		if len(nums) == 0 {
			// fmt.Println(line)
			break // this is the empty line at the end of the file
		}
		num, _ := strconv.Atoi(nums[0] + nums[len(nums)-1])
		sum += num
	}
	return sum
}

func part2(input []byte) int {
	numToInt := map[string]string{
		"one":   "o1e",
		"two":   "t2o",
		"three": "th3ee",
		"four":  "f4ur",
		"five":  "fi5e",
		"six":   "s6x",
		"seven": "se7en",
		"eight": "e8ght",
		"nine":  "n9ne",
	}
	sum := 0
	lines := strings.Split(string(input), "\n")
	for _, line := range lines {
		if line == "" {
			break // this is the empty line at the end of the file
		}
		for word, num := range numToInt {
			line = strings.ReplaceAll(line, word, num)
		}
		nums := regexp.MustCompile("[0-9]").FindAllString(line, -1)
		num, _ := strconv.Atoi(nums[0] + nums[len(nums)-1])
		sum += num
	}
	return sum
}

func main() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	part1_answer := part1(input)
	fmt.Printf("Part 1: %d\n", part1_answer)

	part2_answer := part2(input)
	fmt.Printf("Part 2: %d\n", part2_answer)
}
