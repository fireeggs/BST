'''
    Binary Search Tree

    The BTNode (which stands for "Binary Tree Node") class represents a node in a binary tree. 
    It has three instance variables: left, right and value. 
    The first two contain the memory addresses of other nodes or are set to None,
    if the node has no left or right subtree, respectively

    bst.py

    Created by Seungkyu Kim on Apr 23, 2015
    Copyright © 2015 Seungky Kim. All rights reserved. 
    
'''


class BTNode:
    '''A generic binary tree node that keeps a value and pointers to
    a left child, right child and parent.'''

    def __init__(self, v, p=None):
        '''(BTNode, object, BTNode) -> NoneType
        A new BTNode with value v, no left or right
        children and parent p. p is None by default.'''

        self.value = v
        self.left = None
        self.right = None
        self.parent = p

    def __str__(self):
        '''(BTNode) -> str
        Return the string representation of self.
        This method is called by print() and str()
        NOTE: This method is complete.'''

        return str(self.value)

    def __repr__(self):
        '''(BTNode) -> str
        Return the internal string representation of self.
        This method is called when a list of BTNodes is
        printed.
        NOTE: This method is complete.'''

        return "BTNode: {}".format(self.value)

    def set_right(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the right child of self.
        Set bidirectional links correctly.'''

        self.right = n
        n.parent = self

    def set_left(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the left child of self.
        Set bidirectional links correctly.'''

        self.left = n
        n.parent = self

    def is_left_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self is
        the left child of its parent.'''

        return bool(self.parent) and self.parent.left == self

    def is_right_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self is
        the right child of its parent.'''

        return bool(self.parent) and self.parent.right == self

    def is_leaf(self):
        '''(BTNode) -> bool
        Return True iff self is a leaf node.'''

        return not self.right and not self.left

    def height(self):
        '''(BTNode) -> int
        Return the height of self. Height is defined as the length of the
        longest path by number of nodes from self to a leaf.
        The height of a leaf node is 1.'''

        if not self:
            return 0
        elif self.is_leaf():
            return 1
        else:
            if not self.left:
                return self.right.height() + 1
            elif not self.right:
                return self.left.height() + 1
            else:
                left = self.left.height()
                right = self.right.height()
                return 1 + max(left, right)

    def depth(self):
        '''(BTNode) -> int
        Return the depth of self. Depth is defined as the length of the
        path by number of nodes from the root of the tree to self.
        The depth of a root node is 1.'''

        if not self.parent:
            return 1
        else:
            temp_parent = self.parent.depth()
            return 1 + temp_parent


class BSTree:
    '''A Binary Search Tree that conforms to the BST property at every step.
    The BST property states that for every node with value k, its left child
    is a (possibly empty) BST with values strictly less than k and its right
    child is a (possibly empty) BST with values strictly greater than k.'''

    def __init__(self, root=None):
        '''(BSTree, BTNode) -> NoneType
        Create a new BST with an optional root.
        NOTE: This method is complete.'''

        self.root = root

    def print_tree(self):
        '''(BSTree) -> NoneType
        Print tree recursively (used for testing purposes)
        NOTE: This method is complete.'''

        _print_tree(self.root, 1)

    def insert(self, v):
        '''(BSTree, object) -> NoneType
        Insert a new node with value v into self. Do not duplicate values.
        NOTE: This method is complete.'''

        if not self.root:
            self.root = BTNode(v)
            return
        _insert(self.root, v)

    def height(self):
        '''(BSTree) -> int
        Return the height of this tree.'''
        
        if not self.root:
            return 0
        return self.root.height()

    def search(self, v):
        '''(BSTree, object) -> BTNode
        Return BTNode with value v if it exists in the tree. Return None if no
        such node exists. Assume unique node values.
        NOTE: This method is complete.'''

        return _search(self.root, v)

    def range(self, v_start, v_end):
        '''(BSTree, object, object) -> list
        Return a list of Node objects with values between v_start and
        v_end inclusive. Assume v_start and v_end can be ordered and
        v_start <= v_end. v_start and v_end may not be values that
        exist in the tree.
        NOTE: This method is complete.'''

        return _range(self.root, v_start, v_end)

    def delete(self, v):
        '''(BSTree, object) -> NoneType
        Delete node with value v from self. Change root if required.
        NOTE: This method is complete.'''

        self.root = _delete(self.root, v)


## HELPER RECURSIVE FUNCTIONS

def _print_tree(root, depth):
    '''(BTNode, int) -> NoneType
    Print the left subtree of root, print root preceded by four spaces for
    every unit of depth, then print the right subtree of root.
    depth is the depth of root.
    NOTE: This function is complete.'''

    if root is None:
        return
    _print_tree(root.right, depth + 1)
    print("    " * (depth - 1) + str(root))
    _print_tree(root.left, depth + 1)


def _insert(root, v):
    '''(BTNode, obj) -> NoneType
    Insert a new node with value v into BST rooted at root.
    Do not allow duplicates.
    NOTE: This function is complete.'''

    if root.value == v:
        return
    if v < root.value:
        if root.left:
            _insert(root.left, v)
        else:
            root.set_left(BTNode(v))
    elif v > root.value:
        if root.right:
            _insert(root.right, v)
        else:
            root.set_right(BTNode(v))

def _search(root, v):
    '''(BTNode, object) -> BTNode
    Return BTNode with value v if it exists in subtree rooted at
    root. Return None if no such BTNode exists.'''

    if not root:
        return
    elif root.value == v:
        return root
    else:
        if v < root.value:
            return _search(root.left, v)
        elif v > root.value:
            return _search(root.right, v)

def _range(root, v_start, v_end):
    '''(BTNode, int, int) -> list
    Return an in-order list of BTNodes that have values between
    v_start and v_end, inclusive in subtree rooted at root.'''

    bt_list = []
    if not root:
        return []
    elif root.value not in range(v_start, v_end + 1 ):
        if root.is_leaf() and (root.value in range(v_start, v_end+1)):
            bt_list.extend([root.value])
    else:
        if root.value > v_start:
            if root.left:
                bt_list.extend(_range(root.left, v_start, v_end))
        bt_list.extend([root.value])
        if root.value < v_end:
            if root.right:
                bt_list.extend(_range(root.right, v_start, v_end))
    return bt_list

    
def _delete(root, v):
    '''(BTNode, object) -> BTNode
    Delete BTNode with >>> value v from subtree rooted at root.
    Return root of subtree. Do nothing if value doesn't exist in subtree.'''
    
    if root == None:
        return None
    elif root.value == v:
        if root.is_leaf():
            return None
        elif root.left and not root.right: # only left subtree exists
            return root.left
        elif root.right and not root.left: # only right subtree exists
            return root.right
        elif root.right and root.left: # right and left subtrees exist
            if root.left.height() > root.right.height():
                return in_order_predecessor(root)
            else:
                return in_order_successor(root)
    else:
        if v < root.value:
            return root.set_left(_delete(root.left, v))
        elif v > root.value:
            return root.set_right(_delete(root.right, v))
        

## NEIGHBOURS FUNCTIONS

def in_order_predecessor(node):
    '''(BTNode) -> BTNode
    Return the in-order predecessor of node.
    Return None if node is leftmost.'''

    if node.left:
        node = node.left
        while node.right:
            node = node.right
        return node
    else:
        while not node.is_right_child():
            if node.parent == None:
                return None
            node = node.parent
        if node.is_right_child():
            return node.parent
        else:
            return node.parent.parent

def in_order_successor(node):
    '''(BTNode) -> BTNode
    Return the in-order successor of node.
    Return None if node is rightmost.'''

    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        while not node.is_left_child():
            if node.parent == None:
                return None
            node = node.parent
        if node.is_left_child():
            return node.parent
        else:
            return node.parent.parent


if __name__ == '__main__':

    t = BSTree()
    #for i in [5, 6, 7, 8]:
        #t.insert(i)
    t.print_tree()
    t.height()
    #print(in_order_predecessor(t.root))
    #print(in_order_successor(t.root))