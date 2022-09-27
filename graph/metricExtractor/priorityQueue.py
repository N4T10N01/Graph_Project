import sys

sys.path.append('C:\\Users\\Dingleberry\\Documents\\3XB3\\l1-graph-lab')


from graph.node import Node


class NodePriorityQueue:

    def __init__(self, size: int) -> None:
        self.pq=[None]*(size+1)
        self.N=0
        self.nodePlacements={}
    
    def isEmpty(self)->bool:
        return self.N==0
    
    def insert(self, n: Node, dist: list)->None:
        self.N+=1
        self.nodePlacements[n.id]=self.N
        self.pq[self.N]=[n, dist]
        self._swim(self.N)
    
    def delMin(self) -> list:
        min=self.pq[1]
        self._exch(1, self.N)
        self.N-=1
        self._sink(1)
        self.nodePlacements[min[0].id]=-1
        return min[0]

    def _less(self ,weightList1: list, weightList2: list) -> bool:

        for i in range(len(weightList1)):
            if (weightList1[i]>weightList2[i]):
                return False
            elif(weightList1[i]<weightList2[i]):
                return True

        return False
    
    def _exch(self, i: int, j: int) -> None:
        self.nodePlacements[self.pq[i][0].id]=j
        self.nodePlacements[self.pq[j][0].id]=i
        self.pq[i], self.pq[j]=self.pq[j], self.pq[i]
    
    
    def _swim(self, k: int) ->None:
        while (k>1 and self._less(self.pq[k][1],self.pq[int(k/2)][1])):
            self._exch(int(k/2),k)
        
            k=int(k/2)
    
    def _sink(self, k: int) ->None:
        while (2*k <= self.N):
            j=2*k
            if (j<self.N and self._less(self.pq[j+1][1], self.pq[j][1])):
                j+=1
            if(self._less(self.pq[k][1],self.pq[j][1])):
                break
            self._exch(k,j)
            
            k=j
     
    def change(self, n, weights):
        self.pq[self.nodePlacements[n.id]][1]=weights
        self._swim(self.nodePlacements[n.id])
        self._sink(self.nodePlacements[n.id])

    def contains(self, n:Node):
        return True if self.nodePlacements.get(n.id, -1)!=-1 else False
        

            
# q=NodePriorityQueue(20)

# q.insert(Node('a'), [20])
# print(q.nodePlacements)
# q.insert(Node('b'), [25])
# print(q.nodePlacements)
# q.insert(Node('c'), [22])
# print(q.nodePlacements)
# q.insert(Node('d'), [-3])
# print(q.nodePlacements)
# q.insert(Node('e'), [0])
# print(q.nodePlacements)
# q.insert(Node('f'), [17])
# print(q.nodePlacements)
# q.insert(Node('g'), [12])
# print(q.nodePlacements)
# q.insert(Node('h'), [-50])
# print(q.nodePlacements)
# q.insert(Node('i'), [15])
# print(q.nodePlacements)
# q.insert(Node('j'), [24])
# print(q.nodePlacements)
# q.insert(Node('k'), [100])
# print(q.nodePlacements)
# q.insert(Node('l'), [3])
# print(q.nodePlacements)

# print(q.pq)



# q.delMin()

# q.change(Node('d'), [500])

# print(q.delMin())

# print(q.contains(Node('e')))



