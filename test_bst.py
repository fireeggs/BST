'''
    Binary Search Tree TestCase

    Verify all functions in bst.py with proper examples

    test_bst.py

    Created by Seungkyu Kim on Apr 23, 2015
    Copyright © 2015 Seungky Kim. All rights reserved. 

'''


import unittest
from bst import *


class EmptyTreeTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''Generate an empty tree to test.

        '''

        self.tree = BSTree()

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass

    def testTreeRoot(self):
        '''Verify that root is none.'''

        self.assertEqual(self.tree.root, None)

    def testHeight(self):
        '''Verify the height of the empty tree is 0.'''

        self.assertEqual(self.tree.height(), 0)

    def testSearch(self):
        '''Verify if value v exists in the tree.'''

        self.assertEqual(self.tree.search(20), None)
        self.assertEqual(self.tree.search(5), None)

    def testRange(self):
        '''Verify the appropriate list of Node objects between two nodes.'''

        self.assertEqual(self.tree.range(2, 5), [])
        self.assertEqual(self.tree.range(12, 20), [])

    def testDelete(self):
        pass


class SampleTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''Generate a tree to test.
                9
                    8
            7
        5
            3
                2
        '''

        self.tree = BSTree()
        for val in [5, 7, 3, 2, 9, 8]:
            self.tree.insert(val)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass

    def testTreeRoot(self):
        '''Verify that 5 is the root of the tree.'''

        self.assertEqual(self.tree.root.value, 5)

    def testTreeLeft(self):
        '''Verify that 3 is the left child of the root'''

        self.assertEqual(self.tree.root.left.value, 3)
        self.assertEqual(self.tree.root.left.is_left_child(), True)
        self.assertEqual(self.tree.root.right.is_left_child(), False)

    def testTreeRight(self):
        '''Verify that 7 is the right child of the tree'''

        self.assertEqual(self.tree.root.right.value, 7)
        self.assertEqual(self.tree.root.right.is_right_child(), True)
        self.assertEqual(self.tree.root.left.is_right_child(), False)

    def testTreeParent(self):
        '''Verify 7 is a parent of its child, 9.'''

        self.assertEqual(self.tree.root.right.right.parent.value, 7)

    def testLeaf(self):
        '''Verify the leaves of the tree.'''

        self.assertEqual(self.tree.root.left.left.is_leaf(), True)
        self.assertEqual(self.tree.root.right.right.left.is_leaf(), True)
        self.assertEqual(self.tree.root.right.right.is_leaf(), False)

    def testHeight(self):
        '''Verify the height of the tree is 4.'''

        self.assertEqual(self.tree.root.height(), 4)

    def testDepth(self):
        '''Verify the depth of the tree according to each node.'''

        self.assertEqual(self.tree.root.depth(), 1)
        self.assertEqual(self.tree.root.right.right.left.depth(), 4)
        self.assertEqual(self.tree.root.left.depth(), 2)

    def testSearch(self):
        '''Verify if value v exists in the tree.'''

        self.assertEqual(self.tree.search(20), None)
        self.assertEqual(self.tree.search(5), self.tree.root)
        self.assertEqual(self.tree.search(8), self.tree.root.right.right.left)

    def testRange(self):
        '''Verify the appropriate list of Node objects between two nodes.'''

        self.assertEqual(self.tree.range(2, 5), [2, 3, 5])
        self.assertEqual(self.tree.range(2, 2), [])
        self.assertEqual(self.tree.range(2, 8), [2, 3, 5, 7])
        self.assertEqual(self.tree.range(5, 9), [5, 7, 8, 9])

    def testDelete(self):
        pass

    def testInorderPredecessor(self):
        '''Verify the appropriate inorder predecessor of the given node.'''

        self.assertEqual(in_order_predecessor(self.tree.root).value, 3)
        self.assertEqual(in_order_predecessor(self.tree.root.left.left), None)
        self.assertEqual(in_order_predecessor(self.tree.root.right.right.left)\
                         .value, 7)

    def testInorderSuccessor(self):
        '''Verify the appropriate inorder successor of the given node.'''

        self.assertEqual(in_order_successor(self.tree.root.left).value, 5)
        self.assertEqual(in_order_successor(self.tree.root).value, 7)
        self.assertEqual(in_order_successor(self.tree.root.right.right), None)


class RightTreeTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''test a tree has only right subtree from root.
                9
                    8
            7
        5

        '''

        self.tree = BSTree()
        for val in [5, 7, 9, 8]:
            self.tree.insert(val)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass

    def testTreeRoot(self):
        '''Verify that 5 is the root of the tree.'''

        self.assertEqual(self.tree.root.value, 5)

    def testTreeLeft(self):
        '''Verify that 7 is the left child of the tree'''

        self.assertEqual(self.tree.root.right.is_left_child(), False)

    def testTreeRight(self):
        '''Verify that 7 is the right child of the tree'''

        self.assertEqual(self.tree.root.right.is_right_child(), True)

    def testTreeParent(self):
        '''Verify 7 is a parent of its child, 9.'''

        self.assertEqual(self.tree.root.right.right.parent.value, 7)
        self.assertEqual(self.tree.root.parent, None)

    def testLeaf(self):
        '''Verify that only 8 is a leaf of the tree.'''

        self.assertEqual(self.tree.root.right.right.left.is_leaf(), True)
        self.assertEqual(self.tree.root.right.right.is_leaf(), False)

    def testHeight(self):
        '''Verify the height of the tree.'''

        self.assertEqual(self.tree.root.height(), 4)
        self.assertEqual(self.tree.root.right.right.left.height(), 1)

    def testDepth(self):
        '''Verify the depth of the tree according to each node.'''

        self.assertEqual(self.tree.root.depth(), 1)
        self.assertEqual(self.tree.root.right.right.left.depth(), 4)
        self.assertEqual(self.tree.root.right.depth(), 2)

    def testSearch(self):
        '''Verify if value v exists in the tree.'''

        self.assertEqual(self.tree.search(20), None)
        self.assertEqual(self.tree.search(5), self.tree.root)
        self.assertEqual(self.tree.search(8), self.tree.root.right.right.left)

    def testRange(self):
        '''Verify the appropriate list of Node objects between two nodes.'''

        self.assertEqual(self.tree.range(2, 5), [5])
        self.assertEqual(self.tree.range(5, 5), [5])
        self.assertEqual(self.tree.range(2, 8), [5, 7])
        self.assertEqual(self.tree.range(5, 9), [5, 7, 8, 9])

    def testDelete(self):
        pass

    def testInorderPredecessor(self):
        '''Verify the appropriate inorder predecessor of the given node.'''

        self.assertEqual(in_order_predecessor(self.tree.root.right.right.left)\
                         .value, 7)
        self.assertEqual(in_order_predecessor(self.tree.root), None)
        self.assertEqual(in_order_predecessor(self.tree.root.right.right)\
                         .value, 8)

    def testInorderSuccessor(self):
        '''Verify the appropriate inorder successor of the given node.'''

        self.assertEqual(in_order_successor(self.tree.root.right.right.left)\
                         .value, 9)
        self.assertEqual(in_order_successor(self.tree.root).value, 7)
        self.assertEqual(in_order_successor(self.tree.root.right.right), None)


class LeftTreeTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''test a tree has only left subtree from root.

        5
            4
                    3
                2

        '''

        self.tree = BSTree()
        for val in [5, 4, 2, 3]:
            self.tree.insert(val)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass

    def testTreeRoot(self):
        '''Verify that 5 is the root of the tree.'''

        self.assertEqual(self.tree.root.value, 5)

    def testTreeLeft(self):
        '''Verify that 4 is the left child of the root'''

        self.assertEqual(self.tree.root.left.value, 4)
        self.assertEqual(self.tree.root.left.is_left_child(), True)

    def testTreeRight(self):
        '''Verify the right child of the root'''

        self.assertEqual(self.tree.root.right, None)
        self.assertEqual(self.tree.root.left.is_right_child(), False)

    def testTreeParent(self):
        '''Verify 4 is a parent of its child, 2.'''

        self.assertEqual(self.tree.root.left.left.parent.value, 4)
        self.assertEqual(self.tree.root.parent, None)

    def testLeaf(self):
        '''Verify that only 3 is a leaf of the tree.'''

        self.assertEqual(self.tree.root.left.left.right.is_leaf(), True)
        self.assertEqual(self.tree.root.left.is_leaf(), False)

    def testHeight(self):
        '''Verify the height of the tree is 4.'''

        self.assertEqual(self.tree.root.height(), 4)
        self.assertEqual(self.tree.root.left.left.right.height(), 1)

    def testDepth(self):
        '''Verify the depth of the tree according to each nodes.'''

        self.assertEqual(self.tree.root.depth(), 1)
        self.assertEqual(self.tree.root.left.left.right.depth(), 4)
        self.assertEqual(self.tree.root.left.depth(), 2)

    def testSearch(self):
        '''Verify if value v exists in the tree.'''

        self.assertEqual(self.tree.search(20), None)
        self.assertEqual(self.tree.search(5), self.tree.root)
        self.assertEqual(self.tree.search(3), self.tree.root.left.left.right)

    def testRange(self):
        '''Verify the appropriate list of Node objects between two nodes.'''

        self.assertEqual(self.tree.range(2, 5), [2, 3, 4, 5])
        self.assertEqual(self.tree.range(2, 2), [])
        self.assertEqual(self.tree.range(5, 5), [5])
        self.assertEqual(self.tree.range(4, 5), [4, 5])

    def testDelete(self):
        pass

    def testInorderPredecessor(self):
        '''Verify the appropriate inorder predecessor of the given node.'''

        self.assertEqual(in_order_predecessor(self.tree.root.left.left.right)\
                         .value, 2)
        self.assertEqual(in_order_predecessor(self.tree.root).value, 4)
        self.assertEqual(in_order_predecessor(self.tree.root.left.left), None)

    def testInorderSuccessor(self):
        '''Verify the appropriate inorder successor of the given node.'''

        self.assertEqual(in_order_successor(self.tree.root.left.left).value, 3)
        self.assertEqual(in_order_successor(self.tree.root), None)
        self.assertEqual(in_order_successor(self.tree.root.left.left.right)\
                         .value, 4)


class OneNodeTreeTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''test a tree has only right subtree from root.


            7

        '''

        self.tree = BSTree()
        self.tree.insert(7)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass

    def testTreeRoot(self):
        '''Verify that 5 is the root of the tree.'''

        self.assertEqual(self.tree.root.value, 7)

    def testTreeLeft(self):
        '''Verify that there is not left child of the tree'''

        self.assertEqual(self.tree.root.left, None)
        self.assertEqual(self.tree.root.is_left_child(), False)

    def testTreeRight(self):
        '''Verify that there is not right child of the tree'''

        self.assertEqual(self.tree.root.right, None)
        self.assertEqual(self.tree.root.is_right_child(), False)

    def testTreeParent(self):
        '''Verify that there is no parent for the root.'''

        self.assertEqual(self.tree.root.parent, None)

    def testLeaf(self):
        '''Verify that 7 is a leaf.'''

        self.assertEqual(self.tree.root.is_leaf(), True)

    def testHeight(self):
        '''Verify the height of the tree.'''

        self.assertEqual(self.tree.root.height(), 1)

    def testDepth(self):
        '''Verify the depth of the tree.'''

        self.assertEqual(self.tree.root.depth(), 1)

    def testSearch(self):
        '''Verify if value v exists in the tree.'''

        self.assertEqual(self.tree.search(20), None)
        self.assertEqual(self.tree.search(7), self.tree.root)

    def testRange(self):
        '''Verify the appropriate list of Node objects between two nodes.'''

        self.assertEqual(self.tree.range(2, 5), [])
        self.assertEqual(self.tree.range(5, 7), [7])
        self.assertEqual(self.tree.range(7, 7), [7])

    def testDelete(self):
        pass

    def testInorderPredecessor(self):
        '''Verify the appropriate inorder predecessor of the given node.'''

        self.assertEqual(in_order_predecessor(self.tree.root), None)

    def testInorderSuccessor(self):
        '''Verify the appropriate inorder successor of the given node.'''

        self.assertEqual(in_order_successor(self.tree.root), None)


class HugeTreeTestCase(unittest.TestCase):
    '''Test values in several bases.'''

    def setUp(self):
        '''test a tree has only right subtree from root.
                          77
                      70
                  50
                      49
              22
                  21
          20
                      14
                  12
                          11
                      10
              8
                      5
                  4
                          2
                      1
        '''

        self.tree = BSTree()
        for val in [20, 8, 22, 4, 12, 21, 50, 10, 14, 11, 49, 1, 70, 2, 5, 77]:
            self.tree.insert(val)

    def tearDown(self):
        '''Perform cleanup actions.'''

        pass

    def testTreeRoot(self):
        '''Verify that 20 is the root of the tree.'''

        self.assertEqual(self.tree.root.value, 20)

    def testTreeLeft(self):
        '''Verify that 8 is the left child of the tree.'''

        self.assertEqual(self.tree.root.left.value, 8)
        self.assertEqual(self.tree.root.left.is_left_child(), True)
        self.assertEqual(self.tree.root.right.is_left_child(), False)

    def testTreeRight(self):
        '''Verify that 22 is the right child of the tree'''

        self.assertEqual(self.tree.root.right.value, 22)
        self.assertEqual(self.tree.root.right.is_right_child(), True)
        self.assertEqual(self.tree.root.left.is_right_child(), False)

    def testTreeParent(self):
        '''Verify the parent of the child.'''

        self.assertEqual(self.tree.root.parent, None)
        self.assertEqual(self.tree.root.left.left.right.parent.value, 4)
        self.assertEqual(self.tree.root.right.right.parent.value, 22)
        self.assertEqual(self.tree.root.right.parent.value, 20)

    def testLeaf(self):
        '''Verify the leaves of the tree.'''

        self.assertEqual(self.tree.root.right.left.is_leaf(), True)
        self.assertEqual(self.tree.root.left.right.left.right.is_leaf(), True)
        self.assertEqual(self.tree.root.left.left.left.right.is_leaf(), True)
        self.assertEqual(self.tree.root.left.left.right.is_leaf(), True)
        self.assertEqual(self.tree.root.left.right.left.right.is_leaf(), True)
        self.assertEqual(self.tree.root.left.right.right.is_leaf(), True)
        self.assertEqual(self.tree.root.right.right.left.is_leaf(), True)
        self.assertEqual(self.tree.root.right.right.right.right\
                         .is_leaf(), True)
        self.assertEqual(self.tree.root.right.right.is_leaf(), False)

    def testHeight(self):
        '''Verify the height of the tree.'''

        self.assertEqual(self.tree.root.height(), 5)

    def testDepth(self):
        '''Verify the depth of the tree according to each node.'''

        self.assertEqual(self.tree.root.depth(), 1)
        self.assertEqual(self.tree.root.right.right.right.right.depth(), 5)
        self.assertEqual(self.tree.root.left.depth(), 2)
        self.assertEqual(self.tree.root.left.right.left.depth(), 4)

    def testSearch(self):
        '''Verify if value v exists in the tree.'''

        self.assertEqual(self.tree.search(100), None)
        self.assertEqual(self.tree.search(20), self.tree.root)
        self.assertEqual(self.tree.search(50), self.tree.root.right.right)

    def testRange(self):
        '''Verify the appropriate list of Node objects between two nodes.'''

        self.assertEqual(self.tree.range(11, 49), [20, 21, 22])
        self.assertEqual(self.tree.range(20, 77), [20, 21, 22, 49, 50, 70, 77])
        self.assertEqual(self.tree.range(2, 14), [])
        self.assertEqual(self.tree.range(8, 22), \
                         [8, 10, 11, 12, 14, 20, 21, 22])

    def testDelete(self):
        pass

    def testInorderPredecessor(self):
        '''Verify the appropriate inorder predecessor of the given node.'''

        self.assertEqual(in_order_predecessor(self.tree.root).value, 14)
        self.assertEqual(in_order_predecessor(self.tree.root.right).value, 21)
        self.assertEqual(in_order_predecessor(self.tree.root.left.\
                                              left.left), None)
        self.assertEqual(in_order_predecessor(self.tree.root.right.right.left)\
                         .value, 22)
        self.assertEqual(in_order_predecessor(self.tree.root.left.right.right)\
                         .value, 12)
        self.assertEqual(in_order_predecessor(self.tree.root.left.left)\
                         .value, 2)

    def testInorderSuccessor(self):
        '''Verify the appropriate inorder successor of the given node.'''

        self.assertEqual(in_order_successor(self.tree.root).value, 21)
        self.assertEqual(in_order_successor(self.tree.root.right).value, 49)
        self.assertEqual(in_order_successor(self.tree.root.right.right.left)\
                         .value, 50)
        self.assertEqual(in_order_successor(self.tree.root.left.right.right)\
                         .value, 20)
        self.assertEqual(in_order_successor(self.tree.root.left.left)\
                         .value, 5)
        self.assertEqual(in_order_successor(self.tree.root.right.right.\
                                            right.right), None)


def empty_tree_suite():
    """Return the sample test suite."""

    return unittest.TestLoader().loadTestsFromTestCase(EmptyTreeTestCase)


def sample_suite():
    """Return the sample test suite."""

    return unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)


def right_tree_suite():
    """Return the righttree test suite."""

    return unittest.TestLoader().loadTestsFromTestCase(RightTreeTestCase)


def left_tree_suite():
    """Return the lefttree test suite."""

    return unittest.TestLoader().loadTestsFromTestCase(LeftTreeTestCase)


def one_node_suite():
    '''Return the one node test suite.'''

    return unittest.TestLoader().loadTestsFromTestCase(OneNodeTreeTestCase)


def huge_suite():
    '''Return the huge nodes test suite.'''

    return unittest.TestLoader().loadTestsFromTestCase(HugeTreeTestCase)

if __name__ == '__main__':
    # go!
    runner = unittest.TextTestRunner()
    runner.run(empty_tree_suite())
    runner.run(sample_suite())
    runner.run(right_tree_suite())
    runner.run(left_tree_suite())
    runner.run(one_node_suite())
    runner.run(huge_suite())
