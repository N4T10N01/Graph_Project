try:
    from graph.itinerary.priorityQueue import NodePriorityQueue
    from graph.undirectedGraph import UndirectedGraph
    from graph.kpiParticipant import KPIParticipant
    from graph.itinerary.itineraryObject import ItineraryObject
    from graph.node import Node
    from graph.edge import Edge
except ModuleNotFoundError:
    import sys
    sys.path.append('..')
    from graph.itinerary.priorityQueue import NodePriorityQueue
    from graph.undirectedGraph import UndirectedGraph
    from graph.kpiParticipant import KPIParticipant
    from graph.itinerary.itineraryObject import ItineraryObject
    from graph.node import Node
    from graph.edge import Edge


class ComponentConnector(KPIParticipant, ItineraryObject):
    def __init__(self, graph: UndirectedGraph, componentID: str) -> None:
        self.componentID = componentID
        self.graph = graph
        self.path = []
        self.islands = {}
        self.kpis = {'edgesChecked': 0, 'nodesChecked': 0}
        pass

    def giveIslands(self):
        return self.islands

    def givePath(self) -> list:
        if self.path == []:
            return None
        return self.path

    def generatePath(self, node1, node2, weightGroups) -> None:
        return super().generatePath()

    def giveKPIs(self) -> dict:
        return self.kpis


class DiComponentConnector(ComponentConnector):

    def __init__(self, graph: UndirectedGraph, componentID: str) -> None:
        super().__init__(graph, componentID)

    def generatePath(self, node1, node2, weightGroups) -> None:
        if (self.graph.getNode(node1).ID() == '' or
           self.graph.getNode(node2).ID() == ''):
            return None

        for key in self.kpis.keys():
            self.kpis[key] = 0
        
        copyGraph = UndirectedGraph(
            self.graph.nodeList, self.graph.edgeList,
            self.graph.adjacencyList)
        self.pq = NodePriorityQueue(len(copyGraph.nodeList))
        self.edgeTo = {}
        self.distTo = {}
        self.islands = {}
        self.path=[]

        innerEdges1, island1, outerEdges1 = self._bfs(node1)
        innerEdges2, island2, outerEdges2 = self._bfs(node2)

        for n in island1:
            if n in island2:
                return None

        island1ID = self.graph.getNode(node1).getInfo(self.componentID)
        island2ID = self.graph.getNode(node2).getInfo(self.componentID)

        island1node = Node('island1')
        island2node = Node('island2')

        island1node.addInfo(self.componentID, island1ID)
        island2node.addInfo(self.componentID, island2ID)

        copyGraph.addNode(island1node)
        copyGraph.addNode(island2node)

        island1Edges = []
        island2Edges = []

        for e in outerEdges1.values():

            if (self.graph.getNode(e.node1).getInfo(self.componentID)
            == island1ID): 
                nodeTo = e.node2

            else:
                nodeTo=e.node1

            edge=Edge('island1', nodeTo, e.weights,
                    e.extraInfo, e.uniqueValues)
            island1Edges.append(edge)
            copyGraph.addEdge(edge)

        for e in outerEdges2.values():

            if (self.graph.getNode(e.node2).getInfo(self.componentID)
            == island2ID): 
                nodeTo = e.node2

            else:
                nodeTo=e.node1

            weights={}

            for type in e.weights.keys():
                weights[type] = lambda *args: float('inf')

            edge=Edge('island2', nodeTo, weights,
                    e.extraInfo, e.uniqueValues)
            island2Edges.append(edge)
            copyGraph.addEdge(edge)

        innerEdges1 |= innerEdges2

        for e in innerEdges1.values():
            self.graph.delEdge(e.id)

        self._dijkstra('island1',
                        weightTypes=weightGroups,
                        graph=copyGraph)

        self.islands = {node1: island1, node2: island2}

        for n in island2:

            id = n
            givenPath = []

            if self.edgeTo.get(id, '') == '':
                continue

            while (id != 'island1'):
                givenPath.append(id)

                id = self.edgeTo[id].other(id)
            givenPath.append('island1')
            self.path.append(givenPath)

    def _bfs(self, origin: str):
        marked = {}
        outer = {}
        innerNodes = []
        innerEdges = {}
        cID = self.graph.getNode(origin).getInfo(self.componentID)

        queue = [None]*self.graph.size()
        lastIn = 0
        firstOut = 0

        queue[lastIn] = origin
        lastIn += 1

        while (queue[firstOut] != None and firstOut != len(queue)):
            self.kpis['nodesChecked'] += 1
            n = queue[firstOut]
            innerNodes.append(n)
            firstOut += 1
            marked[n] = True

            for edge in self.graph.adjacencyList[n].values():
                self.kpis['edgesChecked'] += 1
                other = edge.other(n)

                if (not (marked.get(other, False))
                    and self.graph.getNode(other).getInfo(self.componentID) == cID):
                    innerEdges[edge.id] = edge
                    marked[other] = True
                    queue[lastIn] = edge.other(n)
                    lastIn += 1
                
                elif (self.graph.getNode(other).getInfo(self.componentID) != cID):
                    outer[edge.id] = edge

        return innerEdges, innerNodes, outer
        
    def _dijkstra(self, nodeFromID: str, weightTypes: list, 
                    graph: UndirectedGraph) -> tuple:
        self.pq.empty()
        self.nodeFromID = nodeFromID
        nodeFrom = graph.getNode(nodeFromID)

        self.edgeTo = {nodeFromID: Edge(nodeFromID, '')}

        for n in self.graph.allNodes():  # make method to return node list?
            self.distTo[n.id] = [float('inf') for _ in weightTypes]

        self.distTo[nodeFrom.id] = [0 for _ in weightTypes]

        self.pq.insert(nodeFrom, self.distTo[nodeFrom.id])

        while (not (self.pq.isEmpty())):
            nextNode = self.pq.delMin()
            self.kpis['nodesChecked'] += 1
            self.relax(graph, nextNode, weightTypes)

    def relax(self, graph: UndirectedGraph, n: Node,
              weightTypes: list[list[str]]) -> None:
        for eObj in graph.giveAdjacencies(n.id):
            self.kpis['edgesChecked'] += 1
            nodeTo = graph.getNode(eObj.other(n.id))
            weightList = []

            for weightGroup in weightTypes:
                weightList.append(eObj.calculateWeight(weightGroup,
                                                       [self.edgeTo[n.id],
                                                        eObj]))

            for i in range(len(weightTypes)):
                if (self.distTo[nodeTo.id][0] >
                        self.distTo[n.id][0] + weightList[0]):

                    self.distTo[nodeTo.id] = [i + j for i, j in
                                              zip(self.distTo[n.id],
                                                  weightList)]
                    self.edgeTo[nodeTo.id] = eObj
                    if self.pq.contains(nodeTo):
                        self.pq.change(nodeTo, self.distTo[nodeTo.id])
                    else:
                        self.pq.insert(nodeTo, self.distTo[nodeTo.id])
                elif (self.distTo[nodeTo.id][i] <
                      self.distTo[n.id][i] + weightList[i]):
                    break
