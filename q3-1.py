# import math
# def _get_no_lucky_quadruplets(n):
#     total_levels = 1 + math.floor(math.log2(n)) #Total number of levels in balanced binary tree
#     no_lucky_quadruplets = 0
#     for i in range(1,total_levels):
#         if total_levels-i>=2:
#             if i==1:
#                 no_lucky_quadruplets+=(6) #Total number quadruplets when at level 1
#             else:
#                 no_lucky_quadruplets+=(12) #Total number quadruplets when at level 2....total_levels. This is to take quadruplets from both sides of tree into account
#     return no_lucky_quadruplets

# parent_array = [0, 1, 1, 2, 2, 3, 3, 4,6]

# n = len(parent_array)
# print(_get_no_lucky_quadruplets(n))


import sys

# N = int(sys.stdin.readline())
# p = sys.stdin.readline().strip().split()
# p = [int(i) for i in p]
import numpy as np
from collections import Counter
from collections import defaultdict
import math

N = 12
# p = [0, 1, 1, 2, 2, 3, 3, 4,6]
p = [0,1,1,2,2,3,3,4,4,5,7,8]
p = [i - 1 for i in p]
mat = [[np.inf for i in range(N)] for j in range(N)]
for i in range(N):
    if i == 0: continue
    mat[i][p[i]] = 1
    mat[p[i]][i] = 1

def startwith(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]

    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    return dis

res_list = []
res = 0
for i in range(N):
    dis_list = startwith(i, mat)
    # print(dis_list)
    dis_dict = defaultdict(list)
    for idx_j, j in enumerate(dis_list):
        if j != np.inf:
            dis_dict[j].append(idx_j)
    for k in dis_dict:
        if len(dis_dict[k])>=3:
            # res_list
            res += math.comb(len(dis_dict[k]),3)
print(res)
