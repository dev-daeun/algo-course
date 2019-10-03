# python3
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

ROOT_IDX = 0

def test1():
  input_ = open('tests/1')
  _, *relations = input_.readlines()
  relations = [list(map(lambda x: int(x), r.split())) for r in relations]
  tree = Tree()
  root_idx = tree.build(relations=relations)
  
  output = open('tests/1.a')
  in_result, pre_result, post_result = (o.split() for o in output.readlines())

  tree.in_order(root_idx)
  assert tree.in_order_result == list(map(lambda x: int(x), in_result))

  tree.pre_order(root_idx)
  assert tree.pre_order_result == list(map(lambda x: int(x), pre_result))

  tree.post_order(root_idx)
  assert tree.post_order_result == list(map(lambda x: int(x), post_result))

def test2():
  input_ = open('tests/2')
  _, *relations = input_.readlines()
  relations = [list(map(lambda x: int(x), r.split())) for r in relations]
  tree = Tree()
  root_idx = tree.build(relations=relations)
  
  output = open('tests/2.a')
  in_result, pre_result, post_result = (o.split() for o in output.readlines())

  tree.in_order(root_idx)
  assert tree.in_order_result == list(map(lambda x: int(x), in_result))

  tree.pre_order(root_idx)
  assert tree.pre_order_result == list(map(lambda x: int(x), pre_result))

  tree.post_order(root_idx)
  assert tree.post_order_result == list(map(lambda x: int(x), post_result))


class Vertex:
  def __init__(self, val, left, right):
    self.val = val
    self.left = None if left == -1 else left
    self.right = None if right == -1 else right

class Tree:
  def __init__(self):
    self.in_order_result = []
    self.pre_order_result = []
    self.post_order_result = []
    self.vertexs = []

  def build(self, relations):
    for r in relations:
      root_val, left, right = r
      v = Vertex(val=root_val, left=left, right=right)
      self.vertexs.append(v)  # left, right : index of vertex, not value.
    return ROOT_IDX

  def in_order(self, idx):
    if idx is None:
      return
    self.in_order(self.vertexs[idx].left)
    self.in_order_result.append(self.vertexs[idx].val)
    self.in_order(self.vertexs[idx].right)

  def pre_order(self, idx):
    if idx is None:
      return
    self.pre_order_result.append(self.vertexs[idx].val)
    self.pre_order(self.vertexs[idx].left)
    self.pre_order(self.vertexs[idx].right)

  def post_order(self, idx):
    if idx is None:
      return
    self.post_order(self.vertexs[idx].left)
    self.post_order(self.vertexs[idx].right)
    self.post_order_result.append(self.vertexs[idx].val)

def main():
  test1()
  test2()
#   n = int(sys.stdin.readline())
#   input_ = []
#   for _ in range(n):
#     input_.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
  
#   tree = Tree()
#   tree.build(input_)

#   tree.in_order(ROOT_IDX)
#   tree.pre_order(ROOT_IDX)
#   tree.post_order(ROOT_IDX)
#   print(" ".join(str(x) for x in tree.in_order_result))
#   print(" ".join(str(x) for x in tree.pre_order_result))
#   print(" ".join(str(x) for x in tree.post_order_result))

threading.Thread(target=main).start()
