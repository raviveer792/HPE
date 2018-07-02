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
plt.show()'''

from  PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

def threshold(imageArray):
    balanceArr = []
    newArr = imageArray
    for eachrow in imageArray:
        for eachpix in eachrow:
            avgNum=reduce(lambda x,y:x+y,eachpix[:3])/len(eachpix[:3])
            balanceArr.append(avgNum)
            balance = reduce(lambda x, y: x + y, balanceArr) / len(balanceArr)


    for eachrow in newArr:
        for eachpix in eachrow:
                if reduce(lambda x,y:x+y,eachpix[:3])/len(eachpix[:3])>balance:
                    eachpix[0] = 255
                    eachpix[1] = 255
                    eachpix[2] = 255
                    eachpix[3] = 255
                else:
                    eachpix[0] = 0
                    eachpix[1] = 0
                    eachpix[2] = 0
                    eachpix[3] = 255
    return  newArr

pic= Image.open("/home/mohit/PycharmProjects/untitled3/images/sentdex.png")
#pic.show()
data=np.array(pic)
#print(data)
#fig=plt.figure()
ax2=threshold(data)
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=4)
ax1.imshow(ax2)
plt.show()

