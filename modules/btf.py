import binascii


def btf(binary, fpath) -> None:
    binary = binascii.unhexlify(binary)
    with open(fpath, "wb") as f:
        f.write(binary)
