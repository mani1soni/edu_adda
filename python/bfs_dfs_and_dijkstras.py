class gnode:
    

    '''
    This is a class representing the node of a graph

    Attributes:
    
    1. val: The value of the node object
    2. visited: Boolean indicating whether the node is visited or not, for
       the graph searching algorithms
    3. neighbours: The list of nodes connected to this node object (All are objects of class gnode)

    Functions:

    1. __init__ : Initializes node object
    2. __repr__ : Returns a string with information about the node and it's neighbours when print(obj) is called (obj is a gnode object) 
    
    '''

    def __init__(self,info,n=None):
        self.val = info
        self.visited = False
        self.neighbours = []
        if n == None:
            pass
        else:
            for i in range(n):
                self.neighbours.append(None)
    
    def __repr__(self):
        s = str(self.neighbours) if len(self.neighbours)>0 else 'None'
        return 'Node: {} , Neighbours: {}'.format(self.val,s)

'''
Iterative BFS

In this implementation of BFS, a queue is used to push the nodes while searching.
'''
def BFS(start):
	q = list()
	q.append(start)
	while(len(q)!=0):
		x = q[0]
		q.pop(0)
		if not x == None:
			print(x.val)
			if not x.visited:
				for i in x.neighbours:
					q.append(i)
			x.visited = True

'''
Iterative DFS

In this implementation of DFS, a stack is used to push the nodes while searching.
'''
def DFS(start):
	q = list()
	q.append(start)
	while(len(q)!=0):
		x = q[-1]
		q.pop(-1)
		if not x == None:
			print(x.val)
			if not x.visited:
				for i in x.neighbours:
					q.append(i)
			x.visited = True

#Recursive DFS
def DFSr(start):
	if not start == None:
		print(start)
	for i in start.neighbours:
		if not i == None:
			DFSr(i)

'''

Dijkstra's Algorithm Implementation

Algorithm to find the shortest path between the source and all the other nodes.

Here an adjacency matrix represents the connections between different nodes. The matrix is nxn in size
and each cell (i,j) holds a value, which is the distance between the nodes indexed as i and j.

The distances array represents the distance between the source node and the ith node. The source node is 
initially set to 0, and all the other to infinity.

The paths array represents the shortest path from the source to the ith node. 

No nodes of the class gnode are actually passed to the algorithm.

'''


def dijkstras_shortest_path():

	# Variable source is implemented
	n = int(input('Enter no. of nodes: '))
	nodes = []
	for i in range(n):
		nodes.append([None]*n)

	e = int(input('Enter no. of edges: '))
	for i in range(e):
		u , v , l = [int(i) for i in input().split()]
		nodes[u][v] = l

	distances = [float('inf')]*(n)
	
	start = int(input('Enter start location: '))
	distances[start] = 0

	paths = [[i] for i in range(n)]

	for i in range(n):
		for j in range(n):
			if not i == j:
				if not nodes[i][j] == None:
					if distances[j] > distances[i] + nodes[i][j]:
						distances[j] = distances[i] + nodes[i][j]
						paths[j] = [j]+paths[i]

	print(paths)
	print(distances)