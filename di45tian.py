def huagongdafa():
    x=eval(input("请输入一个纯小数："))
    while x>=1 or x<=0:
        x=eval(input("请输入一个纯小数："))
    a=1
    y=x
    while abs(y-int(y))>1e-10:
        a*=10
        y=x*a
    b=int(y)
    print(b,'/',a)
    for i in range(b,0,-1):
        if b%i==0 and a%i==0:
            j=i
            break
    print("最简分数为：",b//j,'/',a//j)

def shuchudaoshu():
    sum_psy=0
    m=eval(input("n="))
    while m!=0:
        sum_psy=sum_psy*10+m%10
        m=m//10
    print(sum_psy)

def sishewuru1():
    m=1
    x=3.14159
    n=eval(input("n="))
    while n<1 or n>5:
        n=eval(input("n="))
    for _ in range(1,n+1):
        m*=10
    y=int(x*m+0.5)
    y=y/m
    print(y)

def sishewuru2(x, n):
    m=1
    # x=3.14159
    # n=eval(input("n="))
    # while n<1 or n>5:
        # n=eval(input("n="))
    for _ in range(1,n+1):
        m*=10
    y=int(x*m+0.5)
    y=y/m
    print(y)

def sishewuru3():
    m=1
    x=eval(input("x(必须输入小数！)="))
    n=eval(input("n="))
    weishu=0
    a=1
    y=x
    while abs(y-int(y))>1e-10:
        weishu+=1
        a*=10
        y=x*a
    while n<1 or n>weishu:
        n=eval(input("n="))
    for _ in range(1,n+1):
        m*=10
    y=int(x*m+0.5)
    y=y/m
    print(y)

if __name__=="__main__":
    # sishewuru3()
    # sishewuru2(3.14159,4)
    # print(round(3.14159,4))
    # sishewuru1()
    # shuchudaoshu()
    huagongdafa()