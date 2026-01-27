# 2026年,01月,19日,17时


class Person:
    def __init__(self,color,name):
        self.color = color
        self.name = name

    def shengren(self):
        print('叫')
    def jiaren(self):
        print('摇尾巴')

if __name__ == '__main__':
    #实例化
    dog = Person('yellow','大黄')
    dog.jiaren()
    dog.shengren()