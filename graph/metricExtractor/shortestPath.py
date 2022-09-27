import sys
sys.path.append('C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab')

from graph.graphBuilder.graphUpdater import GraphUpdater



from graph.metricExtractor.heuristic import *
from graph.undirectedGraph import *
from priorityQueue import NodePriorityQueue


class shortestPath:

    def __init__(self, graph: UndirectedGraph) -> None:
        self.graph=graph
        self.pq=NodePriorityQueue(len(graph.nodeList))
        self.edgeTo={}
        self.distTo={}
        self.nodeFromID=''
        self.nodeToID=''
        self.kpi={'nodesChecked': 0, 'edgesChecked':0}
        
    def givePath(self): #possibly should redefine this to intrisically create a path through an object instead of needing to re-enter nodes givein in this method
        path=[]
        id=self.nodeToID
        while (id!=self.nodeFromID):
            path.append(id)
            id=edgeTo[id].other(id)
        path.append(self.nodeFromID)
        return path
 
    def dijkstra(self, nodeFromID:str, nodeToID:str, weightTypes:list[str])->list[Edge]:
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

    def Astar(self, nodeFromID:str, nodeToID:str, weightTypes:list[str], hList: BaseHeuristic)->list[Edge]:
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
            



generatedDict={'nodePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.stations.csv', 'edgePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.connections.csv', 'nodeID': 'id', 'edgeNodeLabel1': 'station1', 'edgeNodeLabel2': 'station2', 'weightLabel': ['time'], 'uniqueValues': [], 'additionalPaths': {'line': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.lines.csv'}}
        
g=UndirectedGraph({},{},{})
u=GraphUpdater(g, generatedDict)
u.update()

shortpath=shortestPath(g)

edgeTo, distTo=shortpath.Astar('197','250',[['time']],[EuclideanForTube])

print(shortpath.kpi['nodesChecked'])

print(shortpath.givePath()) 

sp=shortestPath(g)

astar=sp.Astar

edgeTo, distTo=astar('197','250',[['time']],[EuclideanForTube])