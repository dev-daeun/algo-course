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
  
  def is_leaf(self):
    return not (self.left or self.right)


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
    return y

  @staticmethod
  def right_rotate(node):
    y = node.left
    node.left = y.right
    y.right = node

    y.parent = node.parent
    node.parent = y

    node.update()
    y.update()
    return y

  def splay(self, node):
    if node.is_root():
      self.root = node
      self.root.update()
      return node
    else:
      parent = node.parent
      grandparent = parent.parent

      if grandparent:
        if grandparent.key > parent.key > node.key:  # left-left
          splayed1 = self.right_rotate(parent)
          splayed2 = self.right_rotate(splayed1.parent)
        if grandparent.key < parent.key < node.key:  # right-right
          splayed1 = self.left_rotate(parent)
          splayed2 = self.left_rotate(splayed1.parent)
        if grandparent.key < parent.key > node.key:  # right-left
          splayed1 = self.right_rotate(parent)
          splayed2 = self.left_rotate(splayed1.parent)
        if grandparent.key > parent.key < node.key: # left-right
          splayed1 = self.left_rotate(parent)
          splayed2 = self.right_rotate(splayed1.parent)

        if not splayed2.is_root():
          self.splay(splayed2)
        else:
          return splayed2
      else:
        if parent.key < node.key:
          splayed = self.left_rotate(parent)
        if parent.key > node.key:
          splayed = self.right_rotate(parent)

        if not splayed.is_root():
          self.splay(splayed)
        else:
          return splayed

  @staticmethod
  def is_leaf(root):
    return not (root.left or root.right)

  def binary_search(self, root, key):
    if root.key == key:
      return root
    
    if root.key > key:
      if not root.left:
        return root
      return self.binary_search(root.left, key)
    
    if root.key < key:
      if not root.right:
        return root
      return self.binary_search(root.right, key)

  def find(self, key):
    if not self.root:
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
    new_node = Vertex(key=key, sum=key, left=None, right=None, parent=None)
    if not self.root:
      self.root = new_node
      self.root.update()
      return

    parent = self.binary_search(self.root, key)
    if parent.key > key:
      parent.left = new_node
      parent.update()
      self.splay(parent.left)
    elif parent.key < key:
      parent.right = new_node
      parent.update()
      self.splay(parent.right)
    else:
      self.splay(parent)

  def delete(self, key):
    if not self.root:
      return
    result = self.binary_search(self.root, key)
    splayed_result = self.splay(result)
    if splayed_result.key == key:
      self.merge(splayed_result.left, splayed_result.right)

  @staticmethod
  def split_left(node):
    subtree_to_split = node.left
    if subtree_to_split:
      subtree_to_split.parent = None
      node.sum -= subtree_to_split.sum
      node.left = None
    return subtree_to_split, node

  @staticmethod
  def split_right(node):
    subtree_to_split = node.right
    if subtree_to_split:
      subtree_to_split.parent = None
      node.sum -= subtree_to_split.sum
      node.right = None
    return node, subtree_to_split

  def traverse(self, root):
    if root:
      self.traverse(root.left)
      print(root.key)
      self.traverse(root.right)

  def range_sum(self, fr, to):
    if not self.root:
      return 0

    fr_node = self.binary_search(self.root, fr)
    root_to_split = self.splay(fr_node)
    dumped_left, splayed_fr = self.split_left(root_to_split)

    to_node = self.binary_search(splayed_fr, to)
    root_to_split = self.splay(to_node)
    splayed_to, dumped_right = self.split_right(root_to_split)

    result = splayed_to.sum
    self.merge(dumped_left, self.merge(splayed_to, dumped_right))
    return result


def test(i):
  n, *data = open(f'./tests/{i}').readlines()
  result = []
  spt = SplayTree()
  last_sum_result = 0

  for d in data:
    op, *num = d.split()
    # print(d)
    if len(num) == 1:
      num = (int(num[0]) + last_sum_result) % MODULO
    else:
      fr, to = list(map(lambda x: (int(x) + last_sum_result) % MODULO, num))
    if op == '+':
      spt.insert(num)
    if op == '-':
      spt.delete(num)
    if op == '?':
      result.append('Found' if spt.find(num) else 'Not found')
    if op == 's':
      last_sum_result = spt.range_sum(fr, to)
      result.append(last_sum_result)

  output = open(f'./tests/{i}.a').readlines()
  output = [o.split('\n')[0] for o in output]
  result = [str(r) for r in result]
  # print(output)
  print(result)
  assert result == output


if __name__ == '__main__':
  for i in range(2, 7):
    print(i)
    test(i)
  # n = int(stdin.readline())
  # spt = SplayTree()
  # last_sum_result = 0
  # for i in range(n):
  #   line = stdin.readline().split()
  #   if line[0] == '+':
  #     x = int(line[1])
  #     spt.insert((x + last_sum_result) % MODULO)
  #   elif line[0] == '-':
  #     x = int(line[1])
  #     spt.delete((x + last_sum_result) % MODULO)
  #   elif line[0] == '?':
  #     x = int(line[1])
  #     print('Found' if spt.find((x + last_sum_result) % MODULO) else 'Not found')
  #   elif line[0] == 's':
  #     l = int(line[1])
  #     r = int(line[2])
  #     res = spt.range_sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
  #     print(res)
  #     last_sum_result = res % MODULO