# 2026年,01月,15日,17时
def str_chazhao():
    #字符或数字
    x = 'qweww'
    print(x.isalnum())
    #数字
    print(x.isdecimal())

    #字符串的查找与替换
    print(x.find('w')) #返回的是字符串的下标
    print(x.find('w',1)) #找w，从1的位置开始找
    print(x.replace('w','W')) #替换w
    print(x.replace('w','W',1)) #替换w,只替换1次

def str_split_join():
    """
    字符串的分割与连接
    :return:
    """
    s1 = 'abc qwe 11 3 -'
    print(s1.split()) #按空格分割

    s2 = 'abc,qwe,11,3,-'
    print(s2.split(',')) #用逗号分割

    s3 = 'abc\nqwe\n11\n3'
    print(s3.split())  # \n可直接分割

    s4 = ['qw','2','www']
    print(''.join(s4)) #接起来是完整的
    print(' '.join(s4))  # 接起来按空格划分

def str_slice():
    """
    字符串的切片
    :return:
    """
    s1 = '0123456789'
    print(s1[2:6])#2-5
    print(s1[2:])#2到结束
    print(s1[:6])#开始到5
    print(s1)
    print(s1[::2]) #步长为2，相当于隔一个输出
    print(s1[1::2]) #从1开始，每隔一个取一个
    print(s1[2:-1]) #从2开始，到-1结束，就是右边第2个结束（开区间）
    print(s1[-2:]) #最后两个字符
    print(s1[::-1]) #字符串的逆序，就是倒着拿，步长为-1

def list_slice():
    my_list =list('0123456789') #强转成list
    print(my_list)
if __name__ == '__main__':
    # str_split_join()
    # str_slice()
    list_slice()

