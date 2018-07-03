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

# file bytecodes
def createExample():
    numberArrayExample =open('numArraEx.txt','a')
    numbersWeHave=range(0,10)
    print(numbersWeHave)
    versionWeHave=range(1,10)
    print(versionWeHave)
    for eachNum in numbersWeHave:
    #numberArrayExample.write("\n")
        for eachVer in versionWeHave:
            #numberArrayExample.write(str(eachNum)+","+str(eachVer)+"\t")
            imgFilePath='images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei=Image.open(imgFilePath)
            eiar=np.array(ei)
            eiar1=str(eiar.tolist())
            lineToWrite=str(eachNum)+'::'+eiar1+'\n'
            numberArrayExample.write(lineToWrite)
createExample()'''
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
plt.show() '''
'''
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
'''

# Image Recognize

import time
from functools import reduce

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter

def whatNumIsThis(filePath):
    matchedArr=[]
    loadExamps=open('numArraEx.txt','r').read()
    loadExamps=loadExamps.split('\n')

    i=Image.open(filePath)
    iar=np.array(i)
    iar1=iar.tolist()
    inQuestion=str(iar1)
    for eachExample in loadExamps:
        if len(eachExample)>3:
            splitEx=eachExample.split('::')
            currentNum=splitEx[0]
            currentArray=splitEx[1]

            eachPixEx=currentArray.split('],')
            eachPixInQ=inQuestion.split('],')
            x=0
            while x<len(eachPixEx):
                if eachPixEx[x]==eachPixInQ[x]:
                    matchedArr.append(int(currentNum))
                x+=1
    print(matchedArr)
    x=Counter(matchedArr)
    print(x)
whatNumIsThis("/home/hpe/PycharmProjects/untitled2/1.1.png")
