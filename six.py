class Tree:

    def __init__(self, file_lines):
        self.nodes_dict = {}
        for idx, line in enumerate(file_lines):
            parent, child = line.split(')')
            self.nodes_dict[child] = parent # Backwards

    def count_parents(self, node):
        if node not in self.nodes_dict:
            return 0
        return 1 + self.count_parents(self.nodes_dict[node])

    def get_parents(self, node):
        parents = []
        while node in self.nodes_dict:
            node = self.nodes_dict[node]
            parents.append(node)
        return parents


with open('input.txt') as fh:
    lines = fh.read().split()

tree = Tree(lines)

total = 0
for node in tree.nodes_dict:
    total += tree.count_parents(node)
print(total) # Part 1

you_nodes = tree.get_parents('YOU')
san_nodes = tree.get_parents('SAN')


def a_to_b(a_nodes, b_nodes):
    b_nodes_set = set(b_nodes)
    for idx, node in enumerate(a_nodes):
        if node in b_nodes_set:
            return idx


print(a_to_b(you_nodes, san_nodes) + a_to_b(san_nodes, you_nodes))