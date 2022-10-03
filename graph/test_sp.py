import matplotlib.pyplot as plt
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

obj1=Dijkstra(g)
x1=[1,2,3,5,10]
y1=[]
kpi1=KPI(obj1)
kpis=kpi1.calcIndicators(obj1.generatePath, ['285','248',[['time']]])
y1.append(kpis['executionTime'])
kpis=kpi1.calcIndicators(obj1.generatePath, ['285','273',[['time']]])
y1.append(kpis['executionTime'])
kpis=kpi1.calcIndicators(obj1.generatePath, ['285','198',[['time']]])
y1.append(kpis['executionTime'])
kpis=kpi1.calcIndicators(obj1.generatePath, ['285','245',[['time']]])
y1.append(kpis['executionTime'])
kpis=kpi1.calcIndicators(obj1.generatePath, ['285','279',[['time']]])
y1.append(kpis['executionTime'])

obj2=Astar(g)
y2=[]
kpi2=KPI(obj2)
kpis=kpi2.calcIndicators(obj2.generatePath, ['285','248',[['time']], [EuclideanForTube]])
y2.append(kpis['executionTime'])
kpis=kpi2.calcIndicators(obj2.generatePath, ['285','273',[['time']], [EuclideanForTube]])
y2.append(kpis['executionTime'])
kpis=kpi2.calcIndicators(obj2.generatePath, ['285','198',[['time']], [EuclideanForTube]])
y2.append(kpis['executionTime'])
kpis=kpi2.calcIndicators(obj2.generatePath, ['285','245',[['time']], [EuclideanForTube]])
y2.append(kpis['executionTime'])
kpis=kpi2.calcIndicators(obj2.generatePath, ['285','279',[['time']], [EuclideanForTube]])
y2.append(kpis['executionTime'])
plt.plot(x1, y1, label = "Dijkstra")
plt.plot(x1, y2, label = "Astar Euclidean")
plt.xlabel('Path Length')
plt.ylabel('Execution time')
plt.title('Dijkstra vs Astar')
plt.legend()
plt.show()