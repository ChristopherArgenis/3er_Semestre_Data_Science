class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0

  def push(self, data):
    node = Node(data)
    if self.top:
      node.next = self.top
      self.top = node
    else:
      self.top = node
    self.size += 1

  def pop(self):
    if self.top:
      data = self.top.data
      self.size -= 1
      if self.top.next:
        self.top = self.top.next
      else:
        self.top = None
      return data
    else:
      return None

  def peek(self):
    if self.top:
      return self.top.data
    else:
      return None

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def check_parentheses(statement):
  stack = Stack()

  for char in statement:
    if char in ('{', '[', '('):
      stack.push(char)
    elif char in ('}', ']', ')'): # changed from if to elif and == to in
      last = stack.pop()
      if last == '{' and char == '}':
        continue
      elif last == '[' and char == ']':
        continue
      elif last == '(' and char == ')':
        continue
      else:
        return False
  if stack.size > 0:
    return False
  else:
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Example:
sl = (
    '{(foo)(bar)}[hello](((this)is)a)test',
    '{(foo)(bar)}[hello](((this)is)atest',
    '{(foo)(bar)}[hello](((this)is)a)test))'
)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

for s in sl:
  m = check_parentheses(s)
  print(f'{s}: {m}')