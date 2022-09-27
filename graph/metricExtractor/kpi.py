import sys
sys.path.append('C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab')

import time
from graph.graphBuilder.graphUpdater import GraphUpdater


from graph.metricExtractor.heuristic import *
from graph.metricExtractor.shortestPath import ShortestPath
from graph.undirectedGraph import *

class KPI:
    def __init__(self, objWithKPI):
        self.obj=objWithKPI
        self.kpis=objWithKPI.giveKPI()

    def calcIndicators(self, func, arguments) -> dict:
        t=self._time(func, arguments)
        self.kpis.update({'executionTime':t})
        return self.kpis

    def _time(self, func, arguments) -> float:
        ti=time.time()
        func(*arguments)
        tf=time.time()
        return tf-ti
        
# generatedDict={'nodePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.stations.csv', 'edgePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.connections.csv', 'nodeID': 'id', 'edgeNodeLabel1': 'station1', 'edgeNodeLabel2': 'station2', 'weightLabel': ['time'], 'uniqueValues': [], 'additionalPaths': {'line': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.lines.csv'}}

# g=UndirectedGraph({},{},{})
# u=GraphUpdater(g, generatedDict)
# u.update()

# sp=ShortestPath(g)

# kpi=KPI(sp)

# print(kpi.calcIndicators(sp.Astar, ['197','250',[['time']],[EuclideanForTube]]))


