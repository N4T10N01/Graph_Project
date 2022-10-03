import matplotlib.pyplot as plt

from UndirectedGraph import UndirectedGraph

class MetricExtractor:

    def __init__(self, graph : UndirectedGraph) -> None:
        self.graph = graph

    #returns number of nodes in the graph
    def get_num_node(self):
        return len(self.graph.nodeList)

    #returns number of edges in the graph
    def get_num_edges(self):
        return len(self.graph.edgeList)

    #determines average weight per edge
    def get_ave_weight(self):

        total_weight = 0

        for e, v in self.graph.edgeList.items():
            total_weight += self.graph.edgeList[v].calculateWeight(weightTypes)
            
        return (total_weight/len(self.graph.edgeList))

    #determines average degree per node
    def get_ave_degree(self):
        
        total_degree = 0

        for e, v in self.graph.nodeList.items():
            total_degree += self.graph.nodeList[v].degree
            
        return (total_degree / len(self.graph.nodeList))


    #histogram - num of nodes per degree
    def histogram(self):

        node_degrees = []

        for i in len(self.graph.nodeList.items()):
            node_degrees.append(self.graph.nodeList[v].degree)

        plt.hist(node_degrees)
        plt.show() 

        return None



    
