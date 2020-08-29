import numpy as np
import math
from typing import List
from PIL import Image, ImageShow


def load_to_array(path: str) -> List[List[List[int]]]:
    red_factor = 2
    img = Image.open(path)
    print("Image loaded, size: ", img.size, " format: ", img.format)
    red_factor += int(max(img.size) / 256)
    return np.asarray(img.reduce(red_factor))


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


def make_ascii_matrix(brightness_matrix: List[List[int]]) -> List[List[str]]:
    ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    ascii_matrix = []
    for row in range(len(brightness_matrix)):
        ascii_matrix.append([])
        for coln in range(len(brightness_matrix[row])):
            # print(round((brightness_matrix[row][coln] / 255) * 65))
            ascii_matrix[row].append(
                ascii_string[(round((brightness_matrix[row][coln] / 255) * 65)) - 1])
    return ascii_matrix


def print_ascii_matrix(ascii_matrix: List[List[str]]) -> None:
    print()
    for row in range(len(ascii_matrix)):
        print()
        for coln in range(len(ascii_matrix[row])):
            print(ascii_matrix[row][coln], end='')
    print()


if __name__ == "__main__":
    img_array = load_to_array("test.png")
    brightness = make_brightness_matrix(img_array)
    ascii_matrix = make_ascii_matrix(brightness)

    # for i in range(len(brightness)):
    #     for j in range(len(brightness[0])):
    #         if (i == j):
    #             print(img_array[i][j])
    #             print(brightness[i][j])

    print_ascii_matrix(ascii_matrix)
