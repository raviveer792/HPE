import scipy as sp
import matplotlib.pyplot as plt

data= sp.genfromtxt("web_traffic.tsv",delimiter="\t") #tsv for tab data
x = data[:,0]
y = data[:,1]
plt.scatter(x,y)
plt.title("Web Traffic last Month")
plt.xlabel("Time")
plt.ylabel("Hits/hours")
plt.xticks()
plt.autoscale(tight=True)
plt.grid()
plt.show()