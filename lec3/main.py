import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

### Init
plt.style.use('dark_background')

###

### Make lists fincs
def makeAdjList(edges, amount_of_vertices):
    graph = [[] for _ in range(amount_of_vertices)]
    if ort:
        for k in range(1, amount_of_vertices + 1):
            for i in range(len(edges)):
                if edges[i][0] == k:
                    graph[k - 1].append([edges[i][1], edges[i][2]])
    else:
        for k in range(1, amount_of_vertices + 1):
            for i in range(len(edges)):
                if edges[i][0] == k:
                    graph[k - 1].append([edges[i][1], edges[i][2]])
                    graph[edges[i][1] - 1].append([edges[i][0], edges[i][2]])

    return graph

def makeIncList(edges, amount_of_vertices):
    graph = [[] for _ in range(amount_of_vertices)]
    if ort:
        for k in range(1, amount_of_vertices + 1):
            graph.append([])
            for i in range(len(edges)):
                if edges[i][0] == k:
                    graph[k - 1].append([(edges[i][0], edges[i][1]), edges[i][2]])
    else:
        for k in range(1, amount_of_vertices + 1):
            graph.append([])
            for i in range(len(edges)):
                if edges[i][0] == k:
                    graph[k - 1].append([(edges[i][0], edges[i][1]), edges[i][2]])
                    graph[edges[i][1] - 1].append([(edges[i][1], edges[i][0]), edges[i][2]])

    return graph
###

#'''
### Read stp and make useful data
#use b13.stp or es30fst.stp to check non-orts
#use simple.stp or custom.stp to check orts
def readStp(filename):
    with open(filename) as f:
        s = f.readlines()
        s = [line.rstrip() for line in s]

    graph = []
    elist = []
    start = 0
    while s[start].lower() != 'Section Graph'.lower():
        start+=1
    end = start + 1
    while s[end].lower() != 'End'.lower():
        end+=1


    for i in range(start + 1, end):
        graph.append(s[i].split(' '))

    nodes = int(graph[0][1])

    if(graph[1][0].lower() == 'Arcs'.lower()):
        ort = True
        edges = int(graph[1][1])
    else:
        ort = False
        edges = int(graph[1][1])

    for i in range(2, len(graph)):
        elist.append([int(graph[i][1]), int(graph[i][2]), int(graph[i][3])])

    return elist, edges, ort, nodes
###
#'''

elist, edges, ort, nodes = readStp('simple.stp')

#'''
### Draw
if ort:
    G = nx.DiGraph(directed=True)
    G.add_weighted_edges_from(elist)

    labels = nx.get_edge_attributes(G, 'weight')

    pos = nx.spring_layout(G, seed=23)

    fig, ax = plt.subplots(figsize=(len(elist), 4))

    def update(idx):
        ax.clear()
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color="b")
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color="r", nodelist=[idx % 11 + 1])

        nx.draw_networkx_edges(
            G, pos, edgelist=[elist[idx]], width=5, alpha=0.5, edge_color="r", style="dashed", ax=ax
        )

        nx.draw_networkx_edges(
            G, pos, edgelist=elist[:idx] + elist[idx + 1:], width=2, edge_color="b", ax=ax
        )

        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", ax=ax)

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax, label_pos=0.3)

        ax.set_title(f'Frame {idx}')

    ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(elist) - 1, interval=500, repeat=True)
    plt.show()
else:
    G = nx.Graph()
    G.add_weighted_edges_from(elist)

    labels = nx.get_edge_attributes(G, 'weight')

    pos = nx.spring_layout(G, seed=30)

    fig, ax = plt.subplots(figsize=(len(elist), 4))

    def update(idx):
        ax.clear()
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color="b")
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color="r", nodelist=[idx % 11 + 1])

        nx.draw_networkx_edges(
            G, pos, edgelist=[elist[idx]], width=5, alpha=0.5, edge_color="r", style="dashed", ax=ax
        )

        nx.draw_networkx_edges(
            G, pos, edgelist=elist[:idx] + elist[idx + 1:], width=3, edge_color="b", ax=ax
        )

        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", ax=ax)

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax)

        ax.set_title(f'Frame {idx}')

    ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(elist) - 1, interval=500, repeat=True)
    plt.show()
###
#'''

#'''
### Make and print lists
adjList = makeAdjList(elist, nodes)
incList = makeIncList(elist, nodes)

for i in range(nodes):
    print(f'{i+1} -> {adjList[i]}')

print()

for i in range(nodes):
    print(f'{i+1} -> {incList[i]}')
###
#'''