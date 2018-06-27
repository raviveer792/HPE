import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

data =sp.genfromtxt("web_traffic2.tsv",delimiter="\t")
#data =sp.genfromtxt("web_t.csv",delimiter=",")
x=data[:,0]
y=data[:,1]
print(np.mean(x))
print(np.mean(y))
plt.scatter(x,y)
plt.title("web traffic over the last month")
plt.xlabel("time")
plt.ylabel("hits/hour")
plt.xticks()
#f1=sp.poly1d()
fx= sp.linspace(0,x[-1],500)
#fx= sp.linspace(0,50)
plt.plot(fx)
plt.legend(["HEllo=Web_Traffic"],loc="upper right")
plt.autoscale(tight=True)
plt.grid()
plt.show()