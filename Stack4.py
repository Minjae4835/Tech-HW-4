from Node4 import Node

class Stack(object):
  def __init__(self):
    self.tail = None

  def print(self):
    n = self.tail
    while n is not None:
      print(n.get_data(), "=>", end=" ")
      n = n.get_next()
    print("NULL")

  def push(self, data=None):
    new_node = Node(data, self.tail)
    self.tail = new_node

  
  def pop(self):
    if self.is_empty():
      return None
    else:
      top = self.tail
      self.tail = self.tail.get_next()
      return top.get_data()
  
  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.tail.get_data()

  
  def clear(self):
    self.tail = None

  def is_empty(self):
    return self.tail is None


def main():
  s = Stack()
  s.print()
  s.push(5)
  s.push(6)
  s.push(7)
  s.print()
  print("Peek:", s.peek())
  print("Pop: ", s.pop())
  s.print()

main()