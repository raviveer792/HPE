import scipy as sp
import matplotlib.pyplot as plt

def mean(values):
    return sum(values)/float(len(values))

def variance(values,mean):
    return sum([(x-mean)**2 for x in values])

def covariance(x,mean_x,y,mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i]-mean_x)*(y[i]-mean_y)
        return covar

def plot_regression_line(x,y):
    plt.scatter(x,y,color="m",marker="o",s=30)
    plt.plot(x,y,color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()



data= sp.genfromtxt("web_traffic.csv", delimiter="\t")
x=[row[0] for row in data]
y=[row[1] for row in data]
mean_x,mean_y=mean(x),mean(y)
var_x,var_y=variance(x,mean(x)),variance(y,mean(y))
print('x stats: mean=%.3f variance=%.3f'%(mean_x,var_x))
print('y stats: mean=%.3f variance=%.3f'%(mean_y,var_y))
'''plt.scatter(x,y,color="m",marker="o",s=30)
plt.xlabel('x')
plt.ylabel('y')
plt.show()'''
covar = covariance(x,mean_x,y,mean_y)
print('Covariance: %.3f'%(covar))
plot_regression_line(x,y)