import pdb


with open('input.txt') as fh:
    text = fh.read().split()


class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = []


def get_create_node(tree, value):
    if not value in tree:
        tree[value] = Node(value)
    return tree[value]


tree = {}
root = None
for idx, line in enumerate(text):
    parent, child = line.split(')')

    p_node = get_create_node(tree, parent)
    c_node = get_create_node(tree, child)

    c_node.parent = p_node
    p_node.children.append(c_node)

    if idx == 0:
        root = p_node


def traverse_tree(node):
    print(node.value)
    for child in node.children:
        traverse_tree(child)


def count_nodes(node):
    if node.parent == None:
        return 0
    else:
        return 1 + count_nodes(node.parent)


def get_nodes(node, ans):
    if node.parent:
        ans.append(node.parent.value)
        get_nodes(node.parent, ans)


#Part 1
#total = 0
#for key in tree:
#    node = get_create_node(tree, key)
#    total += count_nodes(node)
#print(total)

you = get_create_node(tree, 'YOU')
san = get_create_node(tree, 'SAN')
seen = set()

you_nodes = []
get_nodes(you, you_nodes)

san_nodes = []
get_nodes(san, san_nodes)

print(you_nodes)
print(san_nodes)


def a_to_b(a_nodes, b_nodes):
    b_nodes_set = set(b_nodes)
    for idx, node_id in enumerate(a_nodes):
        if node_id in b_nodes_set:
            return idx


print(a_to_b(you_nodes, san_nodes) + a_to_b(san_nodes, you_nodes))
    