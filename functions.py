import numpy as np
import math
from typing import List
from PIL import Image


def load_to_array(path: str) -> List[List[List[int]]]:
    red_factor = 4
    img = Image.open(path)
    print("Image loaded, size: ", img.size, " format: ", img.format)
    red_factor += int(max(img.size) / 256)
    img = img.reduce(red_factor)
    return np.asarray(img)


def make_brightness_matrix(input_matrix: List[List[List[int]]]) -> List[List[float]]:
    brightness_matrix = []
    for row in range(len(input_matrix)):
        brightness_matrix.append([])
        for coln in range(len(input_matrix[row])):
            brightness_matrix[row].append(
                (0.299 * input_matrix[row][coln][0]) +
                (0.587 * input_matrix[row][coln][1]) +
                (0.114 * input_matrix[row][coln][2]))
    return brightness_matrix


def make_ascii_matrix(brightness_matrix: List[List[int]], invert: bool = False) -> List[List[str]]:
    ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B$@"
    ascii_matrix = []
    if (not invert):
        for row in range(len(brightness_matrix)):
            ascii_matrix.append([])
            for coln in range(len(brightness_matrix[row])):
                ascii_matrix[row].append(
                    ascii_string[(round((brightness_matrix[row][coln] / 255) * 65)) - 1])
    else:
        for row in range(len(brightness_matrix)):
            ascii_matrix.append([])
            for coln in range(len(brightness_matrix[row])):
                mapping = 65 - \
                    (round((brightness_matrix[row][coln] / 255) * 65))
                ascii_matrix[row].append(
                    ascii_string[mapping])
    return ascii_matrix


def print_ascii_matrix(ascii_matrix: List[List[str]]) -> None:
    print()
    for row in range(len(ascii_matrix)):
        print()
        for coln in range(len(ascii_matrix[row])):
            print(ascii_matrix[row][coln], end='')
    print()


def all_together(path: str, invert_: bool = False) -> List[List[str]]:
    img_to_arr = load_to_array(path)
    brt_mtrx = make_brightness_matrix(img_to_arr)
    ascii_mtrx = make_ascii_matrix(brt_mtrx, invert=invert_)
    return ascii_mtrx
