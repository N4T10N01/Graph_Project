import sys

sys.path.append('C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab')

from typing import Dict
from graph.node import Node
from graph.edge import Edge

class UndirectedGraph:

    def __init__(self,
    nodeList: dict, #typing stuff from lecture 3 here?
    edgeList: dict,
    adjacencyList: dict
    ) -> None:
        self.nodeList=nodeList
        self.edgeList=edgeList
        self.adjacencyList=adjacencyList

    def addNode(self, n:Node) -> None: #O(1)
        self.nodeList[n.id]= n
        self.adjacencyList[n.id]={}
    
    def getNode(self, id:str)-> Node:
        return self.nodeList[id]
    
    def addEdge(self, e:Edge)->None:

        if e.node1 not in self.nodeList.keys() or e.node2 not in self.nodeList.keys():   #O(E) worst case if bad hashing occurs for contains used for in but average should be O(1), so shouldn't matter
            raise ValueError("1 or more nodes do not exist for edge, halting operation") #average should be O(1) as IDs are unique and shouldn't ever fall under a bucket together when searching
                                                                                         #for existence of node in list
        else:
            self.edgeList[e.id]=e
            self.adjacencyList[e.node1][e.id]=e
            self.nodeList[e.node1].degree+=1
            self.adjacencyList[e.node2][e.id]=e
            self.nodeList[e.node2].degree+=1

    def delNode(self, n:str) -> None: #O(E) worst case, must run through all edges which contain node, but nodes should usually contain a fraction of E (access and deletion of edges is O(1))
        for edgeID in self.adjacencyList[n].keys(): #n to n.id if n is entered as node instead of string
            self.adjacencyList[self.edgeList[edgeID].other(n)].pop(edgeID)
            self.edgeList.pop(edgeID)

        self.nodeList.pop(n)
        
    def delEdge(self, e: str) -> None: #O(1) as only 1 edge goes
        edgeObj=self.edgeList[e]
        self.adjacencyList[edgeObj.node1].pop(edgeObj.id)
        edgeObj.node1.degree-=1
        self.adjacencyList[edgeObj.node2].pop(edgeObj.id)
        edgeObj.node2.degree-=1
        self.edgeList.pop(e)
    
    def size(self):
        return len(self.nodeList.keys())
        

class TubeMap(UndirectedGraph):
    def __init__(self,
    nodeList: dict, #typing stuff from lecture 3 here?
    edgeList: dict,
    lineList: dict,
    adjacencyList: dict
    ) -> None:
        super().__init__(nodeList, edgeList, adjacencyList)
        self.lineList=lineList

    def addLine(self, line: list):
        self.lineList[list[0]]=line[1:3]
        
    def delLine(self, lineNum: str):
        self.lineList.pop(lineNum)
        
