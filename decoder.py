import sys
import argparse
from modules.itb import itb
from modules.btf import btf

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="input file")
args = parser.parse_args()

if not args.file:
    print("No input file provided")
    sys.exit(1)

i = args.file
s = i.rsplit(".", -1)

b2, extension = itb(f"{s[0]}.png")
btf(b2, f"{s[0]}_output.{extension}")
