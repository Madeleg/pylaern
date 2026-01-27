# 2026年,01月,20日,13时
#先设计被依赖的类，就是从小的开始
class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return  f'{self.name}的面积为{self.area}'

class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        #剩余面积
        self.free_area = area
        #家具名称列表
        self.item_list = []

    def __str__(self):
        return  f'户型:{self.house_type},总面积{self.area},剩余{self.free_area},家具有{self.item_list}'

    def add_item(self,item:HouseItem):
        print(f'要添加{item}')
        #判断面积
        if item.area > self.free_area:
            print(f'{item.name}面积太大')
            return
        #家具添加进去
        self.item_list.append(item.name)
        #计算剩余面积
        self.free_area -= item.area

if __name__ == '__main__':
    #1.创建家具
    bed = HouseItem("席梦思", 61)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)
    print(bed)

    #2.创建房子对象
    my_home  = House('两市一厅',60)
    my_home.add_item(bed)


    print(my_home)