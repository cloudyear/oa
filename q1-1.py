import sys
from collections import defaultdict

def rotatek(s, k):
    after_str = ''
    for c in s:
        ord_str = ord(c) - ord('a')
        after_str += chr(ord('a') + (ord_str + k) % 26)
    return after_str

N = int(sys.stdin.readline())
str_list = []
for i in range(N):
    str_list.append(str(sys.stdin.readline().strip()))
str_dict = defaultdict(list)
for s in str_list:
    k = 0
    after_rot_str = s
    while after_rot_str[0] != 'a':
        after_rot_str = rotatek(s, k)
        k += 1
    str_dict[after_rot_str].append(s)
print(str_dict)
print(list(str_dict.values()))
print(len(str_dict.values()))
