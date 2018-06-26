import scipy as sv
import pandas as pd
data=pd.read_csv("csvfiled.csv")

#data= sv.genfromtext("csvfiled.csv", delimiter=",")
print(data.describe())
print(data.size)
print(data.head)
print(data.groupby)