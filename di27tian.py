def feibonaqishulie():
    a1=1
    a2=a1
    print('%5s' % a1,end='')
    print('%5s' % a2,end='')
    for _ in range(3,11):
        a3=a1+a2
        print('%5s' % a3,end='')
        a1=a2
        a2=a3

def leijia():
    a=int(input())
    b=1
    for i in range(1,a):
        b=b*i
        if b%3==0:
            b=b//3
        if b%5==0:
            b=b//5
    print(b)

def diyijiadiyijiayidehe1():
    n=2
    a=1
    for _ in range(1,30):
        print(a)
        a=a+n
        n=n*2

def diyijiadiyijiayidehe2():
    a=1
    for _ in range(1,30):
        print(a)
        a=a*2+1

def diyijiadiyijiayidehe3():
    n=2
    a=1
    for _ in range(1,30):
        print(a)
        n=n*2
        a=n-1

if __name__=="__main__":
    diyijiadiyijiayidehe3()
    # diyijiadiyijiayidehe2()
    # diyijiadiyijiayidehe1()
    # leijia()
    # feibonaqishulie()