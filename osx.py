import os
import sys
import shutil
from pathlib import Path

path = Path()

try:
    current_working_directory = path.cwd()
except:
    current_working_directory = os.getcwd()
    

if not 'images' in os.listdir(current_working_directory):
    print('there is no images follder')
    os.mkdir('images')
    if 'images' in os.listdir(current_working_directory):
        print('images folder created')
    else:
        print('some thing went wrong')
else:
    try:
        os.rmdir('images')
    
    except OSError as error:
        shutil.rmtree('images')
        try:
            shutil.rmtree('__pycache__')
        except:
            sys.stdout.write('boy! there is no __pycache__ file to delete ')
        
        # sys.stderr.write(str(error))
        # sys.stderr.flush()
        
        

##cwd
#print(os.getcwd())

##change dir
#print(os.chdir("path"))

##list files
#os.listdir('path')

#deleting folders
#os.removedirs()

#
#os.rename('test.txt',''demo.txt)
#from datetime import datetime
#mod_time = os.stat('demo.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))


#print(os.path.join(os.environ.get('Desktop'),'text.j')

#print(os.environ)