# 2026年,01月,19日,16时
import sys

sys.setrecursionlimit(10000) #设置递归次数，基本位999次
def f(n):
    if n == 1:
      return 1
    return n + f(n - 1)


if __name__ == '__main__':
    print(f(10))