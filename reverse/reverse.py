class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        out = ""
        node = self.head
        if node != None:
            out = str(node.value) + "->"
            while node.next_node != None:
                node = node.next_node
                out += str(node.value) + "->"
        out += "None"
        return out

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if getattr(node, 'next_node', None) == None:     # Attempting to reverse an empty or single-node list
            return
        else:                                            # Valid list for reversing
            self.head = None                             # Set head to none so that add_to_head calls will not build upon our existing list
            while node != None:
                self.add_to_head(node.value)             # We still have a ref to the old list via node so we can add every item in it to the new list
                node = node.next_node
            
