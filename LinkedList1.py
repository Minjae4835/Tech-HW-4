from Node1 import Node

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
    
    def add(self, data):
      n = Node(data)
      if self.head is not None:
        n.set_next(self.head)
      self.head = n
    
    def search(self, number):
      nextNode = self.head
      while nextNode is not None and nextNode.get_data() != number:
        nextNode = nextNode.get_next()
      # return nextNode
      return nextNode is not None

    def delete(self, data):
      n = self.head
      prev = None
      while n is not None:
        if n.get_data() is data:
          # Delete
          if prev is None:
            self.head = n.get_next()
          else:
            prev.set_next(n.get_next())
          return n.get_data() # optional
        prev = n
        n = n.get_next()
      return None # nothing deleted

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