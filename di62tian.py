def show1(num):
    print('*'*num)

def show2():
    n=eval(input("请输入一个你要打印星号的个数："))
    show1(1)
    show1(2)
    show1(n-1)
    show1(n)

def show3():
    n=eval(input("请输入一个你要打印星号的行数："))
    for i in range(1,n+1):
        show1(i)

def dayinxinghao():
    hs=eval(input("行数："))
    a=[0]*(hs+1)
    for i in range(1,hs+1):
        a[i]=eval(input("第{}行的个数:".format(i)))
    for i in range(1,hs+1):
        show1(a[i])

if __name__=="__main__":
    dayinxinghao()
    # show3()
    # show2()