# 2026年,01月,20日,18时
class A:
    def test(self):
        print('a t')

    def demo(self):
        print('a d')

class B:
    def test(self):
        print('b t')
    def demo(self):
        print('b d')

class C(A,B):
    def test(self):
        print('c t')

if __name__ == '__main__':
    cc = C()
    cc.test()
    #显示查找顺序
    print(C.__mro__)