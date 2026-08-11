class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


n = int(input("Enter number of nodes: "))

head = None
tail = None

for i in range(n):
    data = int(input("Enter value: "))

    new_node = Node(data)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        new_node.prev = tail
        tail = new_node


def delete_head(head):
    if head is None:
        return None

    head = head.next

    if head is not None:
        head.prev = None

    return head


head = delete_head(head)

temp = head

while temp:
    print(temp.data, end=" ")
    temp = temp.next