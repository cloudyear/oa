from collections import Counter
from collections import defaultdict

def health_subsequence(A, m):
    mod_dict = defaultdict(list)
    for i in A:
        mod_dict[i%m].append(i)
    mod_dict = sorted(mod_dict.values(), key=lambda x:len(x), reverse=True)
    # tmp_idx = 0
    # for i in range(len(mod_dict)):
    #     tmp_idx = i
    #     if len(mod_dict[i]) != len(mod_dict[0]):
    #         break ? can pass [13,43,34,1,73,-20,73,-8,17]
    # mod_dict = mod_dict[:tmp_idx + 1]
    max_len = len(max(mod_dict, key=lambda x: len(x)))
    new_mod_list = []
    for i in mod_dict:
        if len(i) == max_len:
            new_mod_list.append(i)
    new_mod_list = sorted(new_mod_list, key=lambda x: min(x))
    return new_mod_list[0]
    # if len(mod_dict) == 1:
    #     return mod_dict[0]
    # else:
    #     tmp_idx = 0
    #     for i in range(len(mod_dict)):
    #         tmp_idx = i
    #         if len(mod_dict[i]) != len(mod_dict[0]):
    #             break
    #     if tmp_idx == len(mod_dict) - 1:
    #         tmp_idx += 1
    #     mod_dict = mod_dict[:tmp_idx]
    # mod_dict = sorted(mod_dict, key=lambda x: min(x))
    # return mod_dict[0]

if __name__ == "__main__":
    A = [2,42,34,-53,73,-8,-53,-8,17]
    m = 7
    # A = [13,43,34,1,73,-20,73,-8,17]
    # m = 6
    # A = [76, -50]
    # m = 13
    # A = [2,5,-1,-34]
    # m = 2
    print(health_subsequence(A, m))
