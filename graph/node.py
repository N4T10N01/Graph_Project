class Node:
    def __init__(self, id: str, extraInfo={}, degree=0) -> None:
        self.id = id
        self.degree = degree
        self.extraInfo = extraInfo

    def ID(self):
        return self.id

    def getDegree(self) -> int:
        return self.degree

    def addToDegree(self, value: int) -> None:
        self.degree += value

    def addInfo(self, infoType, value) -> None:
        self.extraInfo[infoType] = value

    def getInfo(self, infoType) -> any:
        return self.extraInfo[infoType]
