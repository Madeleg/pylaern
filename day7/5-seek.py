# 2026年,01月,24日,15时
# 1. 打开
file = open("file1.txt", "w+")
print(type(file))
# 2. 写入文件
file.write("123 hello")
file.seek(2)
text = file.read()
print(text)
# 3. 关闭
file.close()