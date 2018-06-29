'''from  PIL import Image

im = Image.open("Car.jpg")
im.show()
data=list(im.getdata())
print(data)
'''

import io
from urllib.request import urlopen

from PIL import Image

response = urlopen("https://wallpapercave.com/wp/ppQthYS.jpg")
im_f = io.BytesIO(response.read())
im= Image.open(im_f)
#im = im.rotate(90)
#im = im.resize((800,800))
im.save("Download_img.jpg","JPEG")
im.show()