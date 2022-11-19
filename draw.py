# Your header
# Jonathan Chan 301553184
# Sikij Karki 301

# your mother is a very nice woman

import cmpt120image
import random

# Jon
def recolorImage(img,color):
  ###outline in the color for some reason###
  # saves the height and width of the image
  image_height = len(img)
  image_width = len(img[0])
  # creates an mage to be modified
  new_img = cmpt120image.getBlackImage(image_width, image_height)
  # loops to go through all pixels of the image
  for x in range(image_height):
    for y in range(image_width):
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
  
def mirror(img):
  # saves the height and width of the image
  image_height = len(img)
  image_width = len(img[0])
  # creates an mage to be modified
  new_img = cmpt120image.getBlackImage(image_width, image_height)
  # loops to go through all pixels of the image
  for x in range(image_height):
    for y in range(image_width):
      #sets the pixel on the flip side to the current pixel
      c = image_width - x
      new_img[y][c] = img[y][x]
  # returns the new image
  return new_img
  
def drawItem(canvas,item,row,col):
  # Add your code here
  
def distributeItems(canvas,item,n): 
  #loop to draw n items
  for i in range(n):
    row = random.randint(0, 300)
    col = random.randint(0, 400)
    drawItem(canvas, item, row, col)
