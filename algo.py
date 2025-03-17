class Node:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


node_last = Node(value='Последний элемент')
node_middle = Node(value='Первый элемент за головой', next_item=node_last)
node_head = Node(value='Голова', next_item=node_middle)

temp_node = node_head
while temp_node is not None:
    print(temp_node)
    temp_node = temp_node.next_item