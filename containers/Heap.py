from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        self.num_nodes = 0
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        ret = True
        if not node:
            return True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        Inserts value into the heap.
        FIXME:
        Implement this function.
        HINT:
        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the BST and AVLTree
        insert functions.
        '''
        self.num_nodes += 1
        binary_str = bin(self.num_nodes)[3:]

        if self.root is None:
            self.root = Node(value)
        else:
            Heap._insert(self.root, value, binary_str)

    @staticmethod
    def _insert(node, value, binary_str):
        '''
        implement function
        '''
        if binary_str[0] == '0':
            if len(binary_str) == 1:
                node.left = Node(value)
            else:
                Heap._insert(node.left, value, binary_str[1:])
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        if binary_str[0] == '1':
            if len(binary_str) == 1:
                node.right = Node(value)
            else:
                Heap._insert(node.right, value, binary_str[1:])
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        FIXME:
        Implement this function.
        '''
        return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.
        FIXME:
        (or no helper at all),
        but I personally found dividing up the code into two made
        the most sense.
        '''
        remove_path = list('{0:b}'.format(self.num_nodes))
        self.num_nodes -= 1
        remove_path.pop(0)
        if len(remove_path) < 1:
            self.root = None
        else:
            self.root.value = Heap._remove_bottom_right(self.root, remove_path)
            Heap._trickle_down(self.root)

    @staticmethod
    def _remove_bottom_right(node, remove_path):
        if len(remove_path) == 1:
            if remove_path[0] == '1':
                value = node.right.value
                node.right = None
                return value
            else:
                value = node.left.value
                node.left = None
                return value
        elif remove_path[0] == '1':
            remove_path.pop(0)
            return Heap._remove_bottom_right(node.right, remove_path)
        else:
            remove_path.pop(0)
            return Heap._remove_bottom_right(node.left, remove_path)

    @staticmethod
    def _trickle_down(node):
        if not Heap._is_heap_satisfied(node):
            if node.left:
                left = node.left.value
            else:
                left = None
            if node.right:
                right = node.right.value
            else:
                right = None
            if left is not None and right is not None:
                if left < right:
                    min_child = node.left
                else:
                    min_child = node.right
            else:
                min_child = node.left or node.right
            if min_child and min_child.value < node.value:
                node.value, min_child.value = min_child.value, node.value
                Heap._trickle_down(min_child)
        if node.left and not Heap._is_heap_satisfied(node.left):
            Heap._trickle_down(node.left)
        if node.right and not Heap._is_heap_satisfied(node.right):
            Heap._trickle_down(node.right)
