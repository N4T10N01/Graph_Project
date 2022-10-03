import sys
sys.path.append('..\\l1-graph-lab')


from graph.graphBuilder.csvReader import *
from graph.node import Node
from graph.edge import Edge 

import graph


def collectNodes(data: dict, id: str, deg: str=None) -> list[Node]:
    nodes=[]

    #could place pre-run through list of id to ensure all ids are unique by placing them in set and comparing that set's length to their list
    for i in range(len(data[id])):
        newNode=Node(id=data[id][i], extraInfo={})

        for label in data.keys():

            if label not in [id, deg]: 
                newNode.addInfo(label, data[label][i])

            elif label == deg:
                newNode.degree=data[label][i]

            nodes.append(newNode)

    return nodes

def collectEdges(data: dict, node1: str, node2: str, weightTypes=[], uniqueValueLabels=[])->list[Edge]:
    edges=[]

    for i in range(len(data[node1])):
        newEdge=Edge(data[node1][i], data[node2][i], uniqueValues=uniqueValueLabels, weights={},extraInfo={})
        weights={}

        for label in data.keys():
            if label not in [node1,node2]+weightTypes:
                newEdge.addInfo(label, data[label][i])

            elif label in weightTypes:
                weights[label]  = int(data[label][i])

        newEdge.changeWeight(weights)
        edges.append(newEdge)

    return edges


def collectLines(data: dict, line="line"):
    lines={}

    for i in range(len(data[line])):
        lineDict={}

        for label in data.keys():
            
            if label not in [line]:
                lineDict[label]=data[label][i]

        lines[data[line][i]]=lineDict


    return lines

# answer2=collectEdges(readColumnFormat('C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.connections.csv'), 'station1', 'station1',weightTypes=['time'])
# print(answer2)
