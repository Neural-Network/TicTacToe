from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
#classification
from pybrain.datasets import ClassificationDataSet 
from pybrain.utilities import percentError
from pybrain.structure.modules import SoftmaxLayer
#graphical
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal


net = buildNetwork(9,9,1, bias = True) # board state - random - suggested final result?
ds = SupervisedDataSet(9,1) # board state and final result
targetFile = open('data.txt','r') 
for line in targetFile.readlines():
    data = [int(x) for x in line.strip()if x!='']
    ds.addSample((data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]),(data[9],))

#------------TRAIN-----------------
trainer = BackpropTrainer(net, ds)
trainer.train()
#trainer.trainUntilConvergence()