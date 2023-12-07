package main

import (
	"fmt"
	"os"
	"os/exec"
)

func copyFile(dst_folder, src_file string, day int) error {
	fileName := "AOC"
	data, err := os.ReadFile(src_file)
	if err != nil {
		fmt.Println("Error reading file: ", err)
	}
	if day == 0 {
		// err = os.WriteFile(fmt.Sprintf("%s/AOC.go", dst_folder), data, 0644)
		// if err != nil {
		// 	fmt.Println("Error writing file: ", err)
		// }
		fileName += "_test"
	}
	err = os.WriteFile(fmt.Sprintf("%s/%s.go", dst_folder, fileName), data, 0644)
	if err != nil {
		fmt.Println("Error writing file: ", err)
	}
	return nil
}

func main() {
	files, err := os.ReadDir(".")
	if err != nil {
		fmt.Println("Error reading directory")
	}
	// for each directory
	day := 1
	for _, file := range files {
		if file.IsDir() {
			// fmt.Println(file.Name())
			day++
		}
	}
	fmt.Printf("Creating folder day%d\n", day)
	newDir := fmt.Sprintf("day%d", day)
	os.Mkdir(newDir, 0755)
	fmt.Println("Copying files")
	if err := copyFile(newDir, "AOC_temp.go", day); err != nil {
		fmt.Println("Error copying file: ", err)
	}

	if err := copyFile(newDir, "test_temp.go", 0); err != nil {
		fmt.Println("Error copying file: ", err)
	}

	os.Chdir(newDir)
	os.Create("input.txt")
	os.Create("test_input.txt")

	cmd := exec.Command("go", "mod", "init", newDir)
	err = cmd.Run()
	if err != nil {
		fmt.Println("Error running go mod init: ", err)
	}
}
