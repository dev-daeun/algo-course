# python3
from sys import stdin

MODULO = 1000000001


# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v


def left_rotate(root):
  y = root.right
  root.right = y.left
  y.left = root

  y.parent = root.parent
  root.parent = y

  update(root)
  update(y)

def right_rotate(root):
  y = root.left
  root.left = y.right
  y.right = root

  y.parent = root.parent
  root.parent = y

  update(root)
  update(y)


def is_root(node):
  return not node.parent


def splay(node):
  if is_root(node):
    return node

  parent = node.parent
  grandparent = parent.parent

  if grandparent:
    if grandparent.key > parent.key > node.key:  # left-left
      right_rotate(parent)
      right_rotate(grandparent)
    if grandparent.key < parent.key < node.key:  # right-right
      left_rotate(parent)
      left_rotate(grandparent)
    if grandparent.key < parent.key > node.key:  # right-left
      right_rotate(parent)
      left_rotate(grandparent)
    if grandparent.key > parent.key < node.key: # left-right
      left_rotate(parent)
      right_rotate(grandparent)
  else:
    if node.parent.key < node.key:
      left_rotate(parent)
    if node.parent.key > node.key:
      right_rotate(parent)

  if not is_root(node):
    splay(node)

  return node


def binary_search(root, x):
  while root:
    if root.key < x:
      root = root.right
      continue
    if root.key > x:
      root = root.left
      continue
    return root
  return root.parent


def find(root, key): 
  result = binary_search(root, key)
  splay(result)
  if result.key == key:
    return True
  return False


def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

  
def insert(root, x):
  parent = find(root, x)
  new_node = Vertex(key=x, sum=x, left=None, right=None, parent=parent)
  if parent.key > x:
    parent.left = new_node
    update(parent)
  else if parent.key < x:
    parent.right = new_node
    update(parent)
  else:
    return splay(parent)
  return splay(new_node)


def delete(root, x):
  result = find(root, x)
  splay(result)
  if result.key == x:
    merge(result.left, result.right)


def split_left(root):
  subtree_to_split = root.left
  subtree_to_split.parent = None
  root.sum -= subtree_to_split.sum
  root.left = None
  return subtree_to_split, root


def split_right(root):
  subtree_to_split = root.right
  subtree_to_split.parent = None
  root.sum -= subtree_to_split.sum
  root.right = None
  return subtree_to_split, root


def range_sum(root, fr, to):
  fr_node = binary_search(root, fr)
  if fr_node.key != fr:
    return None
  splay(fr_node)
  dumped_left, splayed_root = split_left(fr_node)

  to_node = binary_search(splayed_root, to)
  if to_node.key != to:
    return None
  splay(to_node)
  dumped_right, splayed_root2 = split_right(to_node)
  result = splayed_root2.sum
  merged = merge(dumped_left, splayed_root2)
  merge(merged, dumped_right)
  return result


def test(i):
  n, data* = open(f'./tests/{i}').readlines()
  result = []

  for d in data:
    op, num = d.split()
    last_sum = 0
    input_ = (int(num) + last_sum_result) % MODULO
  
    if op == '+':
      insert(input_)
    if op == '-':
      delete(input_)
    if op == '?':
      result.append('Found' if find(input_) else 'Not Found')
    if op == 's':
      fr, to = list(map(lambda x: int(x), num.split()))
      fr = (fr + last_sum_result) % MODULO
      to = (fr + last_sum_result) % MODULO
      result.append(range_sum((fr , to))

  output* = open(f'./tests/{i}.a').readlines()
  result = [str(r) for r in result]
  assert result == output


if __name__ == '__main__':
  n = int(stdin.readline())
  last_sum_result = 0
  for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
      x = int(line[1])
      insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
      x = int(line[1])
      delete((x + last_sum_result) % MODULO)
    elif line[0] == '?':
      x = int(line[1])
      print('Found' if find((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
      l = int(line[1])
      r = int(line[2])
      res = range_sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
      print(res)
      last_sum_result = res % MODULO