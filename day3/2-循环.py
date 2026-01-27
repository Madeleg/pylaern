# 2026年,01月,13日,12时

def use_for():
    my_list = ['a', 2, 3]
    for i in my_list:
        print(i)    #i是里面的元素，不是下标
    print(i) #i 在for循环外也可以用，因为相当于在这个函数内

def use_for_else():
    for i in range(10):#range是左闭右开 0 - 9
        if i == 15:
            print(f'找到了{i}')
    else:
        print('没找到')
# use_for()
print('12')
use_for_else()