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
	part1_sum := part1(input)
	if part1_sum != 8 {
		t.Errorf("Expected 8, got %d", part1_sum)
	}
}

func TestPart2(t *testing.T) {
	input, err := os.ReadFile("test_input.txt")
	if err != nil {
		panic(err)
	}

	part2_prod := part2(input)
	if part2_prod != 2286 {
		t.Errorf("Expected 2286, got %d", part2_prod)
	}
}
