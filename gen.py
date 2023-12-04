import sys
import os
import glob
import time
import datetime
import re

def main():
    curr_path = sys.path[0]
    os.chdir(curr_path)
    list_of_files = glob.glob('day*')
    latest_folder = max(list_of_files, key=os.path.getctime)
    day = int(re.findall(r"(\d+)", latest_folder)[0]) + 1
    os.mkdir(f"{curr_path}/day{day}")
    os.system(f"cp {curr_path}/AOC_temp.py {curr_path}/day{day}/AOC.py")
    os.system(f"cp {curr_path}/test_temp.py {curr_path}/day{day}/test.py")
    os.chdir(f"{curr_path}/day{day}")
    open("input.txt", "x")
    open("test_input.txt", "x")
    
    print(f"Created day{day} folder")
    # I know I could use gitpython, but I don't want to install it
    os.system("git add .")
    os.system(f"git commit -m \"Created day{day} folder from python\"")
    
if __name__ == "__main__":
    main()