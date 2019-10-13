# python3
from sys import stdin

MODULO = 1000000001


# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

  def update(self):
    self.sum = self.key + (self.left.sum if self.left != None else 0) + (self.right.sum if self.right != None else 0)
    if self.left != None:
      self.left.parent = self
    if self.right != None:
      self.right.parent = self

  def is_root(self):
    return not self.parent


class SplayTree:

  def __init__(self):
    self.root = None

  @staticmethod
  def left_rotate(node):
    y = node.right
    node.right = y.left
    y.left = node

    y.parent = node.parent
    node.parent = y

    node.update()
    y.update()

  @staticmethod
  def right_rotate(node):
    y = node.left
    node.left = y.right
    y.right = node

    y.parent = node.parent
    node.parent = y

    node.update()
    y.update() 

  def splay(self, node):
    if node.is_root():
      return node
    
    parent = node.parent
    grandparent = parent.parent

    if grandparent:
      if grandparent.key > parent.key > node.key:  # left-left
        self.right_rotate(parent)
        self.right_rotate(grandparent)
      if grandparent.key < parent.key < node.key:  # right-right
        self.left_rotate(parent)
        self.left_rotate(grandparent)
      if grandparent.key < parent.key > node.key:  # right-left
        self.right_rotate(parent)
        self.left_rotate(grandparent)
      if grandparent.key > parent.key < node.key: # left-right
        self.left_rotate(parent)
        self.right_rotate(grandparent)
    else:
      if node.parent.key < node.key:
        self.left_rotate(parent)
      if node.parent.key > node.key:
        self.right_rotate(parent)

    if not node.is_root():
      self.splay(node)

    return node

  @staticmethod
  def binary_search(root, key):
    while root:
      if root.key < key:
        root = root.right
        continue
      if root.key > key:
        root = root.left
        continue
      return root
    return root.parent

  def find(self, key):
    if not root:
      return False
    
    result = self.binary_search(self.root, key)
    self.splay(result)
    
    if result.key != key:
      return False
    return True

  def split(self, root, key):
    result = self.binary_search(root, key)
    if result.key != key:
      return root, None
    
    right = self.splay(result)
    left = right.left
    right.left = None

    if left != None:
      left.parent = None

    left.update()
    right.update()
    return left, right

  def merge(self, left, right):
    if left == None:
      return right
    if right == None:
      return left
    
    while right.left != None:
      right = right.left
    
    right = self.splay(right)
    right.left = left
    right.update()
    return right
  
  def insert(self, key):
    new_node = Vertex(key=x, sum=x, left=None, right=None, parent=None)
    if not self.root:
      self.root = new_node
      return

    parent = self.binary_search(self.root, key)
    if parent.key > x:
      parent.left = new_node
      parent.update()
    elif parent.key < x:
      parent.right = new_node
      parent.update()
    else:
      return self.splay(parent)
    return self.splay(new_node)

  def delete(self, key):
    if not self.root:
      return
    result = self.binary_search(self.root, key)
    splayed_result = self.splay(result)
    if splayed.key == key:
      self.merge(splayed_result.left, splayed_result.right)

  @staticmethod
  def split_left(node):
    subtree_to_split = node.left
    subtree_to_split.parent = None
    node.sum -= subtree_to_split.sum
    node.left = None
    return subtree_to_split, node

  @staticmethod
  def split_right(node):
    subtree_to_split = node.right
    subtree_to_split.parent = None
    node.sum -= subtree_to_split.sum
    node.right = None
    return subtree_to_split, node

  def range_sum(self, root, fr, to):
    fr_node = self.binary_search(root, fr)
    if fr_node.key != fr:
      return None
    
    root_to_split = self.splay(fr_node)
    dumped_left, splayed_root = self.split_left(root_to_split)

    to_node = self.binary_search(splayed_root, to)
    if to_node.key != to:
      return None
    
    root_to_split = self.splay(to_node)
    dumped_right, splayed_root2 = self.split_right(root_to_split)
    result = splayed_root2.sum
    merged = self.merge(dumped_left, splayed_root2)
    self.merge(merged, dumped_right)
    return result


def test(i):
  n, *data = open(f'./tests/{i}').readlines()
  result = []
  spt = SplayTree()

  for d in data:
    op, num = d.split()
    last_sum_result = 0
    input_ = (int(num) + last_sum_result) % MODULO

    if op == '+':
      spt.insert(input_)
    if op == '-':
      spt.delete(input_)
    if op == '?':
      result.append('Found' if spt.find(input_) else 'Not Found')
    if op == 's':
      fr, to = list(map(lambda x: int(x), num.split()))
      fr = (fr + last_sum_result) % MODULO
      to = (fr + last_sum_result) % MODULO
      result.append(spt.range_sum((fr , to)))

  output = open(f'./tests/{i}.a').readlines()
  result = [str(r) for r in result]
  assert result == output


if __name__ == '__main__':
  test(2)
  # n = int(stdin.readline())
  # last_sum_result = 0
  # for i in range(n):
  #   line = stdin.readline().split()
  #   if line[0] == '+':
  #     x = int(line[1])
  #     insert((x + last_sum_result) % MODULO)
  #   elif line[0] == '-':
  #     x = int(line[1])
  #     delete((x + last_sum_result) % MODULO)
  #   elif line[0] == '?':
  #     x = int(line[1])
  #     print('Found' if find((x + last_sum_result) % MODULO) else 'Not found')
  #   elif line[0] == 's':
  #     l = int(line[1])
  #     r = int(line[2])
  #     res = range_sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
  #     print(res)
  #     last_sum_result = res % MODULO