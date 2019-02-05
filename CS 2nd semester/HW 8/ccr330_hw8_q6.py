class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item, parent=None, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent

        def disconnect(self):
            self.item = None
            self.left = None
            self.right = None
            self.parent = None



    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return (self.size)

    def is_empty(self):
        return (len(self) == 0)

    # raise exception if key is not in tree
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if(node is None):
            raise KeyError(str(key) + " is not found")
        else:
            return node.item.value

    # return None if key doesnt exist, or the node containing key, if it does
    def subtree_find(self, curr_root, key):
        if(curr_root is None):
            return None
        else:
            if(curr_root.item.key == key):
                return curr_root
            elif(key < curr_root.item.key):
                return self.subtree_find(curr_root.left, key)
            else:
                return self.subtree_find(curr_root.right, key)

    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if(node is not None):
            node.item.value = value
        else:
            self.subtree_insert(key, value)

    # assumes key is not in tree
    #def subtree_insert_recursive(self, curr_root, key, value):

    def subtree_insert(self, key, value=None):
        entry = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(entry)

        if (self.root is None):
            self.root = new_node
            self.size += 1
        else:
            parent = self.root
            if (key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right

            while(curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right

            new_node.parent = parent
            if(key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node

            self.size += 1
        
    # raises an exception if key is not in tree
    def __delitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            self.subtree_delete(self.root, key)

    # assums that key is in tree + returns value associated to key
    def subtree_delete(self, curr_root, key):
        node_to_delete = self.subtree_find(curr_root, key)
        value = node_to_delete.item.value
        num_children = self.num_children(node_to_delete)

        if(node_to_delete is self.root):
            if(num_children == 0):
                self.root = None
                self.size -= 1
                node_to_delete.disconnect()

            elif (num_children == 1):
                if(self.root.left is not None):
                    child = self.root.left
                else:
                    child = self.root.right
                self.root = child
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: # num_children == 2
                max_of_left = self.max_in_subtree(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if(num_children == 0):
                parent = node_to_delete.parent
                if (parent.left is node_to_delete):
                    parent.left = None
                else:
                    parent.right = None

                self.size -= 1
                node_to_delete.disconnect()

            elif(num_children == 1):
                parent = node_to_delete.parent
                if (node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                self.size -= 1
                node_to_delete.disconnect()

            else: # num_children == 2
                max_of_left = self.max_in_subtree(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    def num_children(self, node):
        count = 0
        if (node.left is not None):
            count += 1
        if (node.right is not None):
            count += 1
        return count

    def max_in_subtree(self, curr_root):
        node = curr_root
        while(node.right is not None):
            node = node.right
        return node

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)
            
    def get_ith_smallest(self, i):
        return self._ithsmallest(self.root, i)
        
    def _ithsmallest(self, root, k):
        lst = []
        curr = root
        x = 0
        while lst or curr:
            if curr:
                lst.append(curr)
                curr = curr.left
            else:
                curr = lst.pop()
                x += 1
                if x == k:
                    return curr.item
                curr = curr.right

bst = BinarySearchTreeMap()
bst[7] = None 
bst[5] = None 
bst[1] = None 
bst[14] = None 
bst[10] = None 
bst[3] = None 
bst[9] = None 
bst[13] = None 
print(bst.get_ith_smallest(3))