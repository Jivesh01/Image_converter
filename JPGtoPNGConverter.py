import sys
import os
from PIL import Image

# grab first and second argument
image_folder = "D:/vs code/pictures"
output_folder = "D:/vs code/new"

# check for the output folder is exist or create it
print(os.path.exists(output_folder))

# loop through image folder
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}/{filename}")

# convert JPG to PNG
    clean_image = os.path.splitext(filename)[0]
    img.save(f"{output_folder}/{clean_image}.png")
    print("all done!")