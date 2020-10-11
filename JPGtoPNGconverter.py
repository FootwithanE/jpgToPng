import sys
import os
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.mkdirs(new_folder)


for file in os.listdir(new_folder):
    img = Image.open(f'{folder}{file}')
    clean_name = os.path.splitext(file)
    img.save(f'{new_folder}{clean_name}.png', 'png')
print('All done!')
