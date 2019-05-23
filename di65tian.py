def sushu1(x):
    if x<=1:
        return 0
    if x==2:
        return 1
    for i in range(2,x):
        if x%i==0:
            return 0
    return 1

def sushu2():
    n=eval(input("n="))
    while n<4:
        n=eval(input("(请输入一个≥4的整数!!!) n="))
    for i in range(4,n+1,2):
        for j in range(2,i):
            if sushu1(j) and sushu1(i-j):
                print(i,'=',j,'+',i-j)
                break
    if i==j:
        print("验证失败！")

def lianjiachengxu1(n):
    sum_int=0
    for i in range(1,n+1):
        sum_int+=i
    return sum_int

def lianjiachengxu2():
    ans=0
    n=eval(input("n="))
    for i in range(1,n+1):
        ans+=lianjiachengxu1(i)
    print(ans)

def prime1(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

def superprime2(n):
    while n>0:
        if prime1(n):
            n=n//10
        else:
            return 0
    return 1

def prime3():
    ans=0
    a=[]
    for i in range(100,1000):
        if superprime2(i):
            ans+=1
            a.append(str(i))
            # print(i,end='--->')
    print('--->'.join(a))
    print("一共有{}个超级素数。".format(ans))

if __name__=="__main__":
    prime3()
    # lianjiachengxu2()
    # sushu2()