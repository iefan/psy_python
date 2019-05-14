def shaixuanfa():
    a=[0]*101
    for i in range(2,101):
        a[i]=True
    a[0],a[1]=False,False
    i=1
    while i<100:
        i+=1
        if a[i]:
            for j in range(2,(100//i)+1):
                # print(i,'----',j)
                a[i*j]=False
    num=0
    for i in range(1,101):
        if a[i]:
            print(' '*6,i,end='')
            num+=1
            if num%10==0:
                print()
    print()
    print("100以内素数(质数)的个数：{}".format(num))

def zuiduandeshudeweishu():
    s1="study"
    s2="student"
    ans=0
    i=0
    while i<len(s1) and i<len(s2):
        if s1[i]==s2[i]:
            ans+=1
        i+=1
    print(ans)

def caihuluoboshu():
    a=[True]*50
    for i in range(50):
        if i%2!=1:
            a[i]=False
        if i%3!=2:
            a[i]=False
        if i%7!=5:
            a[i]=False
    for i in range(50):
        if a[i]:
            print(i)

if __name__=="__main__":
    caihuluoboshu()
    # zuiduandeshudeweishu()
    # shaixuanfa()