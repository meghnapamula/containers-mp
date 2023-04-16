from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    '''

    def __init__(self, xs=None):
        '''
        '''
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __iter__(self):
        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.value
            node = node.right

    def __repr__(self):
        '''
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        '''
        then compare those sorted lists for equality.
        '''
        return self.to_list('inorder') == t2.to_list('inorder')

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        '''
        ret = True
        if node.left:
            if node.value > BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False

        if node.right:
            if node.value < BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        '''
        if self.root:
            self._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        '''
        helper function
        '''
        if node.value < value:
            if node.right is not None:
                BST._insert(node.right, value)
            else:
                node.right = Node(value)
        elif node.value > value:
            if node.left is not None:
                BST._insert(node.left, value)
            else:
                node.left = Node(value)

    def insert_list(self, xs):
        '''
        '''
        for x in xs:
            self.insert(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        FIXME:
        Implement this function.
        '''
        if self.root:
            return BST._find(value, self.root)
        return False

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return False
        elif node.value == value:
            return True
        elif node.value < value:
            return BST._find(value, node.right)
        else:
            return BST._find(value, node.left)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        This is a helper function for find_smallest and
        not intended to be called directly by the user.
        '''
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        '''
        This is a helper function for find_smallest and
        not intended to be called directly by user
        '''
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        '''
        if self.root is not None:
            self.root = self._remove(self.root, value)
            if self.root is not None:
                self.size = 1
            else:
                self.size = 0
        else:
            return None

    @staticmethod
    def _remove(node, value):
        '''
        helper function
        '''
        if node is None:
            return None
        if node.value > value:
            node.left = BST._remove(node.left, value)
        elif node.value < value:
            node.right = BST._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                replace = BST._find_smallest(node.right)
                node.value = replace
                node.right = BST._remove(node.right, replace)
        return node

    def remove_list(self, xs):
        '''
        '''
        for x in xs:
            self.remove(x)
