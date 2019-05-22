def choushu1(n):
    while n%2==0:
        n=n//2
    while n%3==0:
        n=n//3
    while n%5==0:
        n=n//5
    return n==1

def choushu2():
    num=0
    for i in range(1,101):
        if choushu1(i):
            print(i,end='-->')
            num+=1
            if num%10==0:
                print()
    print("结束!")
    print("一共有{}个丑数。".format(num))



def wanquanshu1(n):
    sun=0
    for i in range(1,n):
        if n%i==0:
            sun+=i
    return n==sun

def wanquanshu2():
    ans=0
    for i in range(4,8):
        if wanquanshu1(i):
            print(i)
            ans+=1
    print("个数：",ans)

def huiwenshu1(m):
    temp=m
    n=0
    while temp!=0:
        n=n*10+temp%10
        temp=temp//10
    return m==n

def huiwenshu2():
    num=0
    for i in range(100,10000):
        if huiwenshu1(i):
            print(i,end='    ')
            num+=1
            if num%10==0:
                print()
    print("个数：{}".format(num))

if __name__=="__main__":
    huiwenshu2()
    # wanquanshu2()
    # choushu2()