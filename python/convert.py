import graph

class table():
    def __init__(this, load : list = []):
        this.graph = graph.graph()
        for item in load:
            this.load(item)
    
    def load(this, name : str) -> None:
        with open(name) as file:
            for fact in file:
                fact = fact.split()
                if(len(fact) != 5):
                    raise Exception("Invalid Factor [" + ' '.join(fact) + "]")
                if(not this.graph.hasNode(fact[1])):
                    this.graph.addNode(fact[1])
                if(not this.graph.hasNode(fact[4])):
                    this.graph.addNode(fact[4])
                this.graph.setEdgeRatio(fact[1], fact[4], float(fact[0]), float(fact[3]))
    
    def __str__(this) -> str:
        return str(this.graph)
    
    def convert(this, amount : float, A : str, B : str, trim = 5, work : bool = False) -> float:
        if(A.find("/") != -1 and B.find("/") != -1):
            return this.complexConvert(amount, A, B, trim = trim, work = work)
        path = this.graph.findPath(A, B)
        for i in range(len(path) - 1):
            amount *= this.graph.getEdge(path[i], path[i + 1])
        if(trim):
            amount = round(amount, trim)
        if(work):
            steps = [this.graph.names[i] for i in path]
            return (amount, steps)
        else:
            return amount

    def __convert_inverse__(this, amount : float, A : str, B : str, trim = 5, work : bool = False) -> float:
        path = this.graph.findPath(A, B)
        for i in range(len(path) - 1):
            amount /= this.graph.getEdge(path[i], path[i + 1])
        if(trim):
            amount = round(amount, trim)
        if(work):
            steps = [this.graph.names[i] for i in path]
            return (amount, steps)
        else:
            return amount
    
    def complexConvert(this, amount : float, A : str, B : str, trim = 5, work : bool = False):
        A = A.split("/")
        B = B.split("/")
        amount, workA = this.convert(amount, A[0], B[0], trim = False, work = True)
        amount, workB = this.__convert_inverse__(amount, A[1], B[1], trim = False, work = True)
        if(trim):
            amount = round(amount, trim)
        if(work):
            return (amount, [workA, workB])
        return amount
