class Node:
    def __init__(self,value):
        self.value=value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def hill_climbing(start_node):
    current_node= start_node

    while True:
        best_node=max(current_node.children,key=lambda n: n.value,default=None)
        if not best_node or best_node.value <= current_node.value:return current_node
        current_node = best_node

nodeA, nodeB, nodeC, nodeD = Node(1), Node(2), Node(3), Node(4)
nodeA.add_child(nodeB)
nodeA.add_child(nodeC)
nodeB.add_child(nodeD)
print("Best Node value:", hill_climbing(nodeA).value)
