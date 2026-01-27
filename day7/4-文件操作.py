# 2026年,01月,24日,11时
def wenjian():
    file = open('file1.txt',encoding='utf8')
    text = file.read()
    print(text)
    file.close()

def wenjian_readline():
    """
    一行一行读
    :return:
    """
    file = open('file1.txt',encoding='utf8')

    while True:
        text = file.readline()
        print(text)
        if not text:
            break

    file.close()

def fuzhi_wenjian():
    file_read = open('file1.txt')
    file_wirte = open('file2.txt','w')
    file = file_read.read()
    file_wirte.write(file)

    file_wirte.close()
    file_read.close()

if __name__ == '__main__':
    fuzhi_wenjian()