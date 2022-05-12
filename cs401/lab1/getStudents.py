#!/usr/bin/env python3

import sys, subprocess

STUDENT_DIR = '/u1/class/'

pattern = "^[a-zA-Z]{1,4}[0-9]{5}$"
subprocess.run(f"ls /u1/class | grep -E \'{pattern}\'", shell=True)
