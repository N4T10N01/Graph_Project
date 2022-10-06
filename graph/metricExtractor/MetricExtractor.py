try:
    import matplotlib.pyplot as plt
    from graph.undirectedGraph import UndirectedGraph
except ModuleNotFoundError:
    import sys
    sys.path.append('..')
    from graph.undirectedGraph import UndirectedGraph


class MetricExtractor:

    def __init__(self, graph: UndirectedGraph) -> None:
        self.graph = graph

    # returns number of nodes in the graph
    def get_num_nodes(self):
        return len(self.graph.allNodes())

    # returns number of edges in the graph
    def get_num_edges(self):
        return len(self.graph.allEdges())

    # determines average weight per edge
    def get_ave_weight(self, weightTypes):

        total_weight = 0

        for e in self.graph.allEdges():
            total_weight += e.calculateWeight(weightTypes)

        return (total_weight / len(self.graph.allEdges()))

    # determines average degree per node
    def get_ave_degree(self):

        total_degree = 0

        for n in self.graph.allNodes():
            total_degree += n.getDegree()

        return (total_degree / len(self.graph.allNodes()))

    # histogram - num of nodes per degree
    def degreeHistogram(self):

        node_degrees = {}

        for n in self.graph.allNodes():
            if node_degrees.get(n.getDegree(), -1) != -1:
                node_degrees[n.getDegree()] += 1
            else:
                node_degrees[n.getDegree()] = 1

        self.plotter(
            title='Node',
            x_name='Degree Values',
            y_name='Nodes',
            x_values=node_degrees.keys(),
            y_values=node_degrees.values(),
            type='bar')

    def longitudeVslatitude(self):
        latitude = []
        longitude = []
        for n in self.graph.allNodes():
            latitude.append(float(n.getInfo('latitude')))
            longitude.append(float(n.getInfo('longitude')))

        self.plotter(
            title='LongtitudeVsLatitude',
            x_name='latitude',
            y_name='longitude',
            x_values=latitude,
            y_values=longitude,
            type='scatter',
            more=True
        )

        for n in self.graph.allNodes():
            plt.annotate(n.ID(), (float(n.getInfo('latitude')),
                         float(n.getInfo('longitude'))))

        plt.show()

    @staticmethod
    def plotter(title: str, x_name: str, y_name: str, x_values: list,
                y_values: list, type: str, legend=False, more=False):
        if type == 'bar':
            plt.bar(x_values, y_values)
        elif type == 'line':
            plt.plot(x_values, y_values)
        elif type == 'scatter':
            plt.scatter(x_values, y_values, c='red')

        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(title)
        if legend:
            plt.legend()
        if not (more):
            plt.show()
            plt.figure()
