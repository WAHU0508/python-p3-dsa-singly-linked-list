class Node:
    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:

  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def append(self, node):
    if self.head == None:
        self.head = node
        self.tail = node
        return
    node.prev_node = self.tail
    self.tail.next_node = node
    self.tail = node