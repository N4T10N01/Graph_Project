try:
    from graph.kpiParticipant import KPIParticipant
    from graph.itinerary.itineraryObject import ItineraryObject
    from graph.itinerary.heuristic import BaseHeuristic
    from graph.undirectedGraph import UndirectedGraph
    from graph.itinerary.priorityQueue import NodePriorityQueue
    from graph.edge import Edge
    from graph.node import Node
except ModuleNotFoundError:
    import sys
    sys.path.append('..')
    from graph.kpiParticipant import KPIParticipant
    from graph.itinerary.itineraryObject import ItineraryObject
    from graph.itinerary.heuristic import BaseHeuristic
    from graph.undirectedGraph import UndirectedGraph
    from graph.itinerary.priorityQueue import NodePriorityQueue
    from graph.edge import Edge
    from graph.node import Node


class ShortestPath(ItineraryObject, KPIParticipant):

    def __init__(self, graph: UndirectedGraph) -> None:
        self.pq = NodePriorityQueue(len(graph.nodeList))
        self.edgeTo = {}
        self.distTo = {}
        self.nodeFromID = ''
        self.nodeToID = ''
        self.kpi = {'nodesChecked': 0, 'edgesChecked': 0}
        self.graph = graph
        self.nodeFound = False

    def generatePath(self, nodeFromID: str, nodeToID: str,
                     weightTypes: list[str]) -> list[dict, dict]:
        return None

    def givePath(self) -> list[str]:
        if not self.nodeFound:
            return None
        path = []
        id = self.nodeToID
        while (id != self.nodeFromID):
            path.append(id)
            id = self.edgeTo.get(id, Edge(id, self.nodeFromID)).other(id)
        path.append(self.nodeFromID)
        return path

    def giveKPIs(self) -> dict:
        return self.kpi

    def weightTotal(self):
        if not self.nodeFound:
            return None
        return self.distTo[self.nodeToID]


class Dijkstra(ShortestPath):

    def __init__(self, graph: UndirectedGraph) -> None:
        super().__init__(graph)

    def generatePath(self, nodeFromID: str, nodeToID: str,
                     weightTypes) -> tuple:
        self.pq.empty()
        self.nodeFound = False
        if (self.graph.getNode(nodeFromID).ID() == '' or
           self.graph.getNode(nodeToID).ID() == ''):
            return None
        for key in self.kpi.keys():
            self.kpi[key] = 0
        self.nodeFromID = nodeFromID
        self.nodeToID = nodeToID
        nodeFrom = self.graph.getNode(nodeFromID)
        nodeTo = self.graph.getNode(nodeToID)

        self.edgeTo = {nodeFromID: Edge(nodeFromID, '')}

        for n in self.graph.allNodes():  # make method to return node list?
            self.distTo[n.id] = [float('inf') for _ in weightTypes]

        self.distTo[nodeFrom.id] = [0 for _ in weightTypes]

        self.pq.insert(nodeFrom, self.distTo[nodeFrom.id])

        while (not (self.pq.isEmpty())):
            nextNode = self.pq.delMin()
            self.kpi['nodesChecked'] += 1
            if nextNode.id == nodeTo.id:
                self.nodeFound = True
                return self.edgeTo, self.distTo
            self.relax(self.graph, nextNode, weightTypes)

    def relax(self, graph: UndirectedGraph, n: Node,
              weightTypes: list[list[str]]) -> None:
        for eObj in graph.giveAdjacencies(n.id):
            self.kpi['edgesChecked'] += 1
            nodeTo = self.graph.getNode(eObj.other(n.id))
            weightList = []

            for weightGroup in weightTypes:
                weightList.append(eObj.calculateWeight(weightGroup,
                                                       [self.edgeTo[n.id],
                                                        eObj]))

            for i in range(len(weightTypes)):
                if (self.distTo[nodeTo.id][0] >
                        self.distTo[n.id][0] + weightList[0]):
                    # print(f'node from {n.id} node to {nodeTo.id} from
                    # {self.distTo[nodeTo.id][i]} to
                    # {self.distTo[n.id][i]+weightList[i]}')
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


class Astar(ShortestPath):
    def __init__(self, graph: UndirectedGraph) -> None:
        super().__init__(graph)

    def generatePath(self, nodeFromID: str, nodeToID: str,
                     weightTypes: list[str],
                     hList: BaseHeuristic) -> list[Edge]:
        self.pq.empty()
        self.nodeFound = False
        if (self.graph.getNode(nodeFromID).ID() == '' or
           self.graph.getNode(nodeToID).ID() == ''):
            return None
        for key in self.kpi.keys():
            self.kpi[key] = 0
        self.nodeFromID = nodeFromID
        self.nodeToID = nodeToID
        nodeFrom = self.graph.getNode(nodeFromID)
        nodeTo = self.graph.getNode(nodeToID)

        self.edgeTo = {nodeFromID: Edge(nodeFromID, '')}

        for n in self.graph.allNodes():  # make method to return node list?
            self.distTo[n.id] = [float('inf') for _ in weightTypes]

        self.distTo[nodeFrom.id] = [0 for _ in weightTypes]

        for i in range(len(hList)):
            hList[i] = hList[i](self.graph, self.nodeFromID, self.nodeToID)

        self.pq.insert(nodeFrom, self.distTo[nodeFrom.id])

        while (not (self.pq.isEmpty())):
            nextNode = self.pq.delMin()
            self.kpi['nodesChecked'] += 1
            if nextNode.id == nodeTo.id:
                self.nodeFound = True
                return self.edgeTo, self.distTo
            self.relaxAStar(self.graph, nextNode, weightTypes, hList)

    def relaxAStar(self, graph: UndirectedGraph, n: Node,
                   weightTypes: list[list[str]],
                   hList: list[BaseHeuristic]) -> None:
        for eObj in graph.giveAdjacencies(n.id):
            self.kpi['edgesChecked'] += 1
            nodeTo = self.graph.getNode(eObj.other(n.id))
            weightList = []

            for weightGroup in weightTypes:
                weightList.append(eObj.calculateWeight(weightGroup,
                                                       [self.edgeTo[n.id],
                                                        eObj]))

            for i in range(len(weightTypes)):
                if (self.distTo[nodeTo.id][0] >
                        self.distTo[n.id][0] + weightList[0]):
                    # print(f'node from {n.id} node to {nodeTo.id} from
                    # {self.distTo[nodeTo.id][i]} to
                    # {self.distTo[n.id][i]+weightList[i]}')
                    self.distTo[nodeTo.id] = [i + j for i, j in
                                              zip(self.distTo[n.id],
                                                  weightList)]
                    self.edgeTo[nodeTo.id] = eObj

                    g = self.distTo[nodeTo.id]
                    h = [obj.h(nodeTo) for obj in hList]
                    f = [i + j for i, j in zip(g, h)]

                    if self.pq.contains(nodeTo):
                        self.pq.change(nodeTo, f)
                    else:
                        self.pq.insert(nodeTo, f)
                elif (self.distTo[nodeTo.id][i] <
                      self.distTo[n.id][i] + weightList[i]):
                    break
