from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork

ds = SupervisedDataSet(2,1)
tf = open('data.txt','r') # target file

for line in tf.readlines():
    data = [int(x) for x in line.strip()if x!='']
    for i in range(0,8):
        ds.addSample((data[i],i+1),(data[9],))