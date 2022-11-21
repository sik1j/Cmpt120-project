# Your header
# Jonathan Chan 301553184
# Sikij Karki 301546437

import cmpt120image
import random

# Jon


def recolorImage(img, color):
    ###outline in the color for some reason###
    # saves the height and width of the image
    image_height = len(img)
    image_width = len(img[0])
    # creates an mage to be modified
    new_img = cmpt120image.getBlackImage(image_width, image_height)
    # loops to go through all pixels of the image
    for y in range(image_height):
        for x in range(image_width):
            # checks if the pixel is a color or white space
            if img[y][x] != [255, 255, 255]:
                # sets the pixel to the desried color
                new_img[y][x] = color
            else:
                # sets the pixel to white space
                new_img[y][x] = [255, 255, 255]
    # returns the new image
    return new_img

# Sikij


def minify(img):
    # Add your code here
    new_image_height = int(len(img)/2)
    new_image_width = int(len(img[0])/2)

    new_img = cmpt120image.getBlackImage(
        int(new_image_width), int(new_image_height))

    for row in range(new_image_height):
        for column in range(new_image_width):
            color_1 = img[row*2][column*2]
            color_2 = img[row*2][column*2+1]
            color_3 = img[row*2+1][column*2]
            color_4 = img[row*2+1][column*2+1]
            average = [0, 0, 0]

            for i in range(3):
                average[i] = (color_1[i] + color_2[i] +
                              color_3[i] + color_4[i])/4

            new_img[row][column] = average

    return new_img


def mirror(img):
    # saves the height and width of the image
    image_height = len(img)
    image_width = len(img[0])
    # creates an mage to be modified
    new_img = cmpt120image.getBlackImage(image_width, image_height)
    # loops to go through all pixels of the image
    for y in range(image_height):
        for x in range(image_width):
            # sets the pixel on the flip side to the current pixel
            c = image_width - x - 1
            new_img[y][c] = img[y][x]
    # returns the new image
    return new_img


def drawItem(canvas, item, row, col):
    img = cmpt120image.getImage(item)
    image_height = len(img)
    image_width = len(img[0])
    canvas_height = len(canvas)
    canvas_width = len(canvas[0])

    for y in range(row):
        for x in range(col):
            if img[y][x] != [255, 255, 255]:
                canvas[y+row][x+col] = img[y][x]

    return canvas


def distributeItems(canvas, item, n):
    # loop to draw n items
    for i in range(n):
        row = random.randint(0, 300)
        col = random.randint(0, 400)
        drawItem(canvas, item, row, col)


canvas = cmpt120image.getWhiteImage(400, 300)
