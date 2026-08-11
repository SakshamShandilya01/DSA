class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def delete_tail(head):

    if head is None:
        return None

    if head.next is None:
        return None

    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.prev.next = None

    return head


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


head = delete_tail(head)

temp = head

while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next