from PIL import Image


pic= Image.open("senna.jpg")
#pic.show()
data=list(pic.getdata())
print(data)

file=open("data.txt","w")
for f in data:
    file.write(str(f)+"\n")
