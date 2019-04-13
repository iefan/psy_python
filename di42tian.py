def paishouyouxi1():
    time=0
    count=1
    foxlaoshi=0
    nike=0
    gelaier=0
    while foxlaoshi+nike+gelaier<9*3:
        flag=False
        time+=1
        if foxlaoshi<9:
            foxlaoshi+=1
            flag=True
        if nike<9 and time%2==0:
            nike+=1
            flag=True
        if gelaier<9 and time%4==0:
            gelaier+=1
            flag=True
        if flag:
            count+=1
    print("观众一共听到了%s声掌声。" % count)

def qiudengbishuliezhihe():
    n=1
    t=2
    ans=0
    while True:
        n*=t
        if n>1e+3:
            break
        ans+=n
        # print(n, ans)
    print(ans)

def paishouyouxi2():
    ans=10
    time=10
    flag=False
    while time<=36:
        # print(time, end=" ")
        flag=False
        if time<=18 and time%2==0:
            flag=True 
        if time<=36 and time%4==0:
            flag=True
        if flag:
            ans+=1
        time+=1
        # print(ans)
    print(ans)

if __name__=="__main__":
    paishouyouxi2()
    # qiudengbishuliezhihe()
    # paishouyouxi1()