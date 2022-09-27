import sys
sys.path.append('C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab')


from graph.undirectedGraph import UndirectedGraph
from graph.graphBuilder.csvReader import *
from graph.graphBuilder.collector import *

generatedDict={'nodePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.stations.csv', 'edgePath': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.connections.csv', 'nodeID': 'id', 'edgeNodeLabel1': 'station1', 'edgeNodeLabel2': 'station2', 'weightLabel': ['time'], 'uniqueValues': [], 'additionalPaths': {'line': 'C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab\\_dataset\\london.lines.csv'}}
#Note: make these paths relative
class GraphUpdater:
    def __init__(self, graph: UndirectedGraph, pathList: Dict) ->None:
        self.graph=graph
        self.pathList=pathList

    def update(self)->None:
        self.updateNodes(self.pathList['nodePath'])
        self.updateEdges(self.pathList['edgePath'])

    def updateNodes(self, csvNodePath: str)->None:
        dict=readColumnFormat(csvNodePath)
        nodeList=collectNodes(dict, id=self.pathList['nodeID'])

        for node in nodeList:
            self.graph.addNode(node)

    def updateEdges(self, csvEdgePath:str)->None:
        
        dict=readColumnFormat(csvEdgePath)
        edgeList=collectEdges(
            dict, 
            self.pathList['edgeNodeLabel1'], 
            self.pathList['edgeNodeLabel2'],
            self.pathList['weightLabel'],
            self.pathList['uniqueValues']
            )
        
        for edge in edgeList:
            self.graph.addEdge(edge)
    
    def updatePathList(self, key:str, value:str)->None:
        self.pathList[key]=value


# g=UndirectedGraph({},{},{})
# u=GraphUpdater(g, generatedDict)
# u.update()

# for i,v in g.adjacencyList.items():
#     print(i)
#     for x,y in v.items():
#         print(f'{y.id} {y.extraInfo}')

    

    