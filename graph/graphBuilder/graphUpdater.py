try:
    from graph.undirectedGraph import TubeMap
    from graph.graphBuilder.csvReader import ColumnCsvReader
    from graph.graphBuilder.collector import BaseCollector, TubeCollector
except ModuleNotFoundError:
    import sys

    sys.path.append("..")
    from graph.undirectedGraph import TubeMap
    from graph.graphBuilder.csvReader import ColumnCsvReader
    from graph.graphBuilder.collector import BaseCollector, TubeCollector


class GraphUpdater:
    def __init__(self, graph, pathList: dict) -> None:
        self.graph = graph
        self.pathList = pathList

    def update(self) -> None:
        self.updateNodes(self.pathList['nodePath'])
        self.updateEdges(self.pathList['edgePath'])

    def updateNodes(self, csvNodePath: str) -> None:
        dict = ColumnCsvReader.read(csvNodePath)
        nodeList = BaseCollector.collectNodes(dict, id=self.pathList['nodeID'])

        for node in nodeList:
            self.graph.addNode(node)

    def updateEdges(self, csvEdgePath: str) -> None:
        dict = ColumnCsvReader.read(csvEdgePath)
        edgeList = BaseCollector.collectEdges(
            dict,
            self.pathList['edgeNodeLabel1'],
            self.pathList['edgeNodeLabel2'],
            self.pathList['weightLabel'],
            self.pathList['uniqueValues']
        )

        for edge in edgeList:
            edge.updateID()  # ensures uniqueness
            self.graph.addEdge(edge)

    def updatePathList(self, key: str, value: str) -> None:
        self.pathList[key] = value


class TubeMapUpdater(GraphUpdater):
    def __init__(self, graph: TubeMap, pathList: dict) -> None:
        super().__init__(graph, pathList)

    def update(self) -> None:
        self.updateNodes(self.pathList['nodePath'])
        self.updateEdges(self.pathList['edgePath'])
        self.updateLines(self.pathList['additionalPaths']['line'])

    def updateEdges(self, csvEdgePath: str) -> None:

        dict = ColumnCsvReader.read(csvEdgePath)
        edgeList = BaseCollector.collectEdges(
            dict,
            self.pathList['edgeNodeLabel1'],
            self.pathList['edgeNodeLabel2'],
            self.pathList['weightLabel'],
            self.pathList['uniqueValues']
        )
        for i in range(len(edgeList)):
            # must be done so lambda function is localized
            edgeList[i].changeWeight({'station': (lambda *args, i=i: 1)})
            edgeList[i].changeWeight(
                {'line': lambda *args, i=i: int(args[0].getInfo('line') !=
                                                args[1].getInfo('line'))})
            edgeList[i].updateID()  # ensures uniqueness
            self.graph.addEdge(edgeList[i])

    def updateLines(self, csvLinePath: str):
        dict = ColumnCsvReader.read(csvLinePath)
        # default identity for lines is line
        lineList = TubeCollector.collectLines(dict)
        for lineNumber, lineAttributes in lineList.items():
            self.graph.addLine([lineNumber, lineAttributes])
