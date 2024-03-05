import networkx as nx
import matplotlib.pyplot as plt


def plt_find_decomposition(budget: list[float], preferences: list[set[int]]):
    '''
       function to find if given budget and preferences are decomposition. if True return decomposition.
       :param budget: how much budget to each subject
       :param preferences: preferences of person to subject
       :return: True if decomposition, False otherwise

    >>> find_decomposition([400, 50, 50, 0], [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}])
    The Person 0 contribute:
    100.0 for 1
    The Person 1 contribute:
    100.0 for 1
    The Person 2 contribute:
    100.0 for 1
    The Person 3 contribute:
    50.0 for 2
    50.0 for 3
    The Person 4 contribute:
    100.0 for 1
    True
    >>> find_decomposition([400, 50, 50, 0], [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1}])
    False
    >>> find_decomposition([0, 0, 0, 500], [{0, 1}, {0, 2}, {0}, {1, 2}, {1}])
    False
    '''
    C = sum(x for x in budget)
    n = len(preferences)
    m = len(budget)

    s = m + n
    t = m + n + 1

    G = nx.DiGraph()
    # node to each person
    for i in range(n):
        G.add_node(i, layer="B", name=i)
    # node to each subject
    for i in range(n, m + n):
        G.add_node(i, layer="C", name=i - n)
    # s
    G.add_node(s, layer="A", name="S")
    # t
    G.add_node(t, layer="D", name="T")

    # from s to person
    for i in range(n):
        G.add_edge(s, i, capacity=C / n)
    # from person to subject if want it
    for i in range(len(preferences)):
        for subject in preferences[i]:
            G.add_edge(i, n + subject, capacity=C / n)
    # from subject to t
    for i in range(m):
        G.add_edge(n + i, t, capacity=budget[i])

    flow_value, flow_dict = nx.maximum_flow(G, s, t)
    for edge in G.edges():
        try:
            G[edge[0]][edge[1]]['label'] = flow_dict[edge[0]][edge[1]]
        except:
            pass

    # Remove edges with label == 0
    edges_to_remove = [(u, v) for u, v, label in G.edges(data='label') if label == 0]
    G.remove_edges_from(edges_to_remove)

    node_labels = {node: G.nodes[node]['name'] for node in G.nodes}

    # Draw the graph
    pos = nx.multipartite_layout(G, subset_key="layer")
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=3000, node_color="skyblue", font_size=10,
            font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

    if flow_value < C: return False

    for i in range(n):
        print(f'The Person {i} contribute:')
        for j in range(m):
            try:
                if flow_dict[i][m + j] > 0:
                    print(f'{flow_dict[i][m + j]} for {j}')
            except:
                pass

    return True


def find_decomposition(budget: list[float], preferences: list[set[int]]):
    '''
       function to find if given budget and preferences are decomposition. if True return decomposition.
       :param budget: how much budget to each subject
       :param preferences: preferences of person to subject
       :return: True if decomposition, False otherwise

    >>> find_decomposition([400, 50, 50, 0], [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}])
    The Person 0 contribute:
    100.0 for 1
    The Person 1 contribute:
    100.0 for 1
    The Person 2 contribute:
    100.0 for 1
    The Person 3 contribute:
    50.0 for 2
    50.0 for 3
    The Person 4 contribute:
    100.0 for 1
    True
    >>> find_decomposition([400, 50, 50, 0], [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1}])
    False
    >>> find_decomposition([0, 0, 0, 500], [{0, 1}, {0, 2}, {0}, {1, 2}, {1}])
    False
    '''
    C = sum(x for x in budget)
    n = len(preferences)
    m = len(budget)

    s = m + n
    t = m + n + 1

    G = nx.DiGraph()
    # node to each person
    for i in range(n):
        G.add_node(i)
    # node to each subject
    for i in range(n, m + n):
        G.add_node(i)
    # s
    G.add_node(s)
    # t
    G.add_node(t)

    # from s to person
    for i in range(n):
        G.add_edge(s, i, capacity=C / n)
    # from person to subject if want it
    for i in range(len(preferences)):
        for subject in preferences[i]:
            G.add_edge(i, n + subject, capacity=C / n)
    # from subject to t
    for i in range(m):
        G.add_edge(n + i, t, capacity=budget[i])

    flow_value, flow_dict = nx.maximum_flow(G, s, t)

    if flow_value < C: return False

    for i in range(n):
        print(f'The Person {i} contribute:')
        for j in range(m):
            try:
                if flow_dict[i][m + j] > 0:
                    print(f'{flow_dict[i][m + j]} for {j}')
            except:
                pass

    return True


if __name__ == '__main__':
    plt_find_decomposition([400, 50, 50, 0], [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1}])
