from graph.node import Node
from typing import Any

class Edge:

    def __init__(self,node1:str,node2:str, weights={}, extraInfo={}, uniqueValues=[]) -> None:
        self.id=''
        self.node1=node1
        self.node2=node2
        self.weights=weights
        self.extraInfo=extraInfo
        self.uniqueValues=uniqueValues
        self.updateID(self.uniqueValues)
        

    def other(self, n: str) -> str:
        if n==self.node1:
            return self.node2
        else:
            return self.node1

    def addInfo(self, infoType, value) -> None:
        self.extraInfo[infoType]=value
    
    def getInfo(self, infoType) -> Any:
        return self.extraInfo[infoType]

    def changeWeight(self, newWeights):
        self.weights.update(newWeights)
        self.updateID(self.uniqueValues)
    
    def updateID(self, uniqueValues=[]):
        self.id=self.node1+self.node2+str(sum(self.weights.values())) #list should be small
        for uniqueValue in uniqueValues:
            self.id+=self.extraInfo[uniqueValue]  #list should be a small amount, some constant under 100, therefore, low, or empty
       
    def calculateWeight(self, weightTypes=None):
        if weightTypes==None:
            return sum(self.weights.values())
        else:
            return sum(self.weights[weightType] for weightType in weightTypes)
      
