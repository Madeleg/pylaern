# 2026年,01月,20日,15时
class Women:
    def __init__(self,name):
        self.name = name
        #私有属性
        self.__age = 18

    #私有方法
    # def __secret(self):
    def secret(self):
        print(f'年龄为{self.__age}')

if __name__ == '__main__':
    xiaofang = Women('消防')
    print(xiaofang.secret())