class Edge:

    def __init__(self, node1: str, node2: str, weights={},
                 extraInfo={}, uniqueValues=[]) -> None:
        self.id = node1 + node2
        self.node1 = node1
        self.node2 = node2
        self.weights = weights
        self.extraInfo = extraInfo
        self.uniqueValues = uniqueValues

    def other(self, n: str) -> str:
        if n == self.node1:
            return self.node2
        else:
            return self.node1

    def ID(self):
        return self.id

    def addInfo(self, infoType, value) -> None:
        self.extraInfo[infoType] = value

    def getInfo(self, infoType) -> any:
        return self.extraInfo.get(infoType, None)

    def changeWeight(self, newWeights):
        self.weights.update(newWeights)

    def updateID(self):
        self.id = self.node1 + self.node2
        for uniqueValue in self.uniqueValues:
            # list should be a small amount, some constant under
            # 100, therefore, low, or empty
            self.id += self.extraInfo[uniqueValue]

    def calculateWeight(self, weightTypes=None, dynamicArgs=[]):
        if not weightTypes:
            weights = [self.weights[weightType](*dynamicArgs)
                       for weightType in self.weights.keys()]
            return sum(weights)
        else:
            weights = [self.weights[weightType](*dynamicArgs)
                       for weightType in weightTypes]
            return sum(weights)
