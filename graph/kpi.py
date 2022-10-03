import sys
sys.path.append('..\\l1-graph-lab')

import time



class KPI:
    def __init__(self, objWithKPI):
        self.obj=objWithKPI
        self.kpis=objWithKPI.giveKPIs()

    def calcIndicators(self, func, arguments) -> dict:
        t=self._time(func, arguments)
        self.kpis.update({'executionTime':t})
        return self.kpis

    def _time(self, func, arguments) -> float:
        ti=time.time()
        func(*arguments)
        tf=time.time()
        return tf-ti

#must be inherited by all classes that are desired to be used with the KPI class
class KPIParticipant:
    def giveKPIs(self)->dict:
        return None
        
# generatedDict={'nodePath': ..\\l1-graph-lab\\_dataset\\london.stations.csv', 'edgePath': '..\\l1-graph-lab\\_dataset\\london.connections.csv', 'nodeID': 'id', 'edgeNodeLabel1': 'station1', 'edgeNodeLabel2': 'station2', 'weightLabel': ['time'], 'uniqueValues': [], 'additionalPaths': {'line': '..\\l1-graph-lab\\_dataset\\london.lines.csv'}}

# g=UndirectedGraph({},{},{})
# u=GraphUpdater(g, generatedDict)
# u.update()

# sp=ShortestPath(g)

# kpi=KPI(sp)

# print(kpi.calcIndicators(sp.Astar, ['197','250',[['time']],[EuclideanForTube]]))


