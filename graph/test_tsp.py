try:
    import pytest
    from graph.graphBuilder.graphUpdater import TubeMapUpdater
    from graph.itinerary.tsp import BruteForceTSP
    from graph.undirectedGraph import TubeMap
except ModuleNotFoundError:
    import sys
    sys.path.append('..\\l1-graph-lab')
    from graph.graphBuilder.graphUpdater import TubeMap
    from graph.itinerary.tsp import BruteForceTSP
    from graph.undirectedGraph import TubeMap


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
    return BruteForceTSP(g)


@pytest.fixture
def no_end_or_origin() -> list:
    return [['', ''], ['time']]


@pytest.fixture
def no_end() -> list:
    return [['50', ''], ['time']]


@pytest.fixture
def no_origin() -> list:
    return [['', '50'], ['time']]


@pytest.fixture
def same_node() -> list:
    return [['50', '50'], ['time']]


@pytest.fixture
def two_nodes_c() -> list:
    return [['285', '248'], ['time']]


@pytest.fixture
def two_nodes_dc() -> list:
    return [['50', '199'], ['time']]


@pytest.fixture
def many_nodes_3v1() -> list:
    return [['285', '87', '279'], ['time']]


@pytest.fixture
def many_nodes_3v2() -> list:
    return [['116', '118', '117'], ['time']]


@pytest.fixture
def no_path(no_end_or_origin, no_end, no_origin, two_nodes_dc):
    return [no_end_or_origin, no_end, no_origin, two_nodes_dc]


@pytest.fixture
def singleton(same_node):
    return [same_node]


@pytest.fixture
def two_path(two_nodes_c):
    return [two_nodes_c]


@pytest.fixture
def many_path(many_nodes_3v1, many_nodes_3v2):
    return [many_nodes_3v1, many_nodes_3v2]


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
        assert len(testObj.givePath()) == 3
