
import sys


sys.path.append('C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab')

from graph.itinerary.priorityQueue import NodePriorityQueue
from graph.graphBuilder.graphUpdater import GraphUpdater
from graph.undirectedGraph import UndirectedGraph
from graph.kpi import KPIParticipant
from graph.itinerary.itineraryObject import ItineraryObject
from graph.undirectedGraph import *

class ComponentConnector(KPIParticipant, ItineraryObject):
    def __init__(self, graph: UndirectedGraph, componentID: str) -> None:
        self.componentID=componentID
        self.graph=graph
        self.path=[]
        self.islands={}
        self.kpis={'edgesChecked':0, 'nodesChecked':0}
        pass

    def giveIslands(self):
        return self.islands

    def givePath(self) -> list:
        return self.path

    def generatePath(self, node1, node2, weightGroups) -> None:
        return super().generatePath()

    def giveKPIs(self) -> dict:
        return self.kpis
    
class DijkstraComponentConnector(ComponentConnector):

    def __init__(self, graph: UndirectedGraph, componentID: str) -> None:
        super().__init__(graph, componentID)
    
    def generatePath(self, node1, node2, weightGroups) -> None:
        copyGraph=UndirectedGraph(self.graph.nodeList, self.graph.edgeList, self.graph.adjacencyList)
        self.pq=NodePriorityQueue(len(copyGraph.nodeList))
        self.edgeTo={}
        self.distTo={}
        nodesTo={}
        self.islands={}

        print()
        _, outerEdges1, island1=self._dfs(node1, self.graph.getNode(node1).getInfo(self.componentID), marked={}, outerEdges={}, innerNodes=[])

        _, outerEdges2, island2=self._dfs(node2, self.graph.getNode(node2).getInfo(self.componentID),marked={}, outerEdges={}, innerNodes=[])

        print(island1)
        print("----------------------------------------------------------------------------------")
        print(island2)

        if node1 in island2:
            print("same island, no external path necessary")
            self.path=None
            return

        island1node=Node('island1')
        island1node.addInfo(self.componentID, self.graph.getNode(node1).getInfo(self.componentID))

        island2node=Node('island2')
        island1node.addInfo(self.componentID, self.graph.getNode(node2).getInfo(self.componentID))


       

        island1Edges=[print(e) for e in outerEdges1.values()]
        island2Edges=[Edge(island2node.id, e[0], e[1].weights, e[1].extraInfo, e[1].uniqueValues) for e in outerEdges2.values().values()]

        for n in island1:
            copyGraph.delNode(n)
        for n in island2:
            copyGraph.delNode(n)


        copyGraph.addNode(island1node)
        copyGraph.addNode(island2node)

        for e in island1Edges:
            copyGraph.addEdge(e)
        for e in island2Edges:
            copyGraph.addEdge(e)
            nodesTo[e.other(island2node.id)]=1
        #islands have been compressed into single nodes by this point


        self._dijkstra(island1.id, nodesToID=nodesTo, weightTypes=weightGroups, graph=copyGraph)

        self.islands={node1: island1, node2: island2}

        for n in island2:
            givenPath=[]
            id=node2
            while (id!=node1):
                givenPath.append(id)
                id=self.edgeTo[id].other(id)
            givenPath.append(node1)
            self.path.append(givenPath)

    def _dfs(self,  node: str, nodeComponentID: str, marked, outerEdges, innerNodes):
        # print(node)
        # print(self.graph.getNode(node).getInfo('zone'))
        marked[node]=1
        outerEdges[node]={}
        innerNodes.append(node)
        toBeExplored=[]

        self.kpis['nodesChecked']+=1

        for edge in self.graph.adjacencyList[node].values():
            self.kpis['edgesChecked']+=1
            if self.graph.getNode(edge.other(node)).getInfo(self.componentID)==nodeComponentID and marked.get(edge.other(node),-1)!=1:
                toBeExplored.append(edge.other(node))
            else:
                outerEdges[node][edge.id]=[edge.other(node), edge]
        
        for n in toBeExplored:
            if marked.get(n, -1)==-1:
                marked, outerEdges, innerNodes=self._dfs(n, nodeComponentID, marked, outerEdges, innerNodes)
        
        return marked, outerEdges, innerNodes




    def _dijkstra(self, nodeFromID:str, nodesToID:dict, weightTypes, graph)->tuple:
        self.nodeFromID=nodeFromID
        # self.nodeToID=nodeToID
        nodeFrom=self.graph.getNode(nodeFromID)
        # nodeTo=self.graph.getNode(nodeToID)

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
            if nodesToID.get(nextNode.id, -1) == 1:
                nodesToID.pop(nextNode.id)
                
            if (len(nodesToID)==0):
                return self.edgeTo, self.distTo
            self._relax(graph, nextNode, weightTypes)

        return None

    def _relax(self, graph: UndirectedGraph, n:Node, weightTypes:list[list[str]])->None:
        
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

generatedDict={'nodePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.stations.csv', 'edgePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.connections.csv', 'nodeID': 'id', 'edgeNodeLabel1': 'station1', 'edgeNodeLabel2': 'station2', 'weightLabel': ['time'], 'uniqueValues': [], 'additionalPaths': {'line': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.lines.csv'}}
g=UndirectedGraph({},{},{})
u=GraphUpdater(g, generatedDict)
u.update()

obj=DijkstraComponentConnector(g, 'zone')

obj.generatePath('3','9',[['time']])

print(g.getNode('3').getInfo('zone'))
print(g.getNode('9').getInfo('zone'))

print(obj.givePath())

    