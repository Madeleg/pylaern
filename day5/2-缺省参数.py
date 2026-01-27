# 2026年,01月,19日,11时

def print_info(name,title ='',gender =True):
    print(f'名字{name},{title},{gender}')


if __name__ == '__main__':
    #name是位置参数，必须放在第一个
    #position（位置参数）
    #有标题的是keyword参数，可以随便放
    print_info('ww')
    print_info('www',title='班长')
    print_info('www',title='班长',gender=False)