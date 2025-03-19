class Node:
    """A generic node that can store any type of record dynamically."""
    def __init__(self, **kwargs):
        self.data = kwargs  # Store data as dictionary
        self.next = None  # Pointer to the next node

class LinkedList:
    """A generic linked list to store various records."""
    def __init__(self):
        self.head = None
    
    def to_list(self):
        """Convert the linked list to a list of dictionaries."""
        result = []
        current = self.head
        while current:
            result.append(current.data)  # Assuming `data` is stored as a dictionary
            current = current.next
        return result

    def add_first(self, **kwargs):
        """Insert a record at the beginning."""
        new_node = Node(**kwargs)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, **kwargs):
        """Insert a record at the end."""
        new_node = Node(**kwargs)
        if not self.head:
            self.head = new_node
            return
        c1 = self.head
        while c1.next:
            c1 = c1.next
        c1.next = new_node

    def delete_node(self, **kwargs):
        """Delete a node by matching keyword arguments."""
        if not self.head:
            print("List is empty")
            return None

        c1 = self.head
        previous = None

        while c1:
            if all(c1.data.get(k) == v for k, v in kwargs.items()):
                if previous:
                    previous.next = c1.next
                else:
                    self.head = c1.next
                return c1.data  # Return deleted node data
            previous = c1
            c1 = c1.next

        print("No matching record found")
        return None

    def print_list(self):
        """Print all records in the linked list."""
        c1 = self.head
        while c1:
            print(c1.data)
            c1 = c1.next