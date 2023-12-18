package main

import (
	"os"
	"testing"
)

func TestPart1(t *testing.T) {
	input, err := os.ReadFile("test_input.txt")
	if err != nil {
		panic(err)
	}

	// fmt.Println(input)
	s := parseInput(input)
	part1_sum := part1(&s)
	expected := 4361
	if part1_sum != expected {
		t.Errorf("Expected %d, got %d", expected, part1_sum)
	}
}

// func TestPart2(t *testing.T) {
// 	input, err := os.ReadFile("test_input.txt")
// 	if err != nil {
// 		panic(err)
// 	}

// 	fmt.Println(input)
// 	if true == false {
// 		t.Errorf("Test Not Implemented")
// 	}
// }
