def zuidagongyueshu1():
    m,n=eval(input("请输入两个自然数(用逗号连接)："))
    if n>m:
        temp=m
        m=n
        n=temp
    BOX=m%n
    while BOX!=0:
        m=n
        n=BOX
        BOX=m%n
    print("最大公约(因)数：",n)

def zuidagongyueshu2():
    x,y=eval(input("请输入两个自然数(用逗号连接)："))
    if x<y:
        psy=x
        x=y
        y=psy
    while x!=y:
        x-=y
        if x<y:
            psy=x
            x=y
            y=psy
    print(x)

def zuidagongyueshu3():
    x,y=eval(input("请输入两个自然数(用逗号连接)："))
    if x>y:
        TEMP=x
        x=y
        y=TEMP
    n=x
    while x%n!=0 or y%n!=0:
        n-=1
    print("每组的人数最多为：",n) 

if __name__=="__main__":
    zuidagongyueshu3()
    # zuidagongyueshu2()
    # zuidagongyueshu1()