#from os import remove,rename,join
from os import rename, remove, listdir, rmdir
from os.path import join, isdir

#remove(join("foo","bar.txt"))
#rename(join("foo","two.txt"),join("foo","Hello.txt"))

print(listdir("foo"))

#rmdir("foo2")
print(isdir("foo"))