import queue
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
import collections

### Init
plt.style.use('dark_background')
path = []
###

### Make lists fincs
def makeAdjList(edges, amount_of_vertices):
    graph = [[] for _ in range(amount_of_vertices)]
    if ort:
        for k in range(1, amount_of_vertices + 1):
            for i in range(len(edges)):
                if edges[i][0] == k:
                    graph[k - 1].append(edges[i][1])
    else:
        for k in range(1, amount_of_vertices + 1):
            for i in range(len(edges)):
                if edges[i][0] == k:
                    graph[k - 1].append(edges[i][1])
                    graph[edges[i][1] - 1].append(edges[i][0])

    return graph
###

###
def dfs(graph, source):
    stack = []
    stack.append(source)
    
    while stack:
        s = stack.pop()
        if s not in path:
            path.append(s)

        elif s in path:
            continue
        for neighbour in graph[s - 1]:
            stack.append(neighbour)

def bfs(graph, source):
    queue = collections.deque()
    queue.append(source)
    
    while queue:
        s = queue.popleft()
        if s not in path:
            path.append(s)

        elif s in path:
            continue
        for neighbour in graph[s - 1]:
            queue.append(neighbour)
###

#'''
### Read stp and make useful data
def readStp(filename):
    with open(filename) as f:
        s = f.readlines()
        s = [line.rstrip() for line in s]

    graph = []
    elist = []
    ort = False
    start = 0
    while s[start].lower() != 'Section Graph'.lower():
        start+=1
    end = start + 1
    while s[end].lower() != 'End'.lower():
        end+=1


    for i in range(start + 1, end):
        graph.append(s[i].split(' '))

    nodes = int(graph[0][1])
    edges = int(graph[1][1])


    for i in range(2, len(graph)):
        if graph[i][0].lower() == 'A'.lower():
            ort = True

    for i in range(2, len(graph)):
        if ort:
            if(graph[i][0].lower() == 'A'.lower()):
                elist.append([int(graph[i][1]), int(graph[i][2]), int(graph[i][3])])
            else:
                elist.append([int(graph[i][1]), int(graph[i][2]), int(graph[i][3])])
                elist.append([int(graph[i][2]), int(graph[i][1]), int(graph[i][3])])
        else:
            elist.append([int(graph[i][1]), int(graph[i][2]), int(graph[i][3])])



    return elist, edges, ort, nodes
###
#'''

### simple1.stp is a tree
### simple.stp is not a tree
elist, edges, ort, nodes = readStp('simple1.stp')

'''
### Big tree
elist = []
nodes = 100
k = 2
ort = False
for i in range(1, nodes // 2):
    elist.append([i, k, 1])
    k+=1
    elist.append([i, k, 1])
    k+=1
print(elist)
###
'''

### choose bfs or dfs
dfs(makeAdjList(elist, nodes), 1)
#bfs(makeAdjList(elist, nodes), 1)
###

### Draw
G = nx.Graph()
G.add_weighted_edges_from(elist)

pos = nx.spring_layout(G, seed=30)

fig, ax = plt.subplots(figsize=(len(elist), 4))

def update(idx):
    ax.clear()
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color="b")
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color="r", nodelist=path[0:idx%len(path) + 1])


    nx.draw_networkx_edges(G, pos, width=2, edge_color="b", ax=ax)

    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", ax=ax)

    ax.set_title(f'Frame {idx}')

ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(path), interval=500, repeat=True)
plt.show()
###