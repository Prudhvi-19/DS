class BTNode:
    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


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


def binarytreesize(root):
    if root is None:
        return 0
    else:
        return binarytreesize(root.left) + binarytreesize(root.right) + 1


def heightoftree(root):
    if root is None:
        return 0
    else:
        return (max(heightoftree(root.left), heightoftree(root.right))) + 1


def deepestnode(root):
    if root is None:
        return 0
    q = [root]
    while len(q) != 0:
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return node


paths = []


def paths_r_l(root, path=[]):
    global paths
    if root is None:
        return 0
    paths_r_l(root.left, path + [root.data])
    paths_r_l(root.right, path + [root.data])
    if root.left is None and root.right is None:
        path.append(root.data)
        paths.append(path)


def diameteroftree(root):
    if root is None:
        return 0
    l1 = heightoftree(root.left)
    r1 = heightoftree(root.right)
    d1 = diameteroftree(root.left)
    d2 = diameteroftree(root.right)
    return max(l1 + r1 + 1, max(d1, d2))


def maxpathsum(root):
    if root is None:
        return 0
    l = maxpathsum(root.left)
    r = maxpathsum(root.right)
    max_single = max(max(l, r) + root.data, root.data)
    max_top = max(l + r + root.data, max_single)
    maxpathsum.res = max(maxpathsum.res, max_top)
    return max_single


def mpshelp(root):
    maxpathsum.res = float('-inf')
    maxpathsum(root)
    return maxpathsum.res


def mirrortree(troot):
    if troot is None:
        return
    else:
        mirrortree(troot.left)
        mirrortree(troot.right)
        temp = troot.left
        troot.left = troot.right
        troot.right = temp
    return troot


def lca(root, alpha, beta):
    if root is None:
        return
    if root.data == alpha or root.data == beta:
        return root
    left = lca(root.left, alpha, beta)
    right = lca(root.right, alpha, beta)
    if left and right:
        return root
    else:
        if left:
            return left
        else:
            return right

def all_ancestors(root,node):
    if root is None:
        return 0
    if root.left == node or root.right==node or all_ancestors(root.left,node) or all_ancestors(root.right,node):
        print(root.data,end=" ")
        return 1
    return 0

def zigzagtraversal(root):
    if root is None:
        return
    q = [[root,0]]
    q.append(None)
    stack = []
    while len(q)!=0:
        node = q.pop(0)
        if node == None:
            while stack:
                print(stack.pop(),end=" ")
            if len(q)!=0:
                q.append(None)
        else:
            if node[1] % 2 == 0:
                print(node[0].data, end=" ")
            else:
                stack.append(node[0].data)
            if node[0].left is not None:
                q.append([node[0].left,node[1]+1])
            if node[0].right is not None:
                q.append([node[0].right,node[1]+1])


"""For Diagram Refer Karumanchi Page:155"""
root = BTNode(1)
l1 = BTNode(2)
l2 = BTNode(3)
l3 = BTNode(4)
l4 = BTNode(5)
l5 = BTNode(6)
l6 = BTNode(7)
l7 = BTNode(8)
l8 = BTNode(9)
l9 = BTNode(10)
l10 = BTNode(11)
l11 = BTNode(12)
l12 = BTNode(13)
root.left = l1
root.right = l2
l1.left = l3
l1.right = l4
l2.left = l5
l2.right = l6
l3.left = l7
l3.right = l8
l4.right = l9
l6.left = l10
l10.left = l11
l10.right = l12
# OPERATIONS
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
print("Size of Tree:")
k = binarytreesize(root)
print(k)
print("Height of Tree")
k = heightoftree(root)
print(k)
print("Deepest Node")
k = deepestnode(root)
print(k.data)
print("Paths root to leaves")
paths_r_l(root)
for i in paths:
    print(i)
print("Diameter of Tree")
k = diameteroftree(root)
print(k)
print("Maximum path sum")
k = mpshelp(root)
print(k)
# Remove Below Comment To Convert Tree To its Mirror tree
"""
print("Mirror Tree Level Order")
troot = mirrortree(root)
levelorder(troot)
"""
print("Our Common Ancestor")
k = lca(root, 13, 5)
print(k.data)

print("All ancestors of a Node")
all_ancestors(root,l10)
print()

print("ZigZag")
zigzagtraversal(root)
print()