# 2026年,01月,14日,14时
# 3.将整形转换为不同的进制进行输出

num = 12

hex_str = hex(num) #十六
oct_str = oct(num) #八
bin_str = bin(num) #二

print(hex_str)
print(oct_str)
print(bin_str)

# 1到100之间的奇数求和
total = sum(i for i in range(1,101) if i % 2 == 1)
print(f'和{total}')

#打印乘法表
for i in range(1,10):
    print()
    for j in range(1,i + 1):
        print(f'{i} * {j} = {i * j}  ',end='')
print()

#统计二进制1的个数


def count_bit(num):
    count = 0
    while num: #num会移动到0
        if num & 1: #按位与 and 有0则0
            count+= 1
        num >>=  1
    return  count

print(count_bit(5))