# import the Python Image processing Library

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import glob, os

# Create an Image object from an Image

# img = '/Users/jordanwalker/Downloads/lance-modis/firemap.2017071-2017080.4096x2048.jpg'
#
# # Crop the iceberg portion
# left, top, right, bottom = 1100, 870, 1700, 1700
# cropped = imageObject.crop((left, top, right, bottom))
#
# # Display the cropped portion
#
# cropped.show()

# cropped_image.save(saved_location)

path = '/Users/jordanwalker/Downloads/lance-modis-sa/'

filelist = glob.glob(os.path.join(path, '*.jpg'))
filenames = sorted(x for x in filelist)

for im in filenames:
    saved_location = im.replace('lance-modis-sa','lance-modis-sa-name')
    im_object = im.split('/')
    img_split = im_object[-1].split('.')
    file_label = img_split[-3]

    imageObject = Image.open(im)
    draw = ImageDraw.Draw(imageObject)
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 16)
    draw.text((5, 5),file_label[0:4],(255,255,255),font=font)
    imageObject.save(saved_location)

    # If you need to crop
    # left, top, right, bottom = 1100, 870, 1700, 1700
    # cropped = imageObject.crop((left, top, right, bottom))
    # cropped.save(saved_location)
