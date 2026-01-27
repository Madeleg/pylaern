# 2026年,01月,19日,12时


def duozhi_canshu(num,*args,**kwargs):
    """
    可以返回多个值的定义,*代表拆包，arg代表元组，kwarg代表字典
    :return:
    """
    print(num)
    print(args)
    print(kwargs)

# 1. 定义一个函数 sum_numbers，可以接收的 任意多个整数
# 2. 功能要求：将传递的所有数字累加 并且返回累加结果
def sum_numbers(*args):
    num = 0
    for i in args:
        num += i

    return num

def demo(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    # duozhi_canshu(1,22,3,2,'2',name="小明", age=18, gender=True)
    # print(sum_numbers(1,3,5))

    # 需要将一个元组变量/字典变量传递给函数对应的参数
    gl_nums = (1, 2, 3)
    gl_xiaoming = {"name": "小明", "age": 18}
    # 会把 num_tuple 和 xiaoming 作为元组传递个 args
    # demo(gl_nums, gl_xiaoming)
    demo(*gl_nums, **gl_xiaoming)
