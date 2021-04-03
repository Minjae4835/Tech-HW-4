
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
def main(): # stand-in for linked list class
	new_node = Node("First node")
	next_node = Node("Second node", new_node)
	third_node = Node("Third node", next_node)
  # Fourth node?
	fourth_node = Node("Fourth node", third_node)
  
	#print(next_node.get_data())
	# Print
	n = fourth_node # head
	while n != None:
		print(n.get_data(), "-> ", end = "")
		n = n.get_next()
	print()

#main()

# Don't run main on import
if __name__ == "__main__":
    main()