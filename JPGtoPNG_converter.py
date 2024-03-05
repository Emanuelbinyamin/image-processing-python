# run this command.
# It's going to look through all the images here that in jpg,
# and convert them into a png and put them in a new folder called: New.

# Import the necessary libraries
from PIL import Image, ImageFilter
import sys
import os #OS module to grab the path. So that you can say, Hey, I want these files in "image_processing" and I want to write to this "new"-  file.

# using sys: grab first and second arguments: " image_processing/ new/ " - making a new folder.
# check if new/ exsist, if not: create it- so we could put the images in.
# loop through "image_processing".
# convert images to png.
# save to the new folder.

###############################################################
###############################################################

# Open the image
img_path = './images/astro.jpg'
img = Image.open(img_path)
print(img.size)

print("yes")

###############################################################

# Display the original and resized,filterd images
img.show()
resize.show()
filtered_image.show()

print("yes")

###############################################################
###############################################################

# Print information about the images
print("*******************************************************************************")
print("Original image:", img)
print("Filtered image:", filtered_image)
print("*******************************************************************************")
print("Original image:", img)
print("resized image:", resize)
print("*******************************************************************************")