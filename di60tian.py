def luoboyugutou():
    a=[0]*31
    num=0
    k=0
    for i in range(1,31):
        a[i]=0
    i=1
    while num<15:
        if i>30:
            i=1
        if a[i]==0:
            k+=1
        if k==9:
            a[i]=1
            k=0
            num+=1
        i+=1
    print("骨头所在的位置：",end='')
    for i in range(1,31):
        if a[i]==0:
            print(i,end='   ')

def chujiajiehe():
    sum_int=[0]*2
    sum_int[0]=0
    sum_int[1]=1
    n=eval(input('n='))
    for i in range(1,n+1):
        sum_int[1]*=i
        while sum_int[1]%10==0:
            sum_int[1]=sum_int[1]//10
            sum_int[0]+=1
        sum_int[1]%=1000
    ans=sum_int[0]
    print(ans)

def chuquandexiaopengyou():
    M=10
    a=[0]*(M+1)
    for i in range(1,M+1):
        a[i]=i+1
    a[M]=1
    n=eval(input("n="))
    p=M
    for i in range(1,M+1):
        for _ in range(1,n):
            p=a[p]
        print(a[p],end='---->')
        a[p]=a[a[p]]
    print('结束')

if __name__=="__main__":
    chuquandexiaopengyou()
    # chujiajiehe()
    # luoboyugutou()