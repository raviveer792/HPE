from PIL import  Image

size = 128,128
file="Car.jpg"
im = Image.open(file)
im.thumbnail(size,Image.ANTIALIAS)
im.save(file + ".thumbnail","JPEG")
im.show()