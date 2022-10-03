import sys
sys.path.append('..\\l1-graph-lab')

from graph.graphBuilder.graphUpdater import GraphUpdater


from graph.undirectedGraph import *
from priorityQueue import NodePriorityQueue


class BaseHeuristic:
    def __init__(self, graph: UndirectedGraph, nodeFromID: Node, nodeToID: Node) -> None:
        self.graph=graph
        self.nodeFrom=graph.getNode(nodeFromID)
        self.nodeTo=graph.getNode(nodeToID)
        
    def h(self, currentNode: Node):
        return 0

class EuclideanForTube(BaseHeuristic):
    def __init__(self, graph: UndirectedGraph, nodeFrom: Node, nodeTo: Node) -> None:
        super().__init__(graph, nodeFrom, nodeTo)

    def h(self, currentNode: Node)->float:
        x1=float(currentNode.getInfo('latitude'))
        y1=float(currentNode.getInfo('longitude'))

        x2=float(self.nodeTo.getInfo('latitude'))
        y2=float(self.nodeTo.getInfo('longitude'))
        return ((x1-x2)**2 + (y1-y2)**2)*10
    
class StationCount(BaseHeuristic):

    def __init__(self, graph: UndirectedGraph, nodeFromID: Node, nodeToID: Node) -> None:
        super().__init__(graph, nodeFromID, nodeToID)
        self.distTo={}
        self._bfs()

    def h(self, currentNode: Node)->float:
        return self.distTo.get(currentNode.id) #return self.state.get(currentNode.id, self.state[self.nodeFrom.id]) #

    def _bfs(self):
        marked={}

        queue=[None]*self.graph.size()
        lastIn=0
        firstOut=0

        queue[lastIn]=self.nodeTo.id
        lastIn+=1

        self.distTo[self.nodeTo.id]=0 #goal station is 0 stations away from itself

        while(firstOut!=len(queue)): #while it's not empty
            n=self.graph.getNode(queue[firstOut])
            firstOut+=1
            marked[n.id]=True
    
            # if n.id == self.nodeFrom.id: #should full bfs be run until origin station is found to label every node in graph or should nodes farther than origin be defaulted to inf?
            #     break
            
            for edge in self.graph.adjacencyList[n.id].values():
                other=edge.other(n.id)
                if (not(marked.get(other, False))):
                    marked[other]=True
                    queue[lastIn]=edge.other(n.id)
                    lastIn+=1
                    self.distTo[other]=self.distTo[n.id]+1

            
        






    
    
