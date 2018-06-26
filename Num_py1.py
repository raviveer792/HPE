import scipy as sp

'''data= sp.genfromtxt("web_t.csv",delimiter=",") #csv for comma data
print(data)
print(data.shape)
x = data[:,0]
y = data[:,1]
print(x)
print(y)
print(sp.sum(sp.isnan(y)))
x1 = x[~sp.isnan(y)]
y1 = y[~sp.isnan(y)]
print(x1)
print(y1)'''

data= sp.genfromtxt("web_traffic.tsv",delimiter="\t") #tsv for tab data
print(data)
print(data.shape)
x = data[:,0]
y = data[:,1]
print(x)
print(y)
print(sp.sum(sp.isnan(y)))
x1 = x[~sp.isnan(y)]
y1 = y[~sp.isnan(y)]
print(x1)
print(y1)