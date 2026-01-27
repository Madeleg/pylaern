# 2026年,01月,15日,15时
def yuanzu():
    info_tuple = ("zhangsan",20,188)
    for i in info_tuple:
        print(i)

    print(info_tuple.index("zhangsan"))
    print(info_tuple.count("zhangsan"))
    print(len(info_tuple))

def use_str():
    """
    格式化字符串
    :return:
    """
    info_tuple = ("xiaom",22,19)
    info_str = "%s%d%d" % info_tuple
    print(info_str)

def use_tuple_error():
    """
    使用元祖可能的错误
    :return:
    """
    a = [1]
    print(type(a)) #列表
    b = (1,) #元祖
    c = (1) #类型会变成int
    print(type(b))


if __name__ == '__main__':
    use_tuple_error()