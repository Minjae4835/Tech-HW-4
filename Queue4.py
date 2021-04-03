class Queue(object):
  def __init__(self, size=5):
    self.array = [None for i in range(size)] 
    # no python list function calls!
    self.front = -1
    self.tail = -1

  def print(self):
    for i in range(self.front, self.front + self.size(), 1):
      print(self.array[i % len(self.array)], "=>", end=" ")
    print("NULL\n", self.array)
    print("Size:", self.size())

  def enq(self, number=None):
    # if queue is empty:
    if self.is_empty(): # is empty
      self.front = 0
      self.tail = 0
      self.array[0] = number
      return
    if self.is_full():
      # FIXME double in size if full
      # print("Uh oh we're full!")
      # Creating a new array double the size
      new_array = [None for i in range(2 * self.size())]
      # copy everything over
      size = self.size()
      for i in range(size):
        x = i + self.front # unrolling old array
        new_array[i] = self.array[x % len(self.array)] 
      self.array = new_array
      self.front = 0
      self.tail = size - 1
    #else: 
    self.tail += 1
    self.array[self.tail % len(self.array)] = number
  
  def deq(self):
    #remove data @ front
    # what happens when it's empty?
    # OR when the front exceeds the end of array
    if self.is_empty():
      return None
    n = self.array[self.front]
    self.front += 1
    return n
  
  def get_front(self):
    if self.is_empty():
      return None
    else:
      return self.array[self.front]
  
  def get_tail(self):
    if self.is_empty():
      return None
    else:
      return self.array[self.tail % len(self.array)]
  
  def clear(self):
    self.array = [None for i in range(self.size())]
    self.front = -1
    self.tail = -1
  
  def size(self):
    if self.front == -1:
      return 0
    l = self.tail - self.front + 1
    if self.tail < self.front:
        l = len(self.array) - self.front + self.tail + 1
    return l

  def is_full(self):
    l = self.size()
    return l >= len(self.array)

  def is_empty(self):
    return self.size() == 0 


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
  print("Deq:  ", q.deq())
  q.print()
  # testing when it gets full & wraps around
  for i in range(8, 15):
    q.enq(i)
    q.print()
  print("Tail: ", q.get_tail())  
  print("Is empty?", q.is_empty())
  q.clear()
  q.print()
  print("Is empty?", q.is_empty())
  print("Front:", q.get_front())
  print("Tail: ", q.get_tail()) 

main()
  