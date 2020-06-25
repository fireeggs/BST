# BST

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties −

- The value of the key of the left sub-tree is less than the value of its parent (root) node's key.

- The value of the key of the right sub-tree is greater than or equal to the value of its parent (root) node's key.

Thus, BST divides all its sub-trees into two segments; the left sub-tree and the right sub-tree and can be defined as −

```
left_subtree (keys) < node (key) ≤ right_subtree (keys)
```

## 1. Representation
BST is a collection of nodes arranged in a way where they maintain BST properties. Each node has a key and an associated value. While searching, the desired key is compared to the keys in BST and if found, the associated value is retrieved.

## 2. Node
Define a node class having some data, references to it's left, right child and parent nodes.
```
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
```

## 3. Binary Search Tree
Define a BST class having a root node. 
```
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
```

## 4. Test BST
test_bst.py is built to verify all functions from bst.py such as search, insert, delete, pre-order, in-order, post-order traversal, etc. Generally, it covers empty tree, simple tree, right and left tree, huge tree test case

```
if __name__ == '__main__':
    # go!
    runner = unittest.TextTestRunner()
    runner.run(empty_tree_suite())
    runner.run(sample_suite())
    runner.run(right_tree_suite())
    runner.run(left_tree_suite())
    runner.run(one_node_suite())
    runner.run(huge_suite())
```
