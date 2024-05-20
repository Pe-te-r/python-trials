class Node:
  """
  Represents a node in a linked list.
  """
  def __init__(self, data):
    self.data = data
    self.next = None  # Pointer to the next node in the list

class LinkedList:
  """
  Represents a linked list data structure.
  """
  def __init__(self):
    self.head = None  # Head of the linked list (first node)

  def is_empty(self):
    """
    Checks if the linked list is empty.
    """
    return self.head is None

  def append(self, data):
    """
    Appends a new node with the given data to the end of the list.
    """
    new_node = Node(data)
    if self.is_empty():
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  def prepend(self, data):
    """
    Inserts a new node with the given data at the beginning of the list.
    """
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_after(self, prev_node, data):
    """
    Inserts a new node with the given data after a specific node.
    """
    if not prev_node:
      print("Previous node cannot be None")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, data):
    """
    Deletes the first node containing the given data.
    """
    if self.is_empty():
      return
    current = self.head
    prev = None
    while current and current.data != data:
      prev = current
      current = current.next
    if current is None:
      return  # Data not found
    if prev is None:
      self.head = current.next
    else:
      prev.next = current.next

  def print_list(self):
    """
    Prints the contents of the linked list.
    """
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

# Example usage
linked_list = LinkedList()
linked_list.append("apple")
linked_list.append("banana")
linked_list.prepend("orange")
linked_list.insert_after(linked_list.head.next, "mango")

linked_list.print_list()  # Output: orange -> mango -> apple -> banana -> None

linked_list.delete_node("apple")
linked_list.print_list()  # Output: orange -> mango -> banana -> None
