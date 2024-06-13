import binascii


def ftb(path: str) -> bytes:
    with open(path, "rb") as f:
        content = f.read()
        return binascii.hexlify(content)
