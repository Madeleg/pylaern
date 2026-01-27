# 2026年,01月,18日,14时
from os.path import split


def homework6():
    my_list = [1,1,2,2,3,6,6,8,3,9,8,10]
    result = 0
    for i in my_list:
        result ^= i
        print(result)
        #与负数取反
    split_flag = result&-result #获取result的最低位
