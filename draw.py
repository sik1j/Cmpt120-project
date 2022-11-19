# Your header
# Jonathan Chan 301553184
# Sikij Karki 301

# your mother is a very nice woman

import cmpt120image
import random

# Jon


def recolorImage(img, color):
    # saves the height and width of the image
    image_height = len(img)
    image_width = len(img[0])
    # creates an mage to be modified
    new_img = cmpt120image.getBlackImage(image_width, image_height)
    # loops to go through all pixels of the image
    for x in range(image_height):
        for y in range(image_width):
            # checks if the pixel is a color or white space
            if img[x][y] != [255, 255, 255]:
                # sets the pixel to the desried color
                new_img[x][y] = color
            else:
                # sets the pixel to white space
                new_img[x][y] = [255, 255, 255]
    # returns the new image
    return new_img
# Sikij


def minify(img):
    # Add your code here
    image_height = len(img)
    image_width = len(img[0])

    new_img = cmpt120image.getBlackImage(image_width/2, image_height/2)

    for row in range(image_height/2):
        for column in range(image_width/2):
            color_1 = img[row][column]
            color_2 = img[row][column+1]
            color_3 = img[row+1][column]
            color_4 = img[row+1][column+1]
            average = [0, 0, 0]

            for i in range(3):
                average[i] = (color_1[i] + color_2[i] +
                              color_3[i] + color_4[i])/4

            new_img[row][column] = average

    return new_img


def mirror(img):
    # Add your code here


def drawItem(canvas, item, row, col):
    # Add your code here


def distributeItems(canvas, item, n):
    # loop to draw n items
    for i in range(n):
        row = random.randint(0, 300)
        col = random.randint(0, 400)
        drawItem(canvas, item, row, col)
