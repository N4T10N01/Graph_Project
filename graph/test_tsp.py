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

obj3=BruteForceTSP(g)
x1=[2,3,4,5,10]
y1=[]
kpi3=KPI(obj3)
kpis=kpi3.calcIndicators(obj3.generatePath, [['285','248'],['time']])
y1.append(kpis['combosChecked'])
kpis=kpi3.calcIndicators(obj3.generatePath, [['285','248','273'],['time']])
y1.append(kpis['combosChecked'])
kpis=kpi3.calcIndicators(obj3.generatePath, [['285','248','273','198'],['time']])
y1.append(kpis['combosChecked'])
kpis=kpi3.calcIndicators(obj3.generatePath, [['285','248','273','198', '272'],['time']])
y1.append(kpis['combosChecked'])
kpis=kpi3.calcIndicators(obj3.generatePath, [['285','248','273','198', '272', '245', '191','136','84','148','279'],['time']])
y1.append(kpis['combosChecked'])
kpis=kpi3.calcIndicators(obj3.generatePath, [['285','1'],['time']]) #will give nothing when no path exists