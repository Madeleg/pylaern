# 2026年,01月,27日,16时
my_list = ("This is a test string from Andrew".split())
print(my_list)
#sorted是直接排序，不改变原列表，sort是直接改变原列表

def change_lowest(str_name: str):
    return str_name.lower()

print(sorted(my_list,key=change_lowest))

my_list.sort(key=change_lowest)
print(my_list)
