class BinaryTree:
   class Node:
      def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

   def __init__(self):
      self.root = None

   def insert(self, value) -> None:
      if self.root is None:
            self.root = self.Node(value)
            return
      node = self.root
      while node is not None:
            if node.data > value:
               if node.left is None:
                  node.left = self.Node(value)
                  break
               else:
                  node = node.left
            if node.data < value:
               if node.right is None:
                  node.right = self.Node(value)
                  break
               else:
                  node = node.right

   def print_pos(self, node) -> None:
      if node is None:
            return
      self.print_pos(node.left)
      self.print_pos(node.right)
      if node.data.y > 0:
            print(node.data)

   def print_positive(self) -> None:
      self.print_pos(self.root)

   def print_(self, node) -> None:
      if node is None:
            return
      self.print_(node.left)
      self.print_(node.right)
      print(node.data)

   def print_tree(self) -> None:
      self.print_(self.root)

   def find_by_k(self, k) -> bool:
      if self.root is None:
            return False
      node = self.root
      while node is not None:
            if node.data == k:
               return True
            if node.data > k:
               node = node.left
            else:
               node = node.right
      return False

   def delete_node(self, node, k) -> Node or None:
      if node is None:
            return node
      if k < node.data:
            node.left = self.delete_node(node.left, k)
      elif k > node.data:
            node.right = self.delete_node(node.right, key)
      else:
            if node.left is None:
               tmp = node.right
               return tmp
            elif node.right is None:
               tmp = node.left
               return tmp

            tmp = node.right
            while tmp.left is not None:
               tmp = tmp.left
            node.data = tmp.data
            node.right = self.delete_node(node.right, tmp.data)
      return node

   # def delete_chel(self, node) -> None:
   #    if node is None:
   #          return
   #    self.delete_chel(node.left)
   #    self.delete_chel(node.right)
   #    node.left = None
   #    node.right = None
   #
   # def delete_tree(self) -> None:
   #    self.delete_chel(self.root)
   #    self.root = None

   def delete_negative(self) -> None:
      lst = [self.root]
      i = 0
      while i < len(lst):
            if lst[i].left is not None:
               lst.append(lst[i].left)
            if lst[i].right is not None:
               lst.append(lst[i].right)
            if lst[i].data.x < 0 and lst[i].data.y < 0:
               self.root = self.delete_node(self.root, lst[i].data)
            i += 1