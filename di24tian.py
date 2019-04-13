def bidaxiao1():
    max_int=0
    for i in range(1,11):
        x=float(input("请输入第%s个数:" % i))
        if x>max_int:
            max_int=x
    print("最大的数是",max_int)

def jiajianhunhe1():
    ans=20
    for i in range(2,20,3):
        ans-=i
        print(i+3,ans)
        if i>ans:
            break
    print(i+3,ans)

def jiajianhunhe2():
    ans = 20
    i = 2
    while(i<ans):
        ans -= i
        i += 3
        print(i, ans)
    
    print(i, ans)

def bidaxiao2():
    n=int(input("您要在几个数中求最小值："))
    # print("请输入第1个数：")
    x=float(input("请输入第1个数："))
    min_int=x
    for i in range(2,n+1):
        # print("请输入第%s个数" % i)
        x=float(input("请输入第%s个数:" % i))
        if x<min_int:
            min_int=x
    print("最小的数是",min_int)

if __name__=="__main__":
    # bidaxiao2()
    bidaxiao1()
    # jiajianhunhe2()
    # jiajianhunhe1()