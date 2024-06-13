from modules.ftb import ftb
from modules.bti import bti

i = input("Input file path: ")
b = ftb(i)
s = i.rsplit(".", -1)
bti(b, f"{s[0]}.png", s[1])
