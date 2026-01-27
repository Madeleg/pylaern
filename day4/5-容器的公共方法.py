# 2026年,01月,16日,16时
def set_list_slice():
    test_list =[1,2,3,4,5,6]
    test_list[3:3] = ['x','y','z'] #就是将xyz插入到123456
    print(test_list)


def list_compare():
    a = [1,2,3]
    b = [1,2,3]
    print(a == b)
    print(a is b) #判断id

def use_method():
    """
    容器的方法
    :return:
    """
    a = (1,2,3)
    b = ('a','b','c')
    #zip把两个压缩起来
    print(list(zip(a,b)))
    print(dict(zip(a,b)))

    #如何使用enumerate
    #enumerate就是维护索引
    s = ['s','v','g','b']
    list2 = list(enumerate(s))
    print(list2)
    dict1 = dict(list2) #转成字典
    print({v:k for k,v in dict1.items()}) #键值反转

if __name__ == '__main__':
    # list_compare()
    use_method()