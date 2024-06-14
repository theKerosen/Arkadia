import sys
import argparse
from modules.ftb import ftb
from modules.bti import bti


parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="input file")
args = parser.parse_args()

if not args.file:
    print("No input file provided")
    sys.exit(1)

i = args.file
b = ftb(i)
s = i.rsplit(".", -1)
bti(b, f"{s[0]}.png", s[1])
