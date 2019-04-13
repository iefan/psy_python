def huiwenshu():
    num=int(input("请输入一个整数："))
    m=0
    n=num
    while n>0:
        m=m*10+n%10
        # n=int(n/10)
        n=n//10
        # print("="*10, m, n)
    if num==m:
        print("%s是回文数。" % num)
    else:
        print("%s不是回文数。" % num)
    # print(num,m)

def baigexiangtong():
    ans=0
    for i in range(100,130):
        bai=i//100
        ge=i%10
        if bai==ge:
            ans+=1
            print(i)
    print(ans)

def wanquanshu():
    shu=[]
    n1=int(input("您要在1~几中求完全数："))
    for n in range(1,n1+1):
        print(n)
        sum_int=0   
        for i in range(1,n//2+1):
            if n%i==0:
                sum_int+=i
        if sum_int==n:
            shu.append(n)
    print(shu)
            # print("%s是完全数" % n)
        # else:
            # print("%s不是完全数" % n)

if __name__=="__main__":
    wanquanshu()
    # baigexiangtong()
    # huiwenshu()