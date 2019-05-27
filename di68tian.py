def search1(b,len_int,key):
    high=len_int-1
    low=0
    mid=len_int//2
    while high>=low:
        mid=(high+low)//2
        print(b[mid])
        if b[mid]==key:
            return b[mid]
        else:
            if b[mid]>key:
                high=mid-1
            else:
                low=mid+1
    return 0

def search2():
    MAX=100
    a=[0]*MAX
    for i in range(0,MAX):
        a[i]=i+1
    n=eval(input("请输入一个1~100的数："))
    print()
    print("以下是用二分法猜{}的过程 ⬇".format(n))
    while n<1 or n>100:
        n=eval(input("n="))
    if search1(a,MAX,n):
        print("成功！")
    else:
        print("失败！")

def lianjiachx1(b,n):
    sum_int=0
    for i in range(0,4):
        if b[i]<n:
            continue
        if b[i]==n:
            break
        sum_int+=b[i]
    return sum_int

def lianjiachx2():
    a1=[8,2,-3,4]
    a2=[90,-1,10,100]
    ans=0
    ans+=lianjiachx1(a1,0)
    ans+=lianjiachx1(a2,10)
    print(ans-4)

def chazhaoxingming1(b,key):
    MAX=5
    ft=False
    for i in range(0,MAX):
        if key==b[i]:
            ft=True
            break
    return ft

def chazhaoxingming2():
    a=["潘晟尧","潘湘飞","赵小娜","格莱尔","尼克","马克","马尼","波力"]
    name=input("请输入一个名字：")
    if chazhaoxingming1(a,name):
        print("{}是小小播音员。".format(name))
    else:
        print("{}不是小小播音员。".format(name))

if __name__=="__main__":
    chazhaoxingming2()
    # lianjiachx2()
    # search2()