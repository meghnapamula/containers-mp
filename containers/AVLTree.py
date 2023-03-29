from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree():

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if not node:
            return True
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        a = AVLTree._is_avl_satisfied(node.left)
        b = AVLTree._is_avl_satisfied(node.right)
        return a and b

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        '''
        if node.right:
            q = Node(node.right.value)
            q.left = Node(node.value)
            q.right = node.right.right
            q.left.left = node.left
            q.left.right = node.right.left
            return q
        else:
            return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        '''
        if node.left:
            d = Node(node.value)
            d.right = node.right
            d.left = node.left.right
            q = Node(node.left.value)
            q = node.left.left
            q.right = d
        else:
            q = node
        return q

    def insert(self, value):
        '''
        FIXME:
        Implement this function.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    def insert_list(self, xs):
        '''
        Repeatedly call the insert method.
        '''
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        '''
        helper function
        '''
        if not node:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        balance = AVLTree._balance_factor(node)
        if balance > 1:
            if value < node.left.value:
                node = AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
        elif balance < -1:
            if value > node.right.value:
                node = AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        '''
        balance = AVLTree._balance_factor(node)
        right = AVLTree._balance_factor(node.right)
        left = AVLTree._balance_factor(node.left)
        if balance < -1:
            if right > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        elif balance > 1:
            if left < 0:
                node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        else:
            return node
