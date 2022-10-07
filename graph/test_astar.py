from graph.itinerary.heuristic import EuclideanForTube


try:
    from graph.itinerary.shortestPath import Astar
    from graph.itinerary.shortestPath import BaseHeuristic
    from graph.graphBuilder.graphUpdater import TubeMapUpdater
    from graph.undirectedGraph import TubeMap
    import pytest
except ModuleNotFoundError:
    import sys
    sys.path.append('..\\l1-graph-lab')
    from graph.itinerary.shortestPath import Astar
    from graph.itinerary.shortestPath import BaseHeuristic
    from graph.graphBuilder.graphUpdater import TubeMapUpdater
    from graph.undirectedGraph import TubeMap
    import pytest


@pytest.fixture
def getAlgorithm():
    generatedDict = {'nodePath': '_dataset\\london.stations.csv',
                 'edgePath': '_dataset\\london.connections.csv',
                 'nodeID': 'id',
                 'edgeNodeLabel1': 'station1',
                 'edgeNodeLabel2': 'station2',
                 'weightLabel': ['time'],
                 'uniqueValues': ['line'],
                 'additionalPaths':
                 {'line': '_dataset\\london.lines.csv'}}
    g = TubeMap({}, {}, {}, {})
    u = TubeMapUpdater(g, generatedDict)
    u.update()
    return Astar(g)


@pytest.fixture
def no_end_or_origin() -> list:
    return ['', '', [['time']], [BaseHeuristic]]


@pytest.fixture
def no_end() -> list:
    return ['50', '', [['time']], [BaseHeuristic]]


@pytest.fixture
def no_origin() -> list:
    return ['', '50', [['time']], [BaseHeuristic]]


@pytest.fixture
def same_node() -> list:
    return ['50', '50', [['time']], [BaseHeuristic]]


@pytest.fixture
def two_nodes1() -> list:
    return ['46', '53', [['time']], [BaseHeuristic]]


@pytest.fixture
def two_nodes2() -> list:
    return ['53', '214', [['time']], [BaseHeuristic]]


@pytest.fixture
def many_nodes1() -> list:
    return ['169', '50', [['time']], [BaseHeuristic]]


@pytest.fixture
def many_nodes2() -> list:
    return ['16', '88', [['time']], [BaseHeuristic]]


@pytest.fixture
def no_path(no_end_or_origin, no_end, no_origin):
    return [no_end_or_origin, no_end, no_origin]


@pytest.fixture
def singleton(same_node):
    return [same_node]


@pytest.fixture
def two_path(two_nodes1, two_nodes2):
    return [two_nodes1, two_nodes2]


@pytest.fixture
def many_path(many_nodes1, many_nodes2):
    return [many_nodes1, many_nodes2]


def test_all_cases(no_path,
                singleton,
                two_path,
                many_path,
                getAlgorithm):

    testObj = getAlgorithm
    for case in no_path:
        testObj.generatePath(*case)
        assert testObj.givePath() == None
    
    for case in singleton:
        testObj.generatePath(*case)
        assert len(testObj.givePath()) == 1

    for case in two_path:
        testObj.generatePath(*case)
        assert len(testObj.givePath()) == 2

    for case in many_path:
        testObj.generatePath(*case)
        assert len(testObj.givePath()) > 2
