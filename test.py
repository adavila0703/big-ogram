from bigogram import BigO
import time

test = BigO()

nums_list = [x for x in range(10000)]


def in_num_list(test):
    ret = []
    for i in range(0, 100):
        ret.append(test in nums_list)
    return ret

test.calc_bigo(func = in_num_list, loop = 1000)