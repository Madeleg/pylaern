# 2026年,01月,15日,15时
xiaom_dict = {'name':'小猫'}
# 1.取值
print(xiaom_dict['name'])
# 2.增加、修改
xiaom_dict['age'] = 18
print(xiaom_dict)
xiaom_dict['name'] = '小小毛'
print(xiaom_dict)
# 3.删除
xiaom_dict.pop('name')
xiaom_dict.clear() #删除全部

#4.统计
print(len(xiaom_dict))

#5.合并
temp_dist = {'h':12}
xiaom_dict.update(temp_dist)
print(xiaom_dict)

#遍历
xiaom_dict = {'name':'xxm',
              'q':'1',
              '2':'12'}
for i in xiaom_dict:
    print(i,xiaom_dict[i])

for i in  xiaom_dict.items():
    print(i)

for i in  xiaom_dict.keys():
    print(i)

for i in xiaom_dict.values():
    print(i)

for k,v in xiaom_dict.items():
    print(f'键 {k},值 {v}')

#拆包
def use_unpack_package():
    k,v,w =(1,2,3)
    print(k,v,w)
