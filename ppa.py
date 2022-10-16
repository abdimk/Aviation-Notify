from pathlib import Path

path = Path()

current_working_directory = path.cwd()
home = path.home()

#print(home)

#checking weather the path exists 
test = Path("a.py")
print(test.exists())

#is the path file or dict

images = Path('images')
images.parent
print(images.absolute())