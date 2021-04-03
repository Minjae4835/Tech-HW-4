from Node1 import Node

class Stack(object):
  def __init__(self):
    self.head = None

  def print(self):
    n = self.head
    while n is not None:
      print(n.get_data(), "=>", end=" ")
      n = n.get_next()
    print("NULL")

  def push(self, number=None):
    prev = self.head
    newnode = Node(number)
    newnode.set_next(prev)
    self.head = newnode
  
  def pop(self):
    if self.is_empty():
      return None
    n = self.head
    self.head = self.head.get_next()
    return n
  
  def peek(self):
    return self.head
  
  def clear(self):
    self.head = None
  
  def is_empty(self):
    return self.head == None


def main():
  s = Stack()
  s.print()
  print("Is empty:", s.is_empty())
  s.push(5)
  s.push(6)
  s.push(7)
  s.print()
  print("Peek:", s.peek())
  print("Pop: ", s.pop())
  s.print()
  print("Is empty:", s.is_empty())
  s.clear()
  s.print()
  print("Is empty:", s.is_empty())

main()