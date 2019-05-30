def bijiaodaxiao1(a,n):
    if n==1:
        t=a[1]
    else:
        if bijiaodaxiao1(a,n-1)>a[n]:
            t=bijiaodaxiao1(a,n-1)
        else:
            t=a[n]
    return t

def bijiaodaxiao2():
    a=[0]*6
    for i in range(1,6):
        a[i]=eval(input("请输入一个整数:"))
        print()
    print("最大的数:{}".format(bijiaodaxiao1(a,5)))

def zhanzhuanxiangchu1(a,b):
    if a==b:
        return a
    else:
        if a>b:
            return zhanzhuanxiangchu1(a-b,b)
        else:
            return zhanzhuanxiangchu1(a,b-a)

def zhanzhuanxiangchu2():
    x,y,z=eval(input("请输入三个整数(注意:用逗号连接!!) :"))
    x=zhanzhuanxiangchu1(x,y)
    x=zhanzhuanxiangchu1(x,z)
    print(x)

def gcd1(a,b):
    if b==0:
        return a
    else:
        return gcd1(b,a%b)

def gcd2():
    a,b=eval(input("a,b="))
    print("最大公约数：{}".format(gcd1(a,b)))

if __name__=="__main__":
    gcd2()
    # zhanzhuanxiangchu2()
    # bijiaodaxiao2()