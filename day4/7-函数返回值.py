# 2026年,01月,16日,19时

def measure():
    """
    掌握返回多个值
    :return:
    """

    a = 10
    b = 20
    return  a,b

if __name__ == '__main__':
    a,b = measure()
    print(a,b)
    #交换两个值
    a,b = b,a
    print(a,b)

