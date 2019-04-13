def dadada():
    num=1
    x=eval(input("请输入一个纯小数："))
    while x>=1 or x<=0:
        x=eval(input("请输入一个纯小数："))
        num=1
    num*=10
    y=x*num
    # while abs(y-int(y))>0:
    # while abs(y-int(y))<1 and abs(y-int(y))>0:
    while abs(y-int(y))>1e-9:
        num*=10
        y=x*num
    print(x,"化成整数后是",int(y),sep='')

def shuyinshu():
    ans=0
    n=eval(input("请输入一个整数："))
    i=1
    while i<=n:
        if n%i==0:
            ans+=1
        i+=1
    print(ans)

def shuxiaoshuweishu():
    f=input("f=")
    a=f.index(".")
    b=f[a+1:]
    print(f,"的小数位数是：",len(b))

def dadada2():
    a=input("请输入一个纯小数：")
    c=a.index(".")
    b=a[c+1:]
    # print(c,b)
    # d=1
    a=float(a)
    for _ in range(0,len(b)):
        # d*=10
        a*=10
    print(int(a))

if __name__=="__main__":
    dadada2()
    # shuxiaoshuweishu()
    # shuyinshu()
    # dadada()