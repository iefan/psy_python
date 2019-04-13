def jiaogucaixiang(num=0):
    count=0
    if num == 0:
        x=eval(input("请输入一个整数："))
    else:
        x = num
    while x!=1:
        print(x,"--->",end='')
        if x%2!=0:
            x=x*3+1
        else:
            x=x//2
        count+=1
    print(x)
    # print()
    print("步数：",count)
    
def printjiaogu():
    for i in range(1, 10):
        jiaogucaixiang(i)

def leijisqi():
    s=0
    n=eval(input("n="))
    x=n
    while x>=1:
        # print(x, end=" ")
        if n%x==0:
            s+=1
            print(x, end=" ")
        x-=1
    print()
    print(s)

def jiajianhunhe():
    sum_int=2020
    n=eval(input("n="))
    i=1
    while i<=n:
        if i%2==1:
            sum_int-=i
        else:
            sum_int+=i
        i+=1
    print(sum_int)

if __name__=="__main__":
    jiajianhunhe()
    # leijisqi()
    # printjiaogu()
    # jiaogucaixiang()