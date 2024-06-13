from modules.itb import itb
from modules.btf import btf

i = input("Input file path: ")
s = i.rsplit(".", -1)

b2, extension = itb(f"{s[0]}.png")
btf(b2, f"{s[0]}_output.{extension}")
