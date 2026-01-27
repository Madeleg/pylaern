# 2026年,01月,24日,17时
def use_eval(file_path):
    """
    eval 可以把字符串转成有效表达式
    :param file_path:
    :return:
    """
    file = open(file_path, 'r+', encoding='utf8')
    file_read = file.read()
    my_dict = eval(file_read)
    print(my_dict)
    print(type(my_dict))
    file.close()

if __name__ == '__main__':
    use_eval('file6.txt')