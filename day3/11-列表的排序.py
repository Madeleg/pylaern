# 2026年,01月,14日,12时

name_list = ['zhangsan','lisi','wangwu']
num_list = [2,3,5,1,4]

# # 升序
# name_list.sort()
# num_list.sort()
#
# # 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)

# 反转  123 --> 321
name_list.reverse()
num_list.reverse()

for i in name_list:
    print(f'名字是{i}')

print(name_list)
print(num_list)