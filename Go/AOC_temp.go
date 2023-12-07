package main

import (
	"fmt"
	"os"
)

func part1() {
	fmt.Println("Hello World")
}

func part2() {
	fmt.Println("Hello World")
}

func main() {
	input, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(input)
	part1()
	part2()
}
