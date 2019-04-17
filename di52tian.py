def shuchufenshu1():
    a1,a2,a3,a4,a5=eval(input("1~5号的成绩(注意：输入时要用逗号连接！)："))
    n=eval(input("输入学号1~5："))
    if n==1:
        print(a1)
    elif n==2:
        print(a2)
    elif n==3:
        print(a3)
    elif n==4:
        print(a4)
    elif n==5:
        print(a5)
    else:
        print("输入的学号不存在！")

def shuchufenshu2():
    a=[0]*6
    for i in range(1,6):
        a[i]=eval(input("第{}号成绩：".format(i)))
    n=eval(input("输入学号1~5："))
    if n>=1 and n<=5:
        print(a[n])
    else:
        print("输入的学号不存在！")

def a0jiaa9dehe():
    a=[0]*10
    ans=0
    for i in range(0,10):
        # print(a[i],i)
        a[i]=i
    ans=a[0]+a[9]
    print(ans)

def shuchuzuixiao():
    a=[0]*5
    for i in range(0,5):
        a[i]=eval(input("请输入一个正数："))
    min_int=a[0]
    for i in range(1,5):
        if a[i]<min_int:
            min_int=a[i]
    print(min_int)

if __name__=="__main__":
    shuchuzuixiao()
    # a0jiaa9dehe()
    # shuchufenshu2()
    # shuchufenshu1()