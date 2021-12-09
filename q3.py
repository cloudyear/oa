import sys
from collections import defaultdict
import math
from scipy.special import comb

N = int(sys.stdin.readline())
p = sys.stdin.readline().strip().split()
p = [int(i) for i in p]

# N = 12
# N = 1
# p = [0, 1, 1, 2, 2, 3, 3, 4,6]
# p = [0,1,1,2,2,3,3,4,4,5,7,8]
# p = [0]
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node_dict = {}
for i in range(len(p)):
    if node_dict.get(p[i], None) is None:
        new_node = TreeNode(p[i])
        node_dict[p[i]] = new_node
    else:
        new_node = node_dict[p[i]]
    child_node = TreeNode(i+1)
    node_dict[i+1] = child_node
    if new_node.left is None:
        new_node.left = node_dict[i+1]
    else:
        new_node.right = node_dict[i+1]

tree = node_dict[1]

def pathToNode(root, path, k):
    if root is None:
        return False

    path.append(root.val)

    if root.val == k:
        return True

    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right != None and pathToNode(root.right, path, k))):
        return True

    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        path1 = []
        pathToNode(root, path1, data1)

        path2 = []
        pathToNode(root, path2, data2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i = i + 1

        return (len(path1) + len(path2) - 2 * i)
    else:
        return 0

mat = [[0 for i in range(N)] for j in range(N)]

total_count = 0
for i in range(len(p)):
    row_dis_dict = defaultdict(int)
    over3_dict = defaultdict(int)
    for j in range(len(p)):
        dist = distance(tree, i+1, j+1)
        mat[i][j] = dist
        row_dis_dict[dist] += 1
        if row_dis_dict[dist] >= 3:
            over3_dict[dist] = row_dis_dict[dist]
    # print(row_dis_dict)
    # print(over3_dict)

    for k in over3_dict:
        total_count += math.comb(over3_dict[k], 3) #comb...

print(total_count)
#
# for i in mat:
#     print(i)


# print(tree.val)
# print(tree.left.val)
# print(tree.right.val)
# print(tree.left.left.val)
# print(tree.left.right.val)
# print(tree.right.left.val)
# print(tree.right.right.val)
# print(tree.left.left.left.val)
# print(tree.right.left.left.val)
