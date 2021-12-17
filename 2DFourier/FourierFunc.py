import math
import numpy


def FFT2D(image):
    imageHeight = image.shape[0]
    imageWidth = image.shape[1]
    xPos = 0
    yPos = 0
    xPos2 = 0
    yPos2 = 0

    for xPos in range(0, imageWidth - 1):
        for yPos in range(0, imageHeight - 1):
            for xPos2 in range(0, imageWidth - 1):
                for yPos2 in range(0, imageHeight - 1):
                    image[xPos, yPos] = image[xPos2, yPos2] * numpy.exp(
                        -2j * math.pi * xPos2 * xPos / imageWidth) * numpy.exp(
                        -2j * math.pi * yPos2 * yPos / imageHeight)
    return image


def iFFT2D(image):
    imageHeight = image.shape[0]
    imageWidth = image.shape[1]
    xPos = 0
    yPos = 0
    xPos2 = 0
    yPos2 = 0

    for xPos in range(0, imageWidth - 1):
        for yPos in range(0, imageHeight - 1):
            for xPos2 in range(0, imageWidth - 1):
                for yPos2 in range(0, imageHeight - 1):
                    image[xPos, yPos] = image[xPos2, yPos2] * numpy.exp(
                        2j * math.pi * xPos2 * xPos / imageWidth) * numpy.exp(
                        2j * math.pi * yPos2 * yPos / imageHeight)
    return image
