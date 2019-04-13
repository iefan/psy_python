def woniupashu():
    t=0
    i=0
    while 1:
        t+=1
        i+=3
        if i>=17:
            break
            # print(i)
        t+=1
        i-=1
    print("需要%s分钟" % t)

def dayinshuzi():
    i=10
    n=int(input("n="))
    while True:
        print(i,end=' ')
        if i<=n:
            break
        i-=3

def qiupingjunfen():
    i=0
    sum_int=0.0
    n=int(input())
    # n = 0
    while n!=-1:
        i+=1
        sum_int+=n
        n=int(input())
        # n=int(input())
    if i!=0:
        pjf=sum_int/i
        print("平均分：",pjf)

if __name__=="__main__":
    qiupingjunfen()
    # dayinshuzi()
    # woniupashu()