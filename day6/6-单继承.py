# 2026年,01月,20日,17时
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")
    def run(self):
        print("跑---")
    def sleep(self):
        print("睡---")

class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name) #继承父类的name
        self.color = color

    def bark(self):
        print('汪汪叫')


class XiaoTian(Dog):
    def fly(self):
        print('飞')

    #调用父类
    def bark(self):
        print('aaaa')
        super().bark()
        print('sssss')
        print(f'{self.name}')



if __name__ == '__main__':
    wangcai = Dog('wangcai','blue')
    xtq = XiaoTian('21','yellow')
    xtq.bark()