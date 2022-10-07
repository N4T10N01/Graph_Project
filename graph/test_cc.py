try:
    import pytest
    from graph.graphBuilder.graphUpdater import TubeMapUpdater
    from graph.itinerary.componentConnector import DiComponentConnector
    from graph.undirectedGraph import TubeMap
except ModuleNotFoundError:
    import sys
    sys.path.append('..\\l1-graph-lab')
    from graph.graphBuilder.graphUpdater import TubeMapUpdater
    from graph.itinerary.componentConnector import DiComponentConnector
    from graph.undirectedGraph import TubeMap


@pytest.fixture
def getAlgorithm():
    generatedDict = {'nodePath': '_dataset\\london.stations.csv',
                 'edgePath': '_dataset\\london.connections.csv',
                 'nodeID': 'id', 'edgeNodeLabel1': 'station1',
                 'edgeNodeLabel2': 'station2',
                 'weightLabel': ['time'], 
                 'uniqueValues': ['line'],
                 'additionalPaths':
                 {'line': '_dataset\\london.lines.csv'}}

    g = TubeMap({}, {}, {}, {})
    u = TubeMapUpdater(g, generatedDict)
    u.update()
    return DiComponentConnector(g, 'zone')


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
def two_nodes_diffcomp() -> list:
    return ['84', '136', [['time']]]


@pytest.fixture
def two_nodes_samecomp() -> list:
    return ['140', '237', [['time']]]


@pytest.fixture
def many_nodes() -> list:
    return ['117', '121', [['time']]]


@pytest.fixture
def no_path(no_end_or_origin, no_end, no_origin, same_node,
            two_nodes_samecomp):
    return [no_end_or_origin, no_end, no_origin, same_node,
            two_nodes_samecomp]


@pytest.fixture
def two_path(two_nodes_diffcomp):
    return [two_nodes_diffcomp]


@pytest.fixture
def many_path(many_nodes):
    return [many_nodes]


def test_all_cases(no_path,
                two_path,
                many_path,
                getAlgorithm):

    testObj = getAlgorithm
    for case in no_path:
        testObj.generatePath(*case)
        assert testObj.givePath() == None

    for case in two_path:
        testObj.generatePath(*case)
        assert [case[1], 'island1'] in testObj.givePath()

    for case in many_path:
        testObj.generatePath(*case)
        assert min([len(path) for path in testObj.givePath()]) >= 2
