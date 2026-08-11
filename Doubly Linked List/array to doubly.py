class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


arr = [10, 20, 30, 40]

head = None
prev = None

for value in arr:
    new_node = Node(value)

    if head is None:
        head = new_node
    else:
        prev.next = new_node
        new_node.prev = prev

    prev = new_node