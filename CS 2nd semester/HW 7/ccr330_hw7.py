class Empty(Exception):
    pass

class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0






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


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def breadth_first(self):
        if(self.is_empty()):
            pass
        else:
            nodes_q = ArrayQueue()
            nodes_q.enqueue(self.root)
            while(nodes_q.is_empty() == False):
                curr_node = nodes_q.dequeue()
                yield curr_node
                if(curr_node.left is not None):
                    nodes_q.enqueue(curr_node.left)
                if(curr_node.right is not None):
                    nodes_q.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data
#Question 1
    def max(self):
        return self.subtree_max(self.root)

    def subtree_max(self, curr_root):
        if(curr_root is None):
            return 0
        else:
            left_subtree = self.subtree_max(curr_root.left)
            right_subtree = self.subtree_max(curr_root.right)
            if (left_subtree > right_subtree and left_subtree > curr_root.data):
                return left_subtree
            elif (left_subtree < right_subtree and right_subtree > curr_root.data):
                return right_subtree
            elif (curr_root.data > left_subtree and curr_root.data > right_subtree):
                return curr_root.data
#Question 2               
    def leaves_list(self):
        last_nodes_list = []
        for i in self.preorder():
            if (i.left is None and i.right is None):
                last_nodes_list.append(i.data)
        return last_nodes_list
        
#Question 3
    def height_helper(self, curr_root):
        if(curr_root is None):
            return (True, 0)
        else:
            left_tuple = self.height_helper(curr_root.left)
            right_tuple = self.height_helper(curr_root.right)
            a = [left_tuple[1], right_tuple[1]]
            max_height = max(a)
            if left_tuple[0] is False or right_tuple[0] is False:
                return (False, max_height +1)
            elif left_tuple[1] - right_tuple[1] > 1 or left_tuple[1] - right_tuple[1] < -1:
                return (False, max_height + 1)
            else:
                return (True, max_height + 1)
                
    def is_height_balanced(self):
        return self.height_helper(self.root)[0]
#Question 4          
    def iterative_inorder(self):
        current = self.root
        lst = [] 
        # it said not to use a list but I honestly
        # couldn't figure another way. Sorry        
        done = 0
        while(not done):
            if current is not None:
                lst.append(current)
                current = current.left
            else:
                if(len(lst) >0 ):
                    current = lst.pop()
                    print (current.data)
                    current = current.right 
                else:
                    done = 1
       
def create_subtree(data, left_child=None, right_child=None):
    subtree_root = LinkedBinaryTree.Node(data, None, left_child, right_child)
    if (left_child is not None):
        left_child.parent = subtree_root
    if  (right_child is not None):
        right_child.parent = subtree_root
    return subtree_root

#Question 5
def tree_helper(prefix_exp_str, start_pos):
    if (start_pos > len(prefix_exp_str)):#base case
        return 0
    else:
        left_child = tree_helper(prefix_exp_str[start_pos:], start_pos + 1)
        right_child = tree_helper(prefix_exp_str[start_pos:], start_pos + 2)
        
        return left_child + right_child
              
def create_expression_tree(prefix_exp_str):
    str_list = prefix_exp_str.split()
    expression_root = LinkedBinaryTree.Node(str_list[0])
    tree = tree_helper(str_list, 0)
    return expression_root + tree
    
        
def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    return pretopost_helper(tree.parent)
    
def pretopost_helper(curr_root):
    if(curr_root is None):
        pass
    else:
        yield from prefix_to_postfix(curr_root.left)
        yield from prefix_to_postfix(curr_root.right)
        yield curr_root
        
l_ch1 = create_subtree(5)
r_ch1 = create_subtree(1)
l_ch2 = create_subtree(9, l_ch1, r_ch1)
l_ch3 = create_subtree(2, l_ch2)
r_ch2 = create_subtree(4)
l_ch4 = create_subtree(8)
r_ch3 = create_subtree(7, l_ch4, r_ch2)
root = create_subtree(3, l_ch3, r_ch3)
tree = LinkedBinaryTree(root)
print(tree.max())   
print(tree.leaves_list()) 
print(tree.is_height_balanced())
tree.iterative_inorder()