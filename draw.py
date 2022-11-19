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
  image_width = 
  image_length = 
  for x in range():
    for y in range():
      if img[x][y] != [255, 255, 255]:
        img[x][y] = color
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
