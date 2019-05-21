def bijiaodaxiao(x,y):
    if x>y:
        MAX=x
    else:
        MAX=y
    return MAX

def diaoyonghanshuyi():
    a=[0]*5
    for i in range(0,5):
        a[i]=eval(input("请输入一个整数："))
    ans=a[0]
    for i in range(1,5):
        ans=bijiaodaxiao(ans,a[i])
    print(ans)

def adeacifang1(a):
    sum_int=1
    for _ in range(1,a+1):
        sum_int*=a
    return sum_int

def adeacifang2():
    n=eval(input("请输入一个整数："))
    ans=adeacifang1(n)
    print(ans)

def qiudaiyousandeyueshudeshu1(a):
    num=0
    for i in range(1,a+1):
        if a%i==0:
            num+=1
    return num

def qiudaiyousandeyueshudeshu2():
    for a in range(1,101):
        if qiudaiyousandeyueshudeshu1(a)==3:
            print(a,end='---->')
    print("没有了")

if __name__=="__main__":
    qiudaiyousandeyueshudeshu2()
    # adeacifang2()
    # diaoyonghanshuyi()