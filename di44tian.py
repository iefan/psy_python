def baoshuyouxi():
    num,gelaier,nike,n=0,0,0,0
    while n<=1000:
        nike+=1
        if nike>20:
            nike=1
        gelaier+=1
        if gelaier>30:
            gelaier=1
        if gelaier==nike:
            num+=1
        n+=1
    print("尼克和格莱尔报重的数一共有{}个。".format(num))

def lianjianchengxu():
    ans=0
    k=1
    n=eval(input("请输入一个整数："))
    while k<n:
        ans+=2
        n-=k
        k+=10*ans
        print(k,ans,n)
    print(ans)

def baoshuyouxi1():
    x,y,m=eval(input("请输入三个正整数(请用逗号连接)："))
    gelaier,nike,num,n=0,0,0,0
    while n<=m:
        nike+=1
        if nike>x:
            nike=1
        gelaier+=1
        if gelaier>y:
            gelaier=1
        if gelaier==nike:
            num+=1
        n+=1
    print("尼克和格莱尔报重的数一共有{}个。".format(num))

if __name__=="__main__":
    baoshuyouxi1()
    # lianjianchengxu()
    # baoshuyouxi()