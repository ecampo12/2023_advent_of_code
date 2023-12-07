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

	part1_answer := part1(input)
	if part1_answer != 142 {
		t.Errorf("Expected 142, got %d", part1_answer)
	}
}

func TestPart2(t *testing.T) {
	input, err := os.ReadFile("test_input2.txt")
	if err != nil {
		panic(err)
	}

	part2_answer := part2(input)
	if part2_answer != 281 {
		t.Errorf("Expected 281, got %d", part2_answer)
	}
}
