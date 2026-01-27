# 2026年,01月,22日,17时
class Tool:
    count = 0 #类属性,类似于类的全局变量
    def __init__(self,name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print(f'{cls.name}')

if __name__ == '__main__':
    tool1= Tool('斧子')
    print(Tool.count)
    tool2 = Tool('锤子')
    print(Tool.count)
    # print(tool2.count)这样不好
    #简单来说：类属性 “姓类”，就该用类名访问；
    #实例属性 “姓实例”，才用实例访问，这样代码才清晰、不易出错。
