class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_c = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_c)


def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent


def sibling(node):
    gp = grandparent(node)
    p = node.parent
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left


class Red_Black_Tree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def __iter__(self):
        yield from self.root.__iter__()

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        # Case 1
        if node.parent == None:
            return
        # Case 2
        if node.parent.color == 'black':
            return
        # Case 3
        if sibling(node) and sibling(node).color == 'red':
            sibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))
        # Case 4
        gp = grandparent(node)

        if gp == None:
            return
        if gp.left == node and gp.left.right:
            self.left_rotation(node.parent)
            node = node.left

        elif gp.right and node == gp.right.left:
            self.right_rotation(node.parent)
            node = node.right
        # Case 5
        p = node.parent
        gp = p.parent
        if node == p.left:

            self.right_rotation(gp)
        else:
            self.left_rotation(gp)
        p.color = 'black'
        gp.color = 'red'

    def left_rotation(self, node):
        p = node.parent
        mov_up = node.right
        node.right = mov_up.left
        mov_up.left = node
        node.parent = mov_up
        if p != None:
            if node == p.left:
                p.left = mov_up
            else:
                p.right = mov_up
        mov_up.parent = p

    def right_rotation(self, node):
        p = node.parent
        mov_up = node.left
        node.left = mov_up.right
        mov_up.right = node
        node.parent = mov_up

        if p != None:
            if node == p.left:
                p.left = mov_up
            else:
                p.right = mov_up
        mov_up.parent = p


# Testing

def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)


tree = Red_Black_Tree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)
tree.insert(13)
print_tree(tree.root)

tree.insert(16)
print_tree(tree.root)

