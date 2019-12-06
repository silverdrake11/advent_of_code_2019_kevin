
def count_nodes(tree, node):
    if node not in tree:
        return 0
    node = tree[node]
    return 1 + count_nodes(tree, node)


with open('input.txt') as fh:
    text = fh.read().split()

tree = {}
root = None
for idx, line in enumerate(text):
    parent, child = line.split(')')
    tree[child] = parent

total = 0
for node in tree:
    total += count_nodes(tree, node)
print(total) # Part 1


def get_nodes(tree, node):
    nodes = []
    while node in tree:
        node = tree[node]
        nodes.append(node)
    return nodes


def a_to_b(a_nodes, b_nodes):
    b_nodes_set = set(b_nodes)
    for idx, node in enumerate(a_nodes):
        if node in b_nodes_set:
            return idx


you_nodes = get_nodes(tree, 'YOU')
san_nodes = get_nodes(tree, 'SAN')

print(a_to_b(you_nodes, san_nodes) + a_to_b(san_nodes, you_nodes))