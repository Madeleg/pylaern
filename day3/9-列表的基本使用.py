# 2026年,01月,13日,18时
name_list = ['a','b','c']

# 1 取值
print(name_list[0])
print(name_list.index('a'))

# 2 修改
name_list[2] = 'd'
print(name_list)

# 3 添加
name_list.append('e') #末尾添加
print(name_list)

name_list.insert(0, 'f') # 指定位置添加
print(name_list)

name_list.extend(['fg','h'])  #拼接
print(name_list)

# 4删除
name_list.pop(0)
print(name_list)

name_list.pop()
# name_list.clear()
name_list.remove('d')
print(name_list)