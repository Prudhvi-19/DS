# iamprudhvi
class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if root is None:
        node = BSTNode(data)
        root = node
    else:
        if data < root.data:
            if root.left is None:
                node = BSTNode(data)
                root.left = node
            else:
                insert_node(root.left, data)
        else:
            if root.right is None:
                node = BSTNode(data)
                root.right = node
            else:
                insert_node(root.right, data)


def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is None:
        return
    else:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def levelorder(root):
    if root is None:
        return
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        print(node.data, end=" ")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    print()


def find(root, data):
    if root is None:
        print("Empty Tree")
        return
    while root:
        if root.data == data:
            return root
        elif root.data > data:
            root = root.left
        else:
            root = root.right
    return None


def find_max(root):
    if root is None:
        print("Empty Tree Return")
    if root.right == None:
        return root
    else:
        return find_max(root.right)


def find_min(root):
    if root is None:
        print("Empty Tree")
        return
    if root.left == None:
        return root
    else:
        return find_min(root.left)


def predecessor(root):
    if root is None:
        print("Empty Tree")
        return
    if root.left is not None:
        return find_max(root.left)
    else:
        print("No Predecessor for given root")
        return


def successor(root):
    if root is None:
        print("Empty Tree")
        return
    if root.right is not None:
        return find_min(root.right)
    else:
        print("No Successor for given root")
        return


# Delete Function is Complex Function of Tree DS. I Will write it later
def delete_node(root):
    pass


def lca(root, a, b):
    while (root):
        if (a <= root.data <= b) or (a >= root.data >= b):
            return root
        if a < root.data:
            root = root.left
        else:
            root = root.right
    return None


def is_bst(root, min=float('-inf'), max=float('inf')):
    if root is None:
        return 1
    if root.data <= min or root.data >= max:
        return 0
    t1 = is_bst(root.left, min, root.data)
    t2 = is_bst(root.right, root.data, max)
    res = t1 and t2
    return res


# For Diagram of Tree Refer Karumanchi Page : 179
root = BSTNode(45)

insert_node(root, 33)
insert_node(root, 71)
insert_node(root, 30)
insert_node(root, 35)
insert_node(root, 67)
insert_node(root, 79)
insert_node(root, 19)
insert_node(root, 40)
insert_node(root, 55)
insert_node(root, 69)
insert_node(root, 75)
insert_node(root, 100)
insert_node(root, 10)
insert_node(root, 70)
insert_node(root, 77)
insert_node(root, 97)
insert_node(root, 264)
insert_node(root, 3)
insert_node(root, 15)

print("InOrder")
inorder(root)
print()
print("PreOrder")
preorder(root)
print()
print("PostOrder")
postorder(root)
print()
print("LevelOrder")
levelorder(root)
print("Find My Element")
k = find(root, 264)
if k != None:
    print(k.data)
else:
    print("Not Found")

print("Max Element")
k = find_max(root)
print(k.data)

print("Min Element")
print(find_min(root).data)
print("Find My Predecessor")
k = predecessor(root)
print(k.data)
print("Find My Successor")
k = successor(root)
print(k.data)
print("Our Least Common Ancestor")
k = lca(root, 10, 45)
if k is None:
    print("No Such Nodes or Node")
else:
    print(k.data)
print("Checking our Tree is bst Or not")
k = is_bst(root)
if k==1:
    print("Yes, It is BST")
else:
    print("No! Oops not a BST")
