import numpy as np
from PIL import Image
import binascii


def bti(binary, ipath, extension) -> None:
    extension_binary = binascii.hexlify(extension.encode())
    binary = extension_binary + b"00" + binary
    while len(binary) % 3 != 0:
        binary += b"0"
    binary_int = [int(binary[i : i + 2], 16) for i in range(0, len(binary), 2)]

    size = int(np.sqrt(len(binary_int)))
    size = size if size**2 == len(binary_int) else size - 1

    while len(binary_int) > size**2:
        binary_int.pop()

    image_data = np.array(binary_int, dtype=np.uint8).reshape((size, size))
    image = Image.fromarray(image_data)
    image.save(ipath)
