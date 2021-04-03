class Queue(object):
  def __init__(self, size=5):
    self.q = [None for i in range(size)]  
    # no python list function calls!
    self.front = -1
    self.tail = -1

  def print(self):
    # Ideally, we want to go from front -> tail
    for i in range(self.front, self.front + self.size()):
      print(self.q[i % len(self.q)], "=>", end=" ")
    print("NULL")
    print(self.q)
    print("Size:", self.size())

  def enq(self, number=None):
    # what if empty?
    if self.is_empty():
      self.front = 0
    elif self.is_full():
      # 	(double array size)
      #print("Uh oh, it's full!")
      size = self.size()
      new_array = [None for i in range(2 * size)]
      for i in range(size):
        old_index = (i + self.front) % len(self.q)
        new_array[i] = self.q[old_index]
      self.q = new_array
      self.front = 0
      self.tail = size - 1 # the last element
    # end.append(number)
    self.tail += 1
    self.tail = self.tail % len(self.q)
    self.q[self.tail] = number
  
  def deq(self):
    if self.is_empty():
	 	  return None # Queue is empty
    else:	 
      x = self.q[self.front]
      #self.front = self.next
      self.front += 1 
      return x 

  
  def get_front(self):
    # what if it's empty?
    return self.q[self.front]
  
  def get_tail(self):
    # what if it's empty?
    return self.q[self.tail]
  
  def clear(self):
    self.front = -1
    self.tail = -1

  def is_empty(self):
    # can check size == 0
    return self.front == -1 and self.tail == -1
  
  def is_full(self):
    return self.size() >= len(self.q)
  
  def size(self):
    if self.front == -1:
      return 0
    l = self.tail - self.front + 1
    if self.tail < self.front:
        l = len(self.q) - self.front + self.tail + 1
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