import os
import sys

def show_info():
    print("Current Working Directory:", os.getcwd())
    print("Python Executable Path:", sys.executable)
    print("Command Line Arguments:", sys.argv)
