import scipy as sp
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    print(x)
    print(y)
    n=sp.size(x)
    print("size- ",n)
    m_x,m_y = sp.mean(x),sp.mean(y)
    print("mean x- ",m_x, "mean y- ",m_y)
    SS_xy=sp.sum(y*x-n*m_y*m_x)
    SS_xx=sp.sum(x*x-n*m_x*m_x)
    print(SS_xx)
    print(SS_xy)
    b_1=SS_xy/SS_xx
    b_0=m_y-b_1*m_x
    return b_0,b_1
def plot_regression_line(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    y_pred=b[0]+b[1]*x
    plt.plot(x,y_pred,color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main():
    #x=sp.array([0,1,2,3,4,5,6,7,8,9])
    #y=sp.array([1,2,3,4,6,8,6,5,4,3])
    data= sp.genfromtxt("web_traffic.csv", delimiter="\t")
   # y = sp.genfromtxt("web_traffic2.tsv", delimiter="\t")
    x = data[:, 0]
    y = data[:, 1]
    b=estimate_coef(x,y)
    print("estimates coefficients :\nb_0={} \
          \nb_1={}".format(b[0],b[1]))
    plot_regression_line(x,y,b)
if __name__=="__main__":
    main()