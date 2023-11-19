import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class RandomBinaryTree:
    def __init__(self):
        self.root = None

    def pre_insertNonRand(self, key):  # Для нерандомизированного дерева
        self.root = self.insertNonRand(self.root, key)

    def insertNonRand(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insertNonRand(root.left, key)
        else:
            root.right = self.insertNonRand(root.right, key)
        return root

    def pre_insert(self, key):
        self.root = self.insert(self.root, key)

    def insert(self, root, key): # Для рандомизированного дерева
        if root is None:
            return Node(key)

        if random.random() < 0.5:
            root.left = self.insert(root.left, key)
            root = self.rotate_right(root)
        else:
            root.right = self.insert(root.right, key)
            root = self.rotate_left(root)

        return root

    def rotate_right(self, y):
        x = y.left
        extTr = x.right

        x.right = y
        y.left = extTr

        return x

    def rotate_left(self, x):
        y = x.right
        extTr = y.left

        y.left = x
        x.right = extTr

        return y

    def pre_inorder_tr(self):   # Вывод в симметричном порядке
        self.inorder_tr(self.root)

    def inorder_tr(self, root):
        if root is not None:
            self.inorder_tr(root.left)
            print(root.key, end=' ')
            self.inorder_tr(root.right)

    def pre_preorder_tr(self):  # Вывод в прямом порядке
        self.preorder_tr(self.root)

    def preorder_tr(self, root):
        if root is not None:
            print(root.key, end=' ')
            self.preorder_tr(root.left)
            self.preorder_tr(root.right)

    def pre_postorder_tr(self):  # Вывод в обратном порядке
        self.postorder_tr(self.root)

    def postorder_tr(self, root):
        if root is not None:
            self.postorder_tr(root.left)
            self.postorder_tr(root.right)
            print(root.key, end=' ')


if __name__ == "__main__":

    # Дерево A
    tree_A = RandomBinaryTree()
    keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    # random.shuffle(keys)
    for key in keys:
        # НЕрандомизированное дерево двоичного поиска
        tree_A.pre_insertNonRand(key)

        # Рандомизированное дерево двоичного поиска
        # tree_A.pre_insert(key)

    print("Вывод дерева A в прямом порядке: ")
    tree_A.pre_preorder_tr()
    print("\n")

    # Дерево B
    tree_B = RandomBinaryTree()
    keys2 = [4, 7, 13]
    for key2 in keys2:
        # НЕрандомизированное дерево двоичного поиска
        tree_B.pre_insertNonRand(key2)

        # Рандомизированное дерево двоичного поиска
        # tree_B.pre_insert(key2)

    print("Вывод дерева B в симметричном порядке: ")
    tree_B.pre_inorder_tr()
    print("\n")

    # Дерево C
    # tree_C = RandomBinaryTree()
    # tree_C.merge_trees(tree_A, tree_B)
    # print("Вывод дерева C в прямом порядке: ")
    # tree_C.pre_preorder_tr()

    print("DEBUG: Вывод дерева A в обратном порядке: ")
    tree_A.pre_postorder_tr()
