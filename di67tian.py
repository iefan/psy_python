def dindadeshu1(b,m):
    i=0
    while True:
        x=b[i]
        num=0
        for j in range(0,10):
            if x<b[j]:
                num+=1
        if num==m-1:
            break
        else:
            i+=1
    return x

def dindadeshu2():
    a=[99,200,95,87,98,-12,30,87,75,-25]
    n=eval(input("请输入你要的第几大的数："))
    while n<1 or n>10:
        n=eval(input("请输入你要的第几大的数："))
    print(dindadeshu1(a,n))


def qiuhe1(b):
    sum_int,MAX=b[0],b[0]
    for i in range(1,5):
        sum_int+=b[i]
        if sum_int>MAX:
            MAX=sum_int
        # print(sum_int,MAX)
    return MAX

def qiuhe2():
    a=[0]*5
    for i in range(0,5):
        a[i]=eval(input("请输入一个数："))
    ans=qiuhe1(a)
    print(ans)


def tiaoshengbisai1(x,a):
    num=1
    for j in range(0,5):
        if x<a[j]:
            num+=1
    return num

def tiaoshengbisai2():
    a=[0]*5
    for i in range(5):
        a[i]=eval(input("请输入{}号同学的跳绳成绩：".format(i+1)))
    for i in range(5):
        print(a[i],'----',tiaoshengbisai1(a[i],a))

if __name__=="__main__":
    tiaoshengbisai2()
    # qiuhe2()
    # dindadeshu2()