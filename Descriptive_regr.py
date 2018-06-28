

def mean(values):
    return sum(values)/float(len(values))

def variance(values,mean):
    return sum([(x-mean)**2 for x in values])

def covariance(x,mean_x,y,mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i]-mean_x)*(y[i]-mean_y)
        return covar

dataset=[[1,1],[2,3],[4,5],[6,7],[5,4]]
x=[row[0] for row in dataset]
y=[row[1] for row in dataset]
mean_x,mean_y=mean(x),mean(y)
var_x,var_y=variance(x,mean(x)),variance(y,mean(y))
print('x stats: mean=%.3f variance=%.3f'%(mean_x,var_x))
print('y stats: mean=%.3f variance=%.3f'%(mean_y,var_y))

covar = covariance(x,mean_x,y,mean_y)
print('Covariance: %.3f'%(covar))