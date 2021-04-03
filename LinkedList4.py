from Node4 import Node

class LinkedList(object):
    def __init__(self, list=None):
      self.head = None
      if list is not None:
        for item in list:
          self.add(item)

    def print(self):
      n = self.head
      while n is not None:
        print(n.get_data(), "=>", end=" ")
        n = n.get_next()
      print("NULL")
    
    def add(self, new_el):
      new_node = Node(new_el, self.head)
      self.head = new_node

    def search(self, data):
      node = self.head
      while node != None:
        if node.get_data() == data:
          return True
        node = node.get_next()
      return False

    def delete(self, des_node):
      prev = None
      node = self.head
      while node != None:
        if node.get_data() == des_node:
          prev.set_next(node.get_next())
          return node
        prev = node
        node = node.get_next()
      return None

    def is_empty(self):
      return self.head == None
  
def main():
  l = LinkedList()
  print("is empty?", l.is_empty())
  l.print()
  l.add(5)
  l.add(6)
  l.add(7)
  l.print()
  print("is empty?", l.is_empty())
  print("Search 4: ", l.search(4))
  print("Search 5: ", l.search(5))
  print("Delete 6: ", l.delete(6))
  print("Delete 7: ", l.delete(7))
  l.print()

main()