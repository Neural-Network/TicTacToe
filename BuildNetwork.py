from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork

#-----------------from documentation: building a network
from pybrain.structure import FeedForwardNetwork
n = FeedForwardNetwork()
from pybrain.structure import LinearLayer, SigmoidLayer
inLayer = LinearLayer(5)
hiddenLayer = SigmoidLayer(5)
outLayer = LinearLayer(1)
from pybrain.structure import FullConnection
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
n.sortModules()  # causes an error
#--------------------

ds = SupervisedDataSet(5,1) # 5 indices as input and 1 suggest move as output
tf = open('data.txt','r') # target file

for line in tf.readlines():
    data = [int(x) for x in line.strip()if x!='']
    for i in range(0,8):
        for a[i], j in enumerate(data): # http://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
            if j == 1:
                a[i] # problem....trying to add each index of 1 into the data sample. but if there're fewer than 5 1s, then use 0 to fill out the blank
        ds.addSample(a,b,c,d,e,data[9]) 
    
