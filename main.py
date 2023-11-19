# Операция А=A ⋃обрB означает, что элементы дерева В будут добавлены
# в дерево А в обратном порядке обхода дерева В

# Рандомизированное дерево двоичного поиска
# А – прямой, В – симметричный
# Левый сын, правый брат (указатели)


import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def preorder(root):
    if root is not None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


def randomized_insert(root, keys):
    for key in keys:
        root = insert(root, key)
    return root


def randomized_bst(keys):
    root = None
    root = randomized_insert(root, keys)
    return root


def print_tree(root, order):
    if order == 'pre':
        preorder(root)
    elif order == 'post':
        postorder(root)
    elif order == 'in':
        inorder(root)


keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
random.shuffle(keys)
root = randomized_bst(keys)
print_tree(root, 'in')
