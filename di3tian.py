def huanwei():
    print("请输入一个两位数：")
    n=input()
    n=int(n)
    a=int(n/10)
    b=n%10
    n=10*b+a
    print(n)

def huanwei2():
    print("请输入一个三位数：")
    n=input()
    n=int(n)
    a=int(n/100)
    # b=int((n-a*100)/10)
    b=int(n%100/10)
    c=n%10
    n=c*100+b*10+a
    print(n)

def huanwei3():
    # print("请输入一个三位数：")
    # n=input()
    print(input("请输入一个n位数：")[::-1])

def chufa():
    a=input()
    b=input()
    a=int(a)
    b=int(b)
    c=int(a/b)
    d=a%b
    print(a,'/',b,'=',end='')
    print(c,"......",d)
    
def qiuhe():
    print("请输入一个三位数：",end='')
    n=input()
    n=int(n)
    a=n%10
    b=int(n%100/10)
    c=int(n/100)
    p=a+b+c
    print("各个数位之和是：",p)

def qiuhe2():
    # n = input("请输入一个三位数：")
    print("各个数位之和是：",sum(list(map(int, input("请输入一个数：")))))
    # print("各个数位之和是：",sum(list(map(int, n))))


if __name__=="__main__":
    qiuhe2()
    # qiuhe()
    # chufa()
    # huanwei3()
    # huanwei2()
    # huanwei()