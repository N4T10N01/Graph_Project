try:
    from graph.kpiParticipant import KPIParticipant
    from graph.itinerary.itineraryObject import ItineraryObject
    from graph.undirectedGraph import UndirectedGraph
except ModuleNotFoundError:
    import sys
    sys.path.append('..')
    from graph.kpiParticipant import KPIParticipant
    from graph.itinerary.itineraryObject import ItineraryObject
    from graph.undirectedGraph import UndirectedGraph


class TSP(KPIParticipant, ItineraryObject):
    def __init__(self, graph: UndirectedGraph) -> None:
        self.graph = graph
        self.path = None
        self.kpis = {'edgesChecked': 0, 'nodesChecked': 0, 'combosChecked': 0}
        pass

    def givePath(self) -> list:
        return self.path

    def generatePath(self, nodeList, weightGroups) -> None:
        return super().generatePath()

    def giveKPIs(self) -> dict:
        return self.kpis


class BruteForceTSP(TSP):

    def generatePath(self, nodeList, weightGroups) -> None:
        for key in self.kpis.keys():
            self.kpis[key] = 0
        self.path = None
        adjacencyMatrix = [[float('inf')]*len(nodeList)
                           for i in range(len(nodeList))]

        indexOf = {}
        for i in range(len(nodeList)):
            indexOf[nodeList[i]] = i

        for i in range(len(nodeList)):
            self.kpis['nodesChecked'] += 1
            for edgeObj in self.graph.adjacencyList[nodeList[i]].values():
                self.kpis['edgesChecked'] += 1
                currentNode = nodeList[i]

                try:
                    pos = indexOf[edgeObj.other(currentNode)]
                    # incase there are parallel edges
                    adjacencyMatrix[i][pos] = min(edgeObj.calculateWeight(
                        weightGroups), adjacencyMatrix[i][pos])
                except KeyError:
                    pass

        possibilities = list(self._permutations(nodeList))
        self.kpis['combosChecked'] = len(possibilities)

        bestWeight = float("inf")

        currentWeight = 0
        for nodeCombo in possibilities:
            for i in range(len(nodeCombo)-1):
                currentWeight += adjacencyMatrix[indexOf[nodeCombo[i]]
                                                 ][indexOf[nodeCombo[i+1]]]
            currentWeight += adjacencyMatrix[indexOf[nodeCombo[0]]
                                             ][indexOf[nodeCombo[-1]]]
            if (currentWeight < bestWeight):
                self.path = nodeCombo

    def _permutations(self, nodeList):
        self.kpis['combosChecked'] += 1
        if len(nodeList) <= 1:
            yield nodeList
        else:
            for combo in self._permutations(nodeList[1:]):
                for i in range(len(nodeList)):
                    yield combo[:i]+nodeList[0:1]+combo[i:]
