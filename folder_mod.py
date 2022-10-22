import os
import sys
import shutil
from pathlib import Path

def check_image():
    path = Path()
    try:
        current_working_directory = path.cwd()
    except:
        current_working_directory = os.getcwd()
    
    if not 'images' in os.listdir(current_working_directory):
        sys.stdout.write('there is no images folder')
        os.mkdir(os.path.join(current_working_directory,'images'))
        if 'images' in os.listdir(current_working_directory):
            sys.stdout.write('\nimages folder created')
    else:
        shutil.rmtree('images')
        sys.stdout.write('image folder has been deleted')


check_image()
