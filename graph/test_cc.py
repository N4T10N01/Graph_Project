
import sys
sys.path.append('..\\l1-graph-lab')
from graph.kpi import KPI
from graph.graphBuilder.graphUpdater import GraphUpdater
from graph.itinerary.shortestPath import *
from graph.itinerary.tsp import *
from graph.itinerary.componentConnector import *

from graph.undirectedGraph import UndirectedGraph

generatedDict={'nodePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.stations.csv', 'edgePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.connections.csv', 'nodeID': 'id', 'edgeNodeLabel1': 'station1', 'edgeNodeLabel2': 'station2', 'weightLabel': ['time'], 'uniqueValues': [], 'additionalPaths': {'line': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.lines.csv'}}

g=UndirectedGraph({},{},{})
u=GraphUpdater(g, generatedDict)
u.update()

obj4=DijkstraComponentConnector(g, 'zone')

kpi4=KPI(obj4)
kpis=kpi4.calcIndicators(obj4.generatePath, ['3','9',[['time']]])
print(kpis['executionTime'])
kpis=kpi4.calcIndicators(obj4.generatePath, ['1','273',[['time']]])
print(kpis['executionTime'])
kpis=kpi4.calcIndicators(obj4.generatePath, ['4','198',[['time']]])
print(kpis['executionTime'])
kpis=kpi4.calcIndicators(obj4.generatePath, ['9','84',[['time']]])
print(kpis['executionTime'])
kpis=kpi4.calcIndicators(obj4.generatePath, ['84','55',[['time']]])
print(kpis['executionTime'])


