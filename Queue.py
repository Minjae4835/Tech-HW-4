class Queue(object):
  def __init__(self, size=5):
    self.array = [None for i in range(size)]  
    # no python list function calls!
    self.front = -1
    self.tail = -1

  def print(self):
    # FIXME
    print(self.array)
    print("Size:", self.size())

  def enq(self, data=None):
    # FIXME
    return
  
  def deq(self):
    # FIXME
    return
  
  def get_front(self):
    # FIXME
    return
  
  def get_tail(self):
    # FIXME
    return
  
  def clear(self):
    # FIXME
    return

  def is_empty(self):
    # FIXME
    return
  
  def is_full(self):
    # FIXME
    return
  
  def size(self):
    if self.front == -1:
      return 0
    l = self.tail - self.front + 1
    if self.tail < self.front:
        l = len(self.array) - self.front + self.tail + 1
    return l


def main():
  q = Queue()
  q.print()
  print("Front:", q.get_front())
  print("Tail: ", q.get_tail())
  q.enq(5)
  q.enq(6)
  q.enq(7)
  q.print()
  print("Front:", q.get_front())
  print("Tail: ", q.get_tail())
  print("Deq:  ", q.deq())
  q.print()
  # testing when it gets full & wraps around
  # for i in range(8, 12):
  #   q.enq(i)
  #   q.print()
  print("Tail: ", q.get_tail())
  print("Is empty?", q.is_empty())
  q.clear()
  q.print()
  print("Is empty?", q.is_empty())
  print("Front:", q.get_front())
  print("Tail: ", q.get_tail())

main()