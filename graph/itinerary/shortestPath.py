
import sys

sys.path.append('..\\l1-graph-lab')

from graph.graphBuilder.graphUpdater import GraphUpdater
from graph.kpi import KPIParticipant
from graph.itinerary.itineraryObject import ItineraryObject
from graph.itinerary.heuristic import *
from graph.undirectedGraph import *
from priorityQueue import NodePriorityQueue


class ShortestPath(ItineraryObject, KPIParticipant):

    def __init__(self, graph: UndirectedGraph) -> None:
        self.pq=NodePriorityQueue(len(graph.nodeList))
        self.edgeTo={}
        self.distTo={}
        self.nodeFromID=''
        self.nodeToID=''
        self.kpi={'nodesChecked': 0, 'edgesChecked':0}  
        self.graph=graph
        
    def generatePath(self, nodeFromID:str, nodeToID:str, weightTypes:list[str])->list[dict, dict]:
        return None

    def givePath(self) ->list[str]:
        path=[]
        id=self.nodeToID
        while (id!=self.nodeFromID):
            path.append(id)
            id=self.edgeTo[id].other(id)
        path.append(self.nodeFromID)
        return path

    def giveKPIs(self) -> dict:
        return self.kpi

class Dijkstra(ShortestPath):
    
    def __init__(self, graph: UndirectedGraph) -> None:
        super().__init__(graph)  

 
    def generatePath(self, nodeFromID:str, nodeToID:str, weightTypes)->tuple:
        self.nodeFromID=nodeFromID
        self.nodeToID=nodeToID
        nodeFrom=self.graph.getNode(nodeFromID)
        nodeTo=self.graph.getNode(nodeToID)

        self.edgeTo={}
        self.nodesChecked=0
        self.edgesChecked=0
        
        for n in self.graph.nodeList.values(): #make method to return node list?
            self.distTo[n.id]=[float('inf') for weightGroup in weightTypes]

        self.distTo[nodeFrom.id]=[0 for weightGroup in weightTypes]

        self.pq.insert(nodeFrom, self.distTo[nodeFrom.id])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

        while(not(self.pq.isEmpty())):
            nextNode=self.pq.delMin()
            self.kpi['nodesChecked']+=1
            if nextNode.id == nodeTo.id:
                return self.edgeTo, self.distTo
            self.relax(self.graph, nextNode, weightTypes)

        return None

    def relax(self, graph: UndirectedGraph, n:Node, weightTypes:list[list[str]])->None:
        
        for eObj in graph.adjacencyList[n.id].values():
            self.kpi['edgesChecked']+=1
            nodeTo=self.graph.getNode(eObj.other(n.id))
            weightList=[]

            for weightGroup in weightTypes:
                weightList.append(eObj.calculateWeight(weightGroup))

            for i in range(len(weightTypes)):
                if (self.distTo[nodeTo.id][i]>self.distTo[n.id][i]+weightList[i]):
                    self.distTo[nodeTo.id]=[i+j for i,j in zip(self.distTo[n.id], weightList)]
                    self.edgeTo[nodeTo.id]=eObj
                    self.pq.change(nodeTo, self.distTo[nodeTo.id]) if (self.pq.contains(nodeTo)) else self.pq.insert(nodeTo, self.distTo[nodeTo.id])
    

class Astar(ShortestPath):
    def __init__(self, graph: UndirectedGraph) -> None:
        super().__init__(graph)
        
        
    def generatePath(self, nodeFromID:str, nodeToID:str, weightTypes:list[str], hList: BaseHeuristic)->list[Edge]:
        self.nodeFromID=nodeFromID
        self.nodeToID=nodeToID
        nodeFrom=self.graph.getNode(nodeFromID)
        nodeTo=self.graph.getNode(nodeToID)

        self.edgeTo={}
        self.nodesChecked=0
        self.edgesChecked=0

        for i in range(len(hList)):
            hList[i]=hList[i](self.graph, self.nodeFromID, self.nodeToID)

        
        for n in self.graph.nodeList.values(): #make method to return node list?
            self.distTo[n.id]=[float('inf') for weightGroup in weightTypes]

        self.distTo[nodeFrom.id]=[0 for weightGroup in weightTypes]

        self.pq.insert(nodeFrom, self.distTo[nodeFrom.id])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

        while(not(self.pq.isEmpty())):
            nextNode=self.pq.delMin()
            self.kpi['nodesChecked']+=1
            if nextNode.id == nodeTo.id:
                return self.edgeTo, self.distTo
            self.relaxAStar(self.graph, nextNode, weightTypes, hList)

        return None

    def relaxAStar(self, graph: UndirectedGraph, n:Node, weightTypes:list[list[str]], hList: BaseHeuristic)->None:
        
        for eObj in graph.adjacencyList[n.id].values():
            self.kpi['edgesChecked']+=1
            nodeTo=self.graph.getNode(eObj.other(n.id))
            weightList=[]

            for weightGroup in weightTypes:
                weightList.append(eObj.calculateWeight(weightGroup))

            for i in range(len(weightTypes)):
                if (self.distTo[nodeTo.id][i]>self.distTo[n.id][i]+weightList[i]):
                    self.distTo[nodeTo.id]=[i+j for i,j in zip(self.distTo[n.id], weightList)]
                    self.edgeTo[nodeTo.id]=eObj

                    g=self.distTo[nodeTo.id]
                    h=[obj.h(nodeTo) for obj in hList]
                    f=[i+j for i,j in zip(g,h)]

                    self.pq.change(nodeTo, f) if (self.pq.contains(nodeTo)) else self.pq.insert(nodeTo, f)
    
            




