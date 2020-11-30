import numpy as np
import math
class State:
    def __init__(self, s, zero, prev=None):
        self.s=s
        self.prev=prev
        self.zero=zero
        self.hash=None

        #cummulative backward cost g:
        if self.prev:
            self.g = self.prev.g + 1
        else:
            self.g = 0

        self.f = self.g + self.tiles()
# change       self.f = self.g + self.heuristic       to get results with chosen heuristic.
# heuristic options: tiles, manhattan, euclide and heuro.
# tiles is the tiles heuristic.
# and heuro is our own heuristic measure.


    def __hash__(self):
        if self.hash:
            return self.hash
        s=0
        for i in range(8,-1,-1):
            s=10*s+self.s[i]
        self.hash=s
        return s

    #1,5,6
    #2,0,3
    #4,7,8

    #[1,5,6,2,0,3,4,7,8] zero=4
    def Successors(self):
        succ=[]
        s=self.s
        zero=self.zero
        if (zero-1)>=0 and ((zero-1)//3==zero//3):
            tmp=s.copy()
            tmp[zero-1],tmp[zero]=s[zero],s[zero-1]
            succ.append(State(tmp,zero-1,self))
        if (zero+1<9) and ((zero+1)//3==zero//3):
            tmp=s.copy()
            tmp[zero+1],tmp[zero]=s[zero],s[zero+1]
            succ.append(State(tmp,zero+1,self))
        if (zero-3)>=0:
            tmp=s.copy()
            tmp[zero-3],tmp[zero]=s[zero],s[zero-3]
            succ.append(State(tmp,zero-3,self))
        if (zero+3)<=8:
            tmp=s.copy()
            tmp[zero+3],tmp[zero]=s[zero],s[zero+3]
            succ.append(State(tmp,zero+3,self))

        return succ

    def tiles(self):
        tmp = np.array(self.s)
        test = tmp.reshape(3,3)
        goal = [[1,2,3],[4,5,6],[7,8,0]]

        h = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if test[i][j] == 0:
                    continue
                if (test[i][j] != goal[i][j]):
                    h += 1
        return h

    def manhattan(self):
        tmp = np.array(self.s)
        test = tmp.reshape(3,3)
        goal = [[1,2,3],[4,5,6],[7,8,0]]

        h = 0
        for i in range(0, 3):
            for j in range(0, 3):
                tile = test[i][j]
                if tile == 0:
                    continue
                for m in range(0, 3):
                    for n in range(0, 3):
                        if tile == goal[m][n]:
                            h += abs(i-m) + abs(j-n)
        return h

    def heuro(self):
        return self.manhattan() + self.tiles() ** 0.1


# we just tested the euclidean heuristic to compare results:
    def euclide(self):
        tmp = np.array(self.s)
        test = tmp.reshape(3,3)
        goal = [[1,2,3],[4,5,6],[7,8,0]]

        h = 0
        for i in range(0, 3):
            for j in range(0, 3):
                tile = test[i][j]
                if tile == 0:
                    continue
                for m in range(0, 3):
                    for n in range(0, 3):
                        if tile == goal[m][n]:
                            h += math.sqrt((i-m)*(i-m) + (j-n)*(j-n))
        return h
#Euclidean Heuristic Results:
#Moves: 21
#Visited states: 419
#Explored: 666

    def IsGoal(self):
        solution=[1,2,3,4,5,6,7,8,0]
        s=self.s
        for i in range(9):
            if s[i]!=solution[i]:
                return False
        return True

    def __lt__(self, other):
        if(self.f < other.f):
            return True
        else:
            return False

    def __eq__(self, other):
        for i in range(9):
            if self.s[i]!=other.s[i]:
                return False
        return True


    def __str__(self):

        tmp=np.array(self.s)
        return str(tmp.reshape(3,3))

def Solution(state):
    path=[]
    length=0
    while state:
        path.append(str(state))
        state=state.prev
        length=length+1
    return ('\n'.join(path), length)

def Astar():
    start=State([7,2,4,5,0,6,8,3,1],4)
    visited=set()
    solved=False
    import heapq
    q = []
    heapq.heapify(q)
    heapq.heappush(q,start)

    i=0
    while len(q) > 0:
        i=i+1
        current=heapq.heappop(q)
        if current.IsGoal():
            path, length= Solution(current)
            #print(path)
            #print("Moves: "+str(length))
            solved=True
            break
        if current in visited:
            continue
        visited.add(current)
        for tmp in current.Successors():
            heapq.heappush(q,tmp)


    if not solved:
        print("No Solution")

    #print("Visited states: "+str(len(visited)))
    #print("Explored: "+str(i))
