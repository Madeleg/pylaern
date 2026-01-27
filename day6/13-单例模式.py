# 2026年,01月,23日,20时
class MusicPlayer:
    instance = None #用来保存对象
    def __new__(cls, *args, **kwargs):
        # 1.创建对象，分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls) #类似于c的malloc
        return  cls.instance
    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    player1 = MusicPlayer('东风')
    player2 = MusicPlayer('七里')
    print(id(player1))
    print(id(player2))
    print(player1.name)
    print(player2.name)