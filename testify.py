import os
import asyncio
from pathlib import Path

#os.chdir('images')
#os.listdir(os.getcwd())

# async def send():
#     for image in (os.listdir(os.getcwd())):
#         await asyncio.sleep(2)
#         print(image)
        
        
#asyncio.run(send())

from os import listdir
from os.path import isfile, join
mypath = Path('images')
images = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in images:
    print(i)