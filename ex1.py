# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

labels = ['狐狸', '猫咪', '狗狗', '小猪']  # 设置标签
sizes = [15, 30, 45, 10]  # 占比，和为100
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']  # 颜色
#explode = (0, 0.1, 0, 0)  # 展开第二个扇形，即Hogs，间距为0.1

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)  # startangle控制饼状图的旋转方向

#plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)  # startangle控制饼状图的旋转方向
plt.axis('equal')  # 保证饼状图是正圆，否则会有一点角度偏斜
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

plt.show()