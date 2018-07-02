# Image data Printing
'''from PIL import Image


pic= Image.open("senna.jpg")
#pic.show()
data=list(pic.getdata())
print(data)

file=open("data.txt","w")
for f in data:
    file.write(str(f)+"\n")
'''

# Image matplot
from  PIL import Image
import matplotlib.pyplot as plt
import numpy as np

pic= Image.open("senna.jpg")
#pic.show()
data=np.array(pic)
#print(data)
fig=plt.figure()
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=4)
ax1.imshow(pic)
plt.show()

