# 2026年,01月,20日,18时
class Son1:
    def __init__(self,age,*args):
        self.age = age
        super().__init__(*args)
        #super() 并不是只调用 Son1 的父类（object），而是会继续根据 MRO
        # 查找下一个合适的类，因此会调用 Son2 的 __init__ 方法。
        #到这里时,会检查父类，然后调用第2个父类，就是son2

class Son2:
    def __init__(self,score):
        self.score = score


class Grandson(Son1,Son2):
    def __init__(self,name,*args):
        self.name = name
        super().__init__(*args)


if __name__ == '__main__':
    xiaom = Grandson('小明',18,98)
    print(xiaom.name)
    print(xiaom.age)
    print(xiaom.score)