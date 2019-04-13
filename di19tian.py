def leijiaqi():
    sum_int=0
    n=10000
    for i in range(1,(n+1)):
        sum_int+=i
    print("结果是",sum_int)

def qiupingfanghe():
    sum_int=0
    n=5000
    for i in range(1,n+1):
        sum_int+=i*i
    print("结果是",sum_int)

def chengjiahunhe():
    sum_int=0
    n=100
    for i in range(1,n+1):
        sum_int+=i*(i+1)
    print("结果是",sum_int)

def qipanlidexiaomai():
    sum_int=0
    n=1
    for i in range(1,65):
        n=n*2
        sum_int+=n
        print(i,n)
    print("总数：%s" % sum_int)

def jiafa():
    ans=0
    m=int(input("m="))
    n=int(input("n="))
    for i in range(m,n+1,2):
        ans+=i
    print(ans,i)

def jisuanlilv():
    s=84.0
    for i in range(1,5):
        s=round(s*(1+0.05), 2)+15
        print(i,s)

# cc = lambda i : "pass" if i%7==0 or i%10==7 else i
# print(list(map(cc, range(1,21))))  #这两条语句即可完成逢7或尾7喊“过”的小游戏，或者也可以合并为一句即下面一句
# print(list(map(lambda i : "pass" if i%7==0 or i%10==7 else i, range(1,21)))) 
if __name__=="__main__":
    jisuanlilv()
    # jiafa()
    # qipanlidexiaomai()
    # chengjiahunhe()
    # qiupingfanghe()
    # leijiaqi()