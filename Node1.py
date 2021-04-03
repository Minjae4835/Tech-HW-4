class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return self.data.__str__()

    def __repr__(self):
        return self.data.__repr__()

# Fourth node -> Third node -> Second node -> First node
def main():
  new_node = Node("First node")
  next_node = Node("Second node", new_node)
  node3 = Node("Third node", next_node)
  node4 = Node("Fourth node", node3)
  #print(next_node.get_data())
  n = node4 # Print the whole list
  while n is not None:
    print(n.get_data(), "->", end=" ")
    n = n.get_next()
  print()


#main()


# Don't run main on import
if __name__ == "__main__":
    main()