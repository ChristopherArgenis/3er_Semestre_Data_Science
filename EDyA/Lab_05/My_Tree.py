# My Tree
class Node:
  def __init__(self, data):
    self.data = data
    self.right_child = None
    self.left_child = None

# Node capa 1
n1 = Node("2")
# Nodes capa 2
n2 = Node("1")
n3 = Node("4")
# Node capa 3
n4 = Node("3")
n5 = Node("7")
# Node capa 4
n6 = Node("20")
# Node capa 5
n7 = Node("50")

# Inspirado en el slide 21
n1.left_child = n2
n1.right_child = n3
n3.left_child = n4
n3.right_child = n5
n5.right_child = n6
n6.right_child = n7

# Lista de Nodos
list_Nodes = [n1, n2, n3, n4, n5, n6, n7]

#Iteracion de cada Nodo
for n in list_Nodes:
  if n.left_child: # Si tiene elemento a la izquierda:  imprimirlo
    print(f"{n.data} -> {n.left_child.data}")
  if n.right_child: # Si tiene elemento a la derecha: imprimirlo
    print(f"{n.data} -> {n.right_child.data}")

# Output
# 2 -> 1
# 2 -> 4
# 4 -> 3
# 4 -> 7
# 7 -> 20
# 20 -> 50