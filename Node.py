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

# Fourth node -> Third node -> Second node -> First node
def main():
	new_node = Node("first node data")
	next_node = Node("second node data", new_node)
	print(next_node.get_data())


#main()


# Don't run main on import
if __name__ == "__main__":
    main()
