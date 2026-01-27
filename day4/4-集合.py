# 2026年,01月,15日,18时
def use_set():
    set1 = set() #定义空集合
    set2 = {} #这样就是字典了，不对
    print(type(set1))

    set3 = {1,2,4,5}
    # print(set3[0])#错误的，不支持随机访问

    x = {'apple','ad','s'}
    y = {'goole','adv','s'}
    print(x.difference(y))#x不同于y的

    print(x-y)
    print(x|y)#
    print(x&y)#同或
    print(x^y) #异或，相异则真

def use_generator():
    """
    使用生成式
    :return:
    """
    #要加tuple否则会报错
    my_tuple = tuple(x for x in range(10))#元祖生成式
    print(my_tuple)
    my_set = set(x for x in 'absdskd' if x not in 'ak')
    print(my_set)
    print(max(my_set))
if __name__ == '__main__':
    use_generator()


