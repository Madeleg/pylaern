# 2026年,01月,27日,18时
import re
def simple_function():
    """第一次使用"""
    result = re.match('wangdao','wangdao.cn')
    if result:
        print(result.group())

def single():
    ret = re.match(".", "M")
    print(ret.group())
    ret = re.match("t.o", "too")
    print(ret.group())
    ret = re.match("t.o", "two")
    print(ret.group())

if __name__ == '__main__':
    # simple_function()
    single()