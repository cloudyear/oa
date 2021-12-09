# ## rotation strings
# from collections import defaultdict
#
# def isequivalent(a, b):
#     # if len(a) != len(b):
#     #     return False
#     # else:
#     tmp = None
#     for i in range(len(a)):
#         a_i = ord(a[i])
#         b_i = ord(b[i])
#         diff = b_i - a_i if (b_i-a_i)>=0 else (26-a_i+b_i)
#         if tmp is None:
#             tmp = diff
#         else:
#             if tmp == diff: continue
#             else: return False
#     return True
#
# if __name__ == '__main__':
#     N = int(input().strip())
#     l = []
#     for i in range(N):
#         s = input().strip()
#         l.append(s)
#     res = []
#     l_s = defaultdict(list)
#     for s in l:
#         l_s[len(s)].append(s)
#     group_count = 0
#     for i in l_s:
#         tmp_l = l_s[i]
#         exit_flag = False
#         if len(tmp_l) == 1: group_count += 1
#         for s1 in range(len(tmp_l) - 1):
#             for s2 in range(s1 + 1, len(tmp_l)):
#                 if isequivalent(tmp_l[s1], tmp_l[s2]):
#                     group_count += 1
#                     exit_flag = True
#                     break
#             if exit_flag:
#                 break
#     print(group_count)


def rotk(s, k):
    ans = ''
    # Iterate through each character
    for c in s:
        # Find the index of the char
        a = ord(c) - ord('a')
        # Rotate it by k and convert it to char
        ans = ans + chr(ord('a') + (a + k) % 26)
    return ans


# Prompt for the size
N = int(input())
l = []
# Populate N strings to list
for i in range(N):
    l.append(input())
# Initialize a dictionary
d = {}
# Iterate through all strings
for s in l:
    k = 0
    # Rotate string till we get the first character is 'a'
    t = rotk(s, k)
    while t[0] != 'a':
        k += 1
        t = rotk(s, k)
    # Add it to dictionary based on the string
    if t not in d:
        d[t] = []
    d[t].append(s)
print(d)
print(list(d.values()))

