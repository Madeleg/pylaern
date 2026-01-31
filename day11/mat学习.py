# 2026年,01月,28日,18时
from matplotlib import pyplot as plt
import matplotlib
import random
x = range(0,120)
y = [random.randint(10,30) for i in range(120)]
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)
# 加坐标轴信息
# 在有中文输出的地方，增加一个属性： fontproperties
# plt.xlabel('时间',fontproperties = 'simHei',fontsize=20)
'''另外一种写法
查看 Linux、Mac 下支持的字体
终端执行： fc-list
查看支持的中文（冒号前面有空格) fc-list :lang=zh
查看 Windows 下的字体：“C:\Windows\Fonts”
可以自己下载字体文件（xxx.ttf），然后双击安装即可
from matplotlib import font_manager
#下面是mac电脑字体路径
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=18)
plt.ylabel("天气",fontproperties=my_font)
# plt.ylabel("次数",fontproperties=my_font)
# 设置标题
plt.title('每分钟跳动次数',fontproperties=my_font,color='red')
'''
#rotation将字体旋转45度
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc',size=18)
plt.xlabel('时间',rotation=45,fontproperties = my_font)
plt.ylabel("次数",fontproperties = my_font)
# 设置标题
plt.title('每分钟跳动次数',color='red',fontproperties = my_font)
plt.show()