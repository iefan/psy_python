def zuixiaogongbeishu():
    i=1
    # x=int(input("请输入一个数："))
    # y=int(input("请输入一个数："))
    x,y=eval(input("请输入两个数(用逗号连接)："))
    if x>y:
        temp=x
        x=y
        y=temp
    s=y*i
    while s%x!=0:
        i+=1
        s=y*i
    print("最小公倍数：",s)

def qiukaoshicishu():
    x=2
    while 92*x-98!=87*x-78:
        x+=1
    print("尼克参加了%s次信息学比赛。" % x)

if __name__=="__main__":
    # qiukaoshicishu()
    zuixiaogongbeishu()