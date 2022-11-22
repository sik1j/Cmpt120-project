# draw
# Jonathan Chan 301553184
# Sikij Karki 301546437

import random
import cmpt120image


# Changes the color of all pixels in <img> to <color> except white pixels
def recolorImage(img, color):
    # saves the height and width of the image
    image_height = len(img)
    image_width = len(img[0])
    # creates an image to be modified
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

# <img> width and height are halved
def minify(img):
    # returns image at half sizs
    new_image_height = int(len(img)/2)
    new_image_width = int(len(img[0])/2)

    # black canvas to draw on
    new_img = cmpt120image.getBlackImage(
        int(new_image_width), int(new_image_height))

    # loop through all pixels in new image canvas
    for row in range(new_image_height):
        for column in range(new_image_width):
            # *2 is used to go through half the pixel of the original image
            color_1 = img[row*2][column*2]
            color_2 = img[row*2][column*2+1]
            color_3 = img[row*2+1][column*2]
            color_4 = img[row*2+1][column*2+1]
            # average of 4 pixels used as color for pixel in new image
            average = [0, 0, 0]

            for i in range(3):
                average[i] = (color_1[i] + color_2[i] +
                              color_3[i] + color_4[i])/4

            # set image pixel as average of 4 pixels from original image
            new_img[row][column] = average

    return new_img

# Mirrors <img> over the vertical from left to right
def mirror(img):
    # saves the height and width of the image
    image_height = len(img)
    image_width = len(img[0])
    # creates an image to be modified
    new_img = cmpt120image.getBlackImage(image_width, image_height)
    # loops to go through all pixels of the image
    for y in range(image_height):
        for x in range(image_width):
            # sets the pixel on the flip side to the current pixel
            c = image_width - (x+1)
            new_img[y][c] = img[y][x]
    # returns the new image
    return new_img

# draws <item> onto the <canvas> with <item> top left(0,0) placed at (<row>,<col>)
def drawItem(canvas, item, row, col):
    # takes the arrray format of the item
    img = item
    # saves the sizes of the image and canvas
    image_height = len(img)
    image_width = len(img[0])

    # for loops to go through every pixel of the size of the image
    for y in range(image_height):
        for x in range(image_width):
            # checks if the pixel is white space
            if img[y][x] != [255, 255, 255]:
                # sets the canvas pixel to the appropriate image pixel
                canvas[y+row][x+col] = img[y][x]
    # returns the drawn on canvas
    return canvas


# randomly draws <n> <items> onto <canvas> while ensuring <item> bottom right is within <canvas>
def distributeItems(canvas, item, n):
    img = item

    # the possible largest values the top left of item can be at.
    # item bottom right must be INSIDE the canvas
    # because drawItem doesn't do validation of row col
    adjusted_height = len(canvas) - len(img)
    adjusted_width = len(canvas[0]) - len(img[0])

    # loop to draw n items
    for i in range(n):
        # randomly chooses location
        row = random.randint(0, adjusted_height)
        col = random.randint(0, adjusted_width)
        # draws the item onto the canvas
        drawItem(canvas, item, row, col)

    return canvas
