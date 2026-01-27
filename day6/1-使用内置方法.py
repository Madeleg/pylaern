# 2026年,01月,19日,19时


class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print('跑')
    def eat(self):
        print('吃')
    #返回对象的描述信息，print函数输出使用
    def __str__(self):
        return self.name

if __name__ == '__main__':
    tiger = Person('dax',10,1.75)
    print(tiger)