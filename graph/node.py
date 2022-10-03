
from typing import Any


class Node:
    def __init__(self, id: str, extraInfo={}, degree=0) -> None:
        self.id=id
        self.degree=degree
        self.extraInfo=extraInfo
        
    def addInfo(self, infoType, value) -> None:
        self.extraInfo[infoType]=value
    
    def getInfo(self, infoType) -> Any:
        return self.extraInfo[infoType]

        
