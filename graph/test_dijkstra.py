import pytest
try:
    from graph.itinerary.shortestPath import Dijkstra
    from graph.graphBuilder.graphUpdater import TubeMapUpdater
    from graph.undirectedGraph import TubeMap
except ModuleNotFoundError:
    import sys
    sys.path.append('..\\l1-graph-lab')
    from graph.itinerary.shortestPath import Dijkstra
    from graph.graphBuilder.graphUpdater import TubeMapUpdater
    from graph.undirectedGraph import TubeMap


generatedDict = {'nodePath': '..\\_dataset\\london.stations.csv',
                 'edgePath': '..\\_dataset\\london.connections.csv',
                 'nodeID': 'id',
                 'edgeNodeLabel1': 'station1',
                 'edgeNodeLabel2': 'station2',
                 'weightLabel': ['time'],
                 'uniqueValues': ['line'],
                 'additionalPaths':
                 {'line': '..\\_dataset\\london.lines.csv'}}
g = TubeMap({}, {}, {}, {})
u = TubeMapUpdater(g, generatedDict)
u.update()


@pytest.fixture
def getAlgorithm(g):
    return Dijkstra(g)


@pytest.fixture
def no_end_or_origin() -> list:
    return ['', '', [['time']]]


@pytest.fixture
def no_end() -> list:
    return ['50', '', [['time']]]


@pytest.fixture
def no_origin() -> list:
    return ['', '50', [['time']]]


@pytest.fixture
def same_node() -> list:
    return ['50', '50', [['time']]]


@pytest.fixture
def two_nodes() -> list:
    return ['46', '53', [['time']]]


@pytest.fixture
def many_nodes() -> list:
    return ['169', '50', [['time']]]


@pytest.fixture
def all_cases(no_end_or_origin, no_end, no_origin,
              same_node, two_node, many_node):
    return [no_end_or_origin, no_end, no_origin,
            same_node, two_node, many_node]


@pytest.fixture
def test_all_cases(all_cases):
    testObj = getAlgorithm(g)
    for case in all_cases:
        testObj.generatePath(*case)
        assert testObj.generatePath != []
