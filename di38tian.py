def qiuxiaoshu1():
    i=1
    m=1
    n=7
    print(m//n,'.',end='')
    r=m%n
    while i<=100:
        print((r*10)//n,end='')
        r=(r*10)%n
        i+=1

def qiuxiaoshu2():
    n1=1
    a,b,n2=eval(input("请输入三个正整数(用逗号连接)："))
    # print(a,'/',b,'=',end='',sep='')
    # print("%s/%s=" % (a,b), end="")
    print("{}/{}=".format(a,b), end="")
    print(a//b,'.',end='',sep='')
    r=a%b
    while n1<=n2:
        print((r*10)//b,end='')
        r=(r*10)%b
        n1+=1

if __name__=="__main__":
    qiuxiaoshu2()
    # qiuxiaoshu1()