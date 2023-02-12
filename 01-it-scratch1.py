import requests

img_url = 'https://dl.dropboxusercontent.com/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg'
filename = img_url.split('/')[-1]
response = requests.get(img_url)
filepath = f'D:\\PyProj\\primerProj\\iterator\\{filename}'
with open(filepath, 'wb') as f:
    f.write(response.content)


import PIL
from PIL import Image

# import time
import os
# import logging
from urllib.parse import urlparse

# from urllib.request import urlretrieve
home_dir = '.'
input_dir = home_dir + os.path.sep + 'incoming'
output_dir = home_dir + os.path.sep + 'outgoing'

img_url = 'https://dl.dropboxusercontent.com/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg'
filename = urlparse(img_url).path.split('/')[-1]
filepath = f'D:\\PyProj\\primerProj\\iterator\\{filename}'
filepath_part1 = os.path.splitext(filename)[0]
filepath_part2 = os.path.splitext(filename)[1]

orig_image = Image.open(filepath)
basewidth = 64
wpercent = basewidth / float(orig_image.size[0])
hsize = int(orig_image.size[1] * wpercent)
img = orig_image.resize((basewidth, hsize), PIL.Image.LANCZOS)
new_filepath = f'D:\\PyProj\\primerProj\\iterator\\{filepath_part1}_{basewidth}{filepath_part2}'
img.save(new_filepath)