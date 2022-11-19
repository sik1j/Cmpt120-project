# Your header
# Jonathan Chan 301553184
# Sikij Karki 301

# your mother is a very nice woman

import cmpt120image
import random

# Jon
def recolorImage(img,color):
  # if r<255 or g<255 or b<255 then not white
  # set rgb to color, r=color[0], g=color[1], b=color=[2]
  # use cmpt120image.getBlackImage()
  image_height = len(img)
  image_width = len(img[0])
  new_img = cmpt120image.getBlackImage(image_width, image_height)
  for x in range(image_height):
    for y in range(image_width):
      if img[x][y] != [255, 255, 255]:
        new_img[x][y] = color
      else:
        new_img[x][y] = [255, 255, 255]
  return new_img
# Sikij
def minify(img):
  # Add your code here
  
def mirror(img):
  # Add your code here
  
def drawItem(canvas,item,row,col):
  # Add your code here
  
def distributeItems(canvas,item,n): 
  #loop to draw n items
  for i in range(n):
    row = random.randint(0, 300)
    col = random.randint(0, 400)
    drawItem(canvas, item, row, col)
