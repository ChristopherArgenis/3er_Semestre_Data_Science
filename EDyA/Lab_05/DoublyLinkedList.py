class Node(object):
  def __init__(self, data=None, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class DoublyLinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def append(self, data):
    """Append an item to the list"""
    new_node = Node(data, None, None)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
      self.count += 1

  def delete(self, data):
    """Delete a node from the list"""
    current = self.head
    node_deleted = False
    if current is None:
      node_deleted = False
    elif current.data == data:
      self.head = current.next
      self.head.prev = None
      node_deleted = True
    elif self.tail.data == data:
      self.tail = self.tail.prev
      self.tail.next = None
      node_deleted = True
    else:
      while current:
        if current.data == data:
          current.prev.next = current.next
          current.next.prev = current.prev
          node_deleted = True
        current = current.next
    if node_deleted:
      self.count -= 1

  def iter(self):
    """Iterate through the list."""
    current = self.head
    while current:
      val = current.data
      current = current.next
      yield val

  def contain(self, data):
    """Check if the list contains a node"""
    for node_data in self.iter():
      if data == node_data:
        return True
    return False

# - - - - - - - - - - - - - - - - - - - - - - - -

# My example of Use:
# Creamos una nueva lista doblemente enlazada
my_list = DoublyLinkedList()

# Agregamos algunos elementos a la lista
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Imprimimos la lista (usando el método iter())
print("Lista original:")
for item in my_list.iter():
    print(item)

# Eliminamos el elemento 20 de la lista
my_list.delete(20)

# Verificamos si el elemento 30 está en la lista
print("¿Contiene 30?", my_list.contain(30))

# Imprimimos la lista actualizada
print("Lista después de eliminar 20:")
for item in my_list.iter():
    print(item)

# - - - - - - - - - - - - - - - - - - - - - - - -

# output:
# Lista original:
# 10
# 20
# 30
# ¿Contiene 30? True
# Lista después de eliminar 20:
# 10
# 30