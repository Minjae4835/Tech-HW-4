from Node4 import Node

class Stack(object):
  def __init__(self):
    self.head = None

  def print(self):
    n = self.head
    while n is not None:
      print(n.get_data(), "=>", end=" ")
      n = n.get_next()
    print("NULL")

  def push(self, data=None):
    # FIXME
    return
  
  def pop(self):
    # FIXME
    return
  
  def peek(self):
    # FIXME
    return
  
  def clear(self):
    # FIXME
    return
  
  def is_empty(self):
    # FIXME
    return


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