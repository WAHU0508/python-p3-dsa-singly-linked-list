class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = None

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        # last_node = self.head
        # while last_node.next_node:
        #     last_node = last_node.next_node
        # last_node.next_node = node
        self.tail.next_node = node
        self.tail = node
        
    def delete_tail(self):
      if self.head == None:
        return
      # traverse the entire list to find the second-to-last node (prev)
      curr = self.head
      prev = None
      while curr.next_node:
        prev = curr
        curr = curr.next_node
      # remove the last node by removing the link between the second-to-last node and the tail
      # 1 -> 2 -> 3
      prev.next_node = None
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return " -> ".join(nodes)
    
my_linked_list = SinglyLinkedList()
my_linked_list.append(Node("Bulldog"))
my_linked_list.append(Node("Chihuahua"))
my_linked_list.append(Node("German Shephard"))
print(my_linked_list)