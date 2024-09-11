class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, node):
        """Check if list is empty. The new node thus beomes the first node."""
        if self.head == None:
            self.head = node
            return
        """Set the first node to the last node."""
        last_node = self.head
        """Loop until you find last node"""
        while last_node.next_node:
            """Move from one node to the next. Loops until last node is none."""
            last_node = last_node.next_node
        last_node.next_node = node
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return " -> ".join(nodes)
    
my_linked_list = LinkedList()
my_linked_list.append(Node("Bulldog"))
my_linked_list.append(Node("Chihuahua"))
my_linked_list.append(Node("German Shephard"))
print(my_linked_list)