def shuxianggedezuoweishu():
    x=1
    y=15
    sum_int=y
    print(x," ",y," ",sum_int)
    while sum_int<312:
        x+=1
        y+=2
        sum_int+=y
        print(x," ",y," ",sum_int)
    print("最后一排的座位数：",y)
    print("排数：",x)

def lianjiaxiaochengxu():
    x=eval(input("请输入一个整数："))
    ans=0
    while x!=0:
        ans+=x%8
        x=x//8
    print(ans)

def qiujimukuairshu():
    x=0
    while (x+6)%13!=0 or (x-6)%12!=0:
        x+=1
    print("格莱尔一共有%s块积木" % x)

if __name__=="__main__":
    qiujimukuairshu()
    # lianjiaxiaochengxu()
    # shuxianggedezuoweishu()