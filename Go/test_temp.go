package main

import (
	"fmt"
	"os"
	"testing"
)

func TestPart1(t *testing.T) {
	input, err := os.ReadFile("test_input.txt")
	if err != nil {
		panic(err)
	}

	fmt.Println(input)
	if true == false {
		t.Errorf("Test Not Implemented")
	}
}

func TestPart2(t *testing.T) {
	input, err := os.ReadFile("test_input.txt")
	if err != nil {
		panic(err)
	}

	fmt.Println(input)
	if true == false {
		t.Errorf("Test Not Implemented")
	}
}
