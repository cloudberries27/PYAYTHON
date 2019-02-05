class LinkedBinaryTree:

    class Node:
        def __init__(self, data, parent=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent


    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):    
        return (len(self) == 0)

    def subtree_count(self, curr_root):
        if(curr_root is None):
            return 0
        else:
            left_count = self.subtree_count(curr_root.left)
            right_count = self.subtree_count(curr_root.right)
            return left_count + right_count + 1


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, curr_root):
        if(curr_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(curr_root.left)
            right_sum = self.subtree_sum(curr_root.right)
            return left_sum + right_sum + curr_root.data

    def max(self):
        
        
    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, curr_root):
        if(curr_root.left is None and curr_root.right is None):
            return 0
        elif(curr_root.left is None):
            return 1 + self.subtree_height(curr_root.right)
        elif(curr_root.right is None):
            return 1 + self.subtree_height(curr_root.left)
        else:
            left_height = self.subtree_height(curr_root.left)
            right_height = self.subtree_height(curr_root.right)
            return 1 + max(left_height, right_height)


def create_subtree(data, left_child=None, right_child=None):
    subtree_root = LinkedBinaryTree.Node(data, None, left_child, right_child)
    if (left_child is not None):
        left_child.parent = subtree_root
    if  (right_child is not None):
        right_child.parent = subtree_root
    return subtree_root