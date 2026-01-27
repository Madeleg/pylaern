# 2026年,01月,24日,17时
import sys


def wirte_hello(file_path):
    file = open(file_path,'w+',encoding='utf8')
    file.write('h')
    file.close()

if __name__ == '__main__':
    wirte_hello(sys.argv[1])