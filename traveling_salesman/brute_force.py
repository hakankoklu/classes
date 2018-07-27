import networkx as nx
from itertools import permutations, chain, combinations
import matplotlib.pyplot as plot
import pulp


def plot_cycle(coordinates, cycle):
    # Compute the x and y coordinates in the order according to the cycle
    x_coordinates = [coordinates[i][0] for i in cycle]
    y_coordinates = [coordinates[i][1] for i in cycle]

    # Add the first vertex of the cycle (to close the cycle)
    x_coordinates.append(coordinates[cycle[0]][0])
    y_coordinates.append(coordinates[cycle[0]][1])

    plot.plot(x_coordinates, y_coordinates, 'xb-', )
    plot.show()


def get_cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    result = 0
    for i in range(len(cycle) - 1):
        result += g[cycle[i]][cycle[i+1]]['weight']
    result += g[cycle[-1]][cycle[0]]['weight']
    return result


def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))

    return sum_of_weights*2/(n-1)


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Iterate through all permutations of n vertices
    #for p in permutations(range(n)):
    weight = float("inf")
    for perm in permutations(g.nodes(), n):
        cycle = get_cycle_length(g, perm)
        weight = min(cycle, weight)
    return weight


def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():
            if v != current_node and v not in path and g[current_node][v]['weight'] < min_edge:
                min_edge = g[current_node][v]['weight']
                next_node = v

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight


def lower_bound(g, sub_cycle):
    # The weight of the current path.
    current_weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])

    # For convenience we create a new graph which only contains vertices not used by g.
    unused = [v for v in g.nodes() if v not in sub_cycle]
    h = g.subgraph(unused)

    # Compute the weight of a minimum spanning tree.
    t = list(nx.minimum_spanning_edges(h))
    mst_weight = sum([h.get_edge_data(e[0], e[1])['weight'] for e in t])

    # If the current sub_cycle is "trivial" (i.e., it contains no vertices or all vertices), then our lower bound is
    # just the sum of the weight of a minimum spanning tree and the current weight.
    if len(sub_cycle) == 0 or len(sub_cycle) == g.number_of_nodes():
        return mst_weight + current_weight

    # If the current sub_cycle is not trivial, then we can also add the weight of two edges connecting the vertices
    # from sub_cycle and the remaining part of the graph.
    # s is the first vertex of the sub_cycle
    s = sub_cycle[0]
    # t is the last vertex of the sub_cycle
    t = sub_cycle[-1]
    # The minimum weight of an edge connecting a vertex from outside of sub_sycle to s.
    min_to_s_weight = min([g[v][s]['weight'] for v in g.nodes() if v not in sub_cycle])
    # The minimum weight of an edge connecting the vertex t to a vertex from outside of sub_cycle.
    min_from_t_weight = min([g[t][v]['weight'] for v in g.nodes() if v not in sub_cycle])

    # Any cycle which starts with sub_cycle must be of length:
    # the weight of the edges from sub_cycle +
    # the minimum weight of an edge connecting sub_cycle and the remaining vertices +
    # the minimum weight of a spanning tree on the remaining vertices +
    # the minimum weight of an edge connecting the remaining vertices to sub_cycle.
    return current_weight + min_from_t_weight + mst_weight + min_to_s_weight


# The branch and bound procedure takes
# 1. a graph g;
# 2. the current sub_cycle, i.e. several first vertices of cycle under consideration.
# Initially sub_cycle is empty;
# 3. currently best solution current_min, so that we don't even consider paths of greater weight.
# Initially the min weight is infinite
def branch_and_bound(g, sub_cycle=None, current_min=float("inf")):
    # If the current path is empty, then we can safely assume that it starts with the vertex 0.
    if sub_cycle is None:
        sub_cycle = [0]

    # If we already have all vertices in the cycle, then we just compute the weight of this cycle and return it.
    if len(sub_cycle) == g.number_of_nodes():
        weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
        weight = weight + g[sub_cycle[-1]][sub_cycle[0]]['weight']
        return weight

    # Now we look at all nodes which aren't yet used in sub_cycle.
    unused_nodes = list()
    for v in g.nodes():
        if v not in sub_cycle:
            unused_nodes.append((g[sub_cycle[-1]][v]['weight'], v))

    # We sort them by the distance from the "current node" -- the last node in sub_cycle.
    unused_nodes = sorted(unused_nodes)

    for (d, v) in unused_nodes:
        assert v not in sub_cycle
        extended_subcycle = list(sub_cycle)
        extended_subcycle.append(v)
        # For each unused vertex, we check if there is any chance to find a shorter cycle if we add it now.
        if lower_bound(g, extended_subcycle) < current_min:
            current_min = branch_and_bound(g, extended_subcycle, current_min)
            # WRITE YOUR CODE HERE
            # If there is such a chance, we add the vertex to the current cycle, and proceed recursively.
            # If we found a short cycle, then we update the current_min value.

    # The procedure returns the shortest cycle length.
    return current_min


# The function should return a 2-approximation of an optimal Hamiltonian cycle.

def approximation(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # You might want to use the function "nx.minimum_spanning_tree(g)"
    # which returns a Minimum Spanning Tree of the graph g
    mst = nx.minimum_spanning_tree(g)
    cycle = [0]
    while len(cycle) < n:
        added = False
        go_back = 0
        while not added:
            for node in list(mst[cycle[len(cycle) - 1 - go_back]]):
                if node not in cycle:
                    cycle.append(node)
                    added = True
                    break
            go_back += 1

    weight = sum(g[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1))
    weight += g[cycle[-1]][cycle[0]]['weight']

    # You also might want to use the command "list(nx.dfs_preorder_nodes(graph, 0))"
    # which gives a list of vertices of the given graph in depth-first preorder.

    return weight


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_graph(coordinates):
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight=dist(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))
    return g


def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    # Write your code here.
    return sum(g[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1)) + g[cycle[0]][cycle[-1]]['weight']

g = nx.Graph()
g.add_edge(0, 1, weight=2)
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=2)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=1)
g.add_edge(1, 3, weight=1)

print(all_permutations(g))


coordinates = [
    (231, 72),
    (68, 9),
    (11, 90),
    (237, 116),
    (168, 112),
    (141, 69),
    (17, 18)
    ]

coordinates = [(181, 243), (101, 143), (100, 216), (167, 15), (37, 201), (163, 226), (2, 42), (35, 73), (85, 116), (142, 235), (200, 18)]
optimal_cycle = [0, 5, 9, 2, 4, 1, 8, 7, 6, 3, 10]

coordinates = [(145, 176), (185, 244), (67, 192), (5, 137), (165, 154), (106, 286), (132, 173), (285, 143), (164, 115), (41, 181), (27, 137), (242, 190), (56, 208), (126, 240), (269, 221), (166, 43), (98, 296), (290, 194), (146, 67), (27, 138), (68, 283), (110, 42), (252, 41), (7, 219), (262, 205), (136, 251), (184, 240), (251, 29), (50, 148), (185, 299), (172, 106), (164, 198), (28, 88), (4, 236), (75, 42), (259, 158), (21, 38), (298, 277), (46, 97), (71, 1), (210, 173), (71, 296), (74, 227), (230, 136), (148, 278), (197, 257), (226, 29), (154, 258), (102, 162), (197, 274), (74, 12), (87, 102), (276, 65), (14, 60), (81, 184), (129, 49), (45, 68), (119, 61), (201, 45), (35, 14), (134, 173), (199, 218), (269, 233), (53, 78), (171, 167), (267, 123), (291, 245), (252, 202), (101, 262), (54, 250), (219, 300), (209, 7), (125, 230), (25, 90), (0, 144), (98, 7), (254, 94), (111, 78), (48, 175), (35, 207), (208, 192), (132, 37), (236, 97), (240, 211), (298, 265), (160, 153), (235, 279), (29, 53), (251, 213), (17, 169), (62, 11), (75, 20), (4, 115), (92, 4), (227, 61), (290, 41), (66, 15), (68, 224), (69, 265), (195, 88), (194, 129), (73, 129), (143, 119), (219, 28), (170, 260), (199, 51), (31, 300), (64, 138), (2, 100), (166, 13), (268, 131), (176, 131), (125, 283), (145, 41), (90, 208), (251, 136), (220, 142), (277, 278), (130, 228), (169, 263), (190, 207), (44, 15), (295, 162), (259, 209), (39, 2), (218, 129), (41, 203), (48, 12), (161, 20), (154, 263), (233, 205), (116, 190), (272, 289), (234, 109), (31, 100), (208, 61), (128, 25), (103, 205), (101, 159), (274, 255), (169, 22), (2, 202), (292, 240), (276, 133), (283, 94), (226, 31), (75, 247), (180, 88), (8, 215), (82, 156), (214, 231), (220, 4), (72, 136), (109, 37), (91, 158), (169, 10), (187, 184), (13, 70), (165, 133), (210, 93), (142, 212), (103, 234), (9, 286), (211, 283), (249, 264), (25, 187), (95, 146), (265, 126), (220, 191), (9, 125), (89, 148), (286, 156), (146, 273), (262, 23), (148, 281), (102, 300), (99, 297), (295, 178), (295, 83), (4, 228), (289, 141), (9, 42), (285, 241), (73, 108), (85, 73), (209, 150), (58, 158), (72, 65), (213, 108), (40, 72), (193, 201), (169, 98), (246, 125), (44, 180), (201, 145), (33, 42), (243, 91), (80, 93), (139, 240), (145, 101), (150, 162), (11, 229), (66, 280), (97, 84), (283, 58), (199, 14), (97, 200), (280, 231), (47, 249), (188, 89), (91, 55), (191, 94), (235, 153), (219, 72), (236, 286), (142, 132), (44, 71), (258, 236), (138, 62), (98, 154), (266, 194), (235, 165), (28, 157), (56, 155), (75, 115), (161, 67), (292, 28), (252, 249), (124, 9), (131, 14), (104, 225), (121, 80), (155, 171), (225, 71), (113, 262), (154, 47), (37, 76), (64, 97), (29, 287), (259, 279), (268, 235), (125, 88), (11, 58), (183, 171), (254, 167), (26, 63), (73, 271), (35, 265), (62, 110), (235, 104), (136, 152), (157, 69), (280, 157), (108, 58), (42, 9), (4, 92), (28, 183), (214, 75), (213, 2), (16, 27), (36, 149), (93, 210), (228, 209), (120, 273), (229, 18), (66, 164), (12, 220), (26, 14), (194, 164), (212, 167), (251, 282), (31, 268), (221, 66), (31, 102), (27, 91), (137, 85), (300, 178), (50, 225), (55, 95), (9, 157), (77, 291), (90, 268), (67, 169), (276, 5), (189, 102), (227, 263), (246, 99), (195, 189), (64, 77), (118, 211), (274, 130), (34, 117), (188, 23), (291, 252), (163, 295), (65, 113), (167, 278), (162, 286), (135, 77), (81, 27)]
optimal_cycle = [0, 60, 6, 250, 215, 102, 199, 275, 298, 241, 231, 77, 203, 184, 187, 288, 63, 56, 216, 189, 236, 32, 73, 274, 134, 273, 291, 38, 278, 237, 197, 51, 183, 248, 295, 224, 101, 152, 107, 149, 154, 170, 166, 219, 138, 48, 54, 2, 12, 126, 79, 277, 97, 42, 146, 281, 68, 234, 263, 112, 5, 175, 176, 16, 280, 41, 20, 202, 246, 98, 69, 208, 247, 271, 238, 106, 162, 33, 179, 201, 266, 23, 148, 141, 165, 256, 9, 193, 78, 282, 265, 186, 223, 28, 260, 19, 10, 222, 89, 279, 74, 3, 169, 92, 108, 255, 157, 242, 53, 245, 87, 195, 36, 181, 259, 267, 59, 124, 254, 121, 127, 90, 96, 39, 50, 91, 299, 34, 210, 253, 57, 21, 153, 93, 75, 228, 229, 136, 81, 55, 218, 18, 251, 225, 235, 113, 15, 140, 128, 109, 155, 292, 205, 71, 258, 151, 264, 46, 145, 103, 58, 105, 135, 257, 213, 233, 272, 94, 22, 27, 173, 283, 226, 95, 204, 52, 178, 144, 76, 286, 196, 82, 249, 133, 188, 159, 99, 211, 284, 209, 147, 191, 30, 8, 158, 111, 100, 194, 185, 116, 125, 43, 212, 221, 244, 35, 115, 192, 65, 167, 110, 290, 143, 180, 7, 252, 171, 122, 276, 177, 17, 220, 24, 123, 14, 207, 62, 240, 217, 227, 139, 182, 142, 66, 293, 84, 37, 117, 132, 239, 270, 164, 285, 86, 214, 70, 163, 49, 45, 1, 26, 104, 119, 296, 29, 294, 297, 174, 44, 172, 129, 47, 25, 198, 13, 118, 72, 161, 230, 261, 114, 206, 137, 131, 289, 160, 31, 156, 287, 190, 120, 61, 150, 262, 130, 83, 88, 67, 11, 168, 80, 40, 269, 268, 243, 64, 4, 85, 200, 232]


# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return an optimal weight of a Hamiltonian cycle.

# This function returns all the subsets of the given set s in the increasing order of their sizes.
def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# This function finds an optimal Hamiltonian cycle using the dynamic programming approach.
def dynamic_programming(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # The variable power now contains a tuple for each subset of the set {1, ..., n-1}.
    power = powerset(range(1, n))
    # The variable T is a dictionary, where the element T[s, i] for a set s and an integer i
    # equals the shortest path going through each vertex from s exactly once,
    # and ending at the vertex i.
    # Note that i must be in s.
    # Also, we will always assume that we start our cycle from the vertex number 0.
    # Thus, for convenience, we will always exclude the element 0 from the set s.
    T = {}
    # For every non-zero vertex i, we say that T[ tuple with the element i only, i]
    # equals the weight of the edge from 0 to i.
    # Indeed, by the definition of T, this element must be equal to the weight of
    # the shortest path which goes through the vertices 0 and i and ends at the vertex i.
    for i in range(1, n):
        # Syntactic note: In Python, we define a tuple of length 1 that contains the element i as (i,) *with comma*.
        T[(i,), i] = g[0][i]['weight']

    # For every subset s of [1,...,n-1]
    for s in power:
        # We have already initialized the elements of T indexed by sets of size 1, so we skip them.
        if len(s) > 1:
            # For every vertex i from s which we consider as the ending vertex of a path going through vertices from s.
            for i in s:
                # Define the tuple which contains all elements from s without *the last vertex* i.
                t = tuple([x for x in s if x != i])
                # Now we compute the optimal value of a cycle which visits all vertices from s and ends at the vertex i.

                # WRITE YOUR CODE HERE

    # Return the weight of on optimal cycle - this is the minimum of the following sum:
    # weight of a path + the last edge to the vertex 0.
    return min(T[tuple(range(1, n)), i] + g[i][0]['weight'] for i in range(1, n))


# This function finds an optimal Hamiltonian path using an Integer Linear Programing solver.

def ilp(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Define a new Integer Linear Program.
    m = pulp.LpProblem('TSP', pulp.LpMinimize)

    # Define variables x_i_j for 1 <= i,j <= n corresponding to the directed edges from i to j.
    # Each variable is of the Binary type (i.e., it can take on either 0 or 1).
    # An edge (i,j) will be taken in an optimal Hamiltonian cycle if and only if x_i_j == 1.
    x = [[pulp.LpVariable('x_' + str(i) + '_' + str(j), cat='Binary')
          for i in range(n)] for j in range(n)]

    # Never take self-loops (an edge from i to i).
    for i in range(n):
        m += pulp.lpSum(x[i][i]) == 0

    # Make sure the self-loops areof weight 0.
    for i in range(n):
        g.add_edge(i, i, weight=0)
    # The objective function (to be minimized) is the sum of the weights of taken edges
    m += pulp.lpSum([g[i][j]['weight'] * x[i][j] for i in range(n) for j in range(n)])

    # Add the constraints saying that each vertex has exactly one outgoing edge.
    for i in range(n):
        m += pulp.lpSum([x[i][j] for j in range(n)]) == 1

    # Add the constraints saying that each vertex has exactly one incoming edge.
    for i in range(n):
        m += pulp.lpSum([x[j][i] for j in range(n)]) == 1

    # Introduce auxiliary variables u_i for 0 <= i <= n-1.
    u = []
    # u_0 = 0
    u.append(pulp.LpVariable('u_0', 1, 1, cat='Integer'))
    # For i > 0, we have that 2 <= u_i <= n.
    for i in range(1, n):
        u.append(pulp.LpVariable('u_' + str(i), 2, n, cat='Integer'))

    # In order to ensure that we find *one* cycle covering all vertices,
    # for every i, j > 0, we add the constraint u_i - u_j + n * x_i_j <= n-1
    for i in range(1, n):
        for j in range(1, n):
            m += pulp.lpSum([u[i] - u[j] + n * x[i][j]]) <= n - 1

    # Solve the constructed Integer Linear Program.
    m.solve()

    # Compute the weight of the resulting cycle.
    weight = sum([g[i][j]['weight'] * pulp.value(x[i][j]) for i in range(n) for j in range(n)])
    print('The minimal cycle length is %f' % weight)

    # Extract cycle from the matrix x
    cycleMatrix = [[pulp.value(x[i][j]) for i in range(n)] for j in range(n)]
    i = 0
    i = cycleMatrix[0].index(1)
    cycle = [i]
    while (i != 0):
        i = cycleMatrix[i].index(1)
        cycle.append(i)
    return cycle