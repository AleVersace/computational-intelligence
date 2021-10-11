'''
Bricks problem, like the bag problem, we have to build a wall using bricks that have different values
chosing the ones that will bring us to our GOAL value, arbitrarily chosen.
'''

import random
from collections import deque

from matplotlib import pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout


random.seed(42)
BLOCKS = [random.randint(1, 50) for _ in range(10)]
print(BLOCKS)

GOAL = 79

search_tree = nx.DiGraph()

# The frontier contains all the blocks divided in ((used), (not used))
# Definetely redundant, but functional
frontier = deque()
frontier.append(((), tuple(sorted(BLOCKS, reverse=False))))
node_color = dict()

n = 0
while frontier:
    n += 1
    current_bag, available_blocks = frontier.popleft()
    print(current_bag)
    search_tree.add_node(current_bag)

    node_color[current_bag] = 'yellow'
    if sum(current_bag) == GOAL:
        print(f"Whoa! Found a solution in {n:,} steps\n\t{current_bag}")
        node_color[current_bag] = 'lime'
        break
    if sum(current_bag) > GOAL:
        node_color[current_bag] = 'red'
        continue
    node_color[current_bag] = 'royalblue'

    for i, object in enumerate(available_blocks):
        new_state = ((*current_bag, object), tuple(available_blocks[:i]+available_blocks[i+1:]))
        search_tree.add_node(new_state[0])

        node_color[new_state[0]] = 'lavender'

        search_tree.add_edge(current_bag, new_state[0], label=object)
        frontier.appendleft(new_state)  # using just "append" will use a breath-first approach

node_color[()] = 'navy'
plt.figure(figsize=(12, 12))
pos = graphviz_layout(search_tree, prog='fdp')
nx.draw(search_tree, pos=pos,
    node_color=[node_color[n] for n in search_tree.nodes],
    with_labels=False)
nx.draw_networkx_edge_labels(search_tree, pos=pos, edge_labels=nx.get_edge_attributes(search_tree, 'label'))
plt.show()



