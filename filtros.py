import os
from PIL import Image
import pytesseract
import numpy as np
import cv2
import time
from tqdm import tqdm


def openimage(filename):
    return Image.open(os.path.join(filename))


def negative(img: Image) -> Image:
    """Retorna uma nova imagem correspondente ao negativo de img"""

    negated = Image.new(img.mode, img.size, "red")
    w, h = negated.size
    for i in range(w):
        for j in range(h):
            if img.mode == "RGB":
                r, g, b = img.getpixel((i, j))
                negated.putpixel((i, j), (255 - r, 255 - g, 255 - b))
            elif img.mode == "RGBA":
                r, g, b, a = img.getpixel((i, j))
                negated.putpixel((i, j), (255 - r, 255 - g, 255 - b, a))
            else:
                # silent failure
                pass
    return negated


def media_grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x, y))
            # média das coordenadas RGB
            lum = (pxl[0] + pxl[1] + pxl[2]) // 3
            img.putpixel((x, y), (lum, lum, lum))
    return img


def grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x, y))
            # média ponderada das coordenadas RGB
            lum = int(0.3 * pxl[0] + 0.59 * pxl[1] + 0.11 * pxl[2])
            img.putpixel((x, y), (lum, lum, lum))
    return img
