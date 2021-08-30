def pad(text : str, length : int, character : chr = ' ') -> str:
    return text + (character * max(0, (length - len(text))))

class grid():
    def __init__(this, size : int = 0, init : any = None):
        this.matrix = [[init for i in range(size)] for j in range(size)]
        this.init = init
    
    def display(this) -> None:
        for row in this.matrix:
            print(row)
    
    def inc(this) -> None:
        this.matrix.append([this.init for i in range(len(this.matrix))])
        for arr in this.matrix:
            arr.append(this.init)
    
    def setValue(this, A : int, B : int, value : any) -> None:
        if(A >= len(this.matrix) or B >= len(this.matrix)):
            raise Exception("Edge out of bounds [" + A + ", " + B + "]")
        this.matrix[A][B] = value
    
    def __getitem__(this, key : int) -> list:
        if(key >= len(this.matrix)):
            raise Exception("Index [" + key + "] out of bounds")
        return this.matrix[key]

class graph():
    def __init__(this, blank : any = -1):
        this.names = []
        this.grid = grid(init = blank)
        this.blank = blank
    
    def __str__(this):
        ret = ""
        maxLen = 0
        for i in this.names:
            maxLen = max(maxLen, len(i))
        maxLen += 1
        for i in range(len(this.names)):
            ret += pad(this.names[i], maxLen) + str(this.grid[i]) + "\n"
        return ret
    
    def addNode(this, name : str):
        this.names.append(name)
        this.grid.inc()
    
    def value(this, name : str) -> int:
        for i in range(len(this.names)):
            if(this.names[i] == name):
                return i
        raise Exception("Node [" + name + "] does not exist")
    
    def getName(this, index : int) -> str:
        if(index <= len(this.names)):
            raise Exception("Index [" + index + "] out of range")
        return this.names[index]
    
    def setEdge(this, A : str, B : str, value : any) -> None:
        x = this.value(A)
        y = this.value(B)
        this.grid[x][y] = value
    
    def setEdgeRatio(this, A : str, B : str, Av : any, Bv : any) -> None:
        x = this.value(A)
        y = this.value(B)
        this.grid[x][y] = Bv / Av
        this.grid[y][x] = Av / Bv
    
    def getEdge(this, A, B) -> any:
        if(type(A) is str):
            A = this.value(A)
        if(type(B) is str):
            B = this.value(B)
        return this.grid[A][B]
    
    def getConnected(this, node) -> list:
        if(type(node) is str):
            node = this.value(node)
        ret = []
        i = 0
        for val in this.grid[node]:
            if(val != this.blank):
                ret.append(i)
            i += 1
        return ret
    
    def __path_find__(this, nodes : list, name : int) -> int:
        size = len(nodes)
        if(name >= size):
            raise Exception("Node id [" + name + "] is impossible")
        for i in range(size):
            if(nodes[i][1] == name):
                return i
    
    def findPath(this, A : str, B : str) -> list:
        x = this.value(A)
        y = this.value(B)
        
        nodes = [[float("inf"), i, [], False] for i in range(len(this.grid.matrix))]
        nodes[x][0] = 0
        
        while True:
            nodes.sort()
            for node in nodes:
                if(not node[3]):
                    current = node
                    break
            else:
                raise Exception("No Path Between [" + A + "] [" + B + "] exists")
            
            for item in this.getConnected(current[1]):
                dist = current[0] + 1
                loc = this.__path_find__(nodes, item)
                node = nodes[loc]
                if(dist < node[0]):
                    node[0] = dist
                    node[2] = current[2] + [current[1]]
            
            current[3] = True
            end = this.__path_find__(nodes, y)
            if(nodes[end][0] != float("inf")):
                return nodes[end][2] + [nodes[end][1]]
    
    def hasNode(this, name):
        for item in this.names:
            if(name == item):
                return True
        return False

