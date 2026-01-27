# 2026年,01月,24日,15时
import os


def sacn_dir(current_path,width):
    """
    目录深度遍历
    :param current_path: 路径
    :param width: 缩进宽度
    :return:
    """
    file_list =os.listdir(current_path)#把当前文件目录列表传进去
    for file in file_list:
        print(' '* width,file)
        new_path = current_path + '/' + file #拼接起来
        if os.path.isdir(new_path):
            sacn_dir(new_path,width + 4)

def use_stat(file_path):
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))

if __name__ == '__main__':
    # sacn_dir('.',0)
    use_stat('file1.txt')