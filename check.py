#!/usr/bin/python3

"""
Script to check submissions for a lab-exam
"""

from __future__ import print_function

import os
import subprocess
import json


MAIN_FILE = "main.c"
TIMEOUT = 3


def get_files():
    """Gives list of all submission available"""
    all_files = os.listdir(os.getcwd())
    submissions = [fname for fname in all_files
                   if fname.endswith(".c") and fname not in [MAIN_FILE, __file__]]
    return submissions


def check_program(filename):
    """Compiles and checks all codes available
    Returns marks calculated from the script
    """
    # compile
    try:
        failed = subprocess.call(["gcc", MAIN_FILE, filename, "-lm", "-Wall"],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                                timeout=TIMEOUT)
        if failed:  # non-zero exit code
            return 0
        # run
        score = subprocess.call("./a.out")
        return score
    except subprocess.TimeoutError:
        return 0


def main():
    """Main"""
    submissions = get_files()
    result = {filename.replace(".c", '').upper(): check_program(filename)
              for filename in submissions}
    with open("results.json", "w") as res:
        res.write(json.dumps(result, indent=4))

    print("%s submissions evalutated" % len(submissions))
    print("Results saved in results.json")


if __name__ == "__main__":
    main()
