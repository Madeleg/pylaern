print('hello world')


# a = input()
# print(a)

def sum2():
    """
    学习算术运算符
    :return:
    """
    a = 5 / 2
    print(a)
    a = 5 // 2
    print(a)
    b = 2 ** 3
    print(b)


# sum2()

def use_bit():
    """
    位运算训练
    :return:
    """
    print()
    print('-' * 50)
    print(5 >> 1)
    print(-5 >> 1)  # 减1除2


# use_bit()

i = 0
while i <= 5:
    print(i)
    i += 1
print(f'i的值{i}')

print("hello world", end='')