# 2026年,01月,27日,16时
import copy
def fuzhi():
    """
    赋值
    :return:
    """
    #这是不可变数据类型
    a = 2
    b = a
    a = 5
    print(a)
    print(b)
    #可变数据类型
    a = [1,2,3,4,5]
    b = a
    b[0] = 100
    print(a)
    print(b)

def shadow_copy():
    """
    浅copy：只复制外壳，里面可变数据类型还是一样的
    :return:
    """
    a = [1,2,[3,4]]
    b = copy.copy(a)
    a[0] = 100
    a[2][0] = 200
    print(a)
    print(b)

def deep_copy():
    """
    深copy：递归创建所有对象的实例，相当于创建一个副本
    :return:
    """
    a = [1,2,[3,4]]
    b = copy.deepcopy(a)
    a[0] = 100
    a[2][0] = 200
    print(a)
    print(b)

if __name__ == '__main__':
    # fuzhi()
    # shadow_copy()
    deep_copy()