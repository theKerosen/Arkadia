from PIL import Image
import numpy as np
import binascii


def itb(ipath: str):
    i = Image.open(ipath).convert("L")
    idata = np.array(i)
    b = idata.flatten()
    binary = binascii.hexlify(b.tostring())

    extension_binary = binary[:8]
    binary = binary[8:]
    if extension_binary.endswith(b"00"):
        extension_binary = extension_binary[:-2]
    extension = binascii.unhexlify(extension_binary).decode()
    return binary, extension
