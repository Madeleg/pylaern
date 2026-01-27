# 2026年,01月,20日,14时
class Gun:
    #初始化
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0
    #增加子弹
    def add_bullet(self,count):
        self.bullet_count += count
    #发射
    def shoot(self):
        if self.bullet_count <= 0:
            print('无子弹')
            return
        self.bullet_count -= 1
        print(f'{self.model}发射子弹,子弹数为{self.bullet_count}')

    def __str__(self):
        return f'{self.model}冲'


class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print(f'{self.name}还没有枪')
            return
        self.gun.add_bullet(50)
        self.gun.shoot()




if __name__ == '__main__':
    ak47 = Gun('ak47')
    xusanduo = Soldier('许')
    xusanduo.gun = ak47
    xusanduo.fire()
    print(xusanduo.gun)

