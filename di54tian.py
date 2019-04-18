def laoyongzhuoxiaoji():
    a=[0]*6
    for i in range(1,6):
        a[i]=i
    i=1
    print(i,':  ',end='')
    for j in range(1,6):
        print(a[j],end='  ')
    print()
    for i in range(2,11):
        for j in range(0,5):
            a[j]=a[j+1]
        a[5]=a[0]
        print(i,':  ',end='')
        for j in range(1,6):
            print(a[j],end='  ')
        print()

def daozhedashu():
    b=[0]*4
    for i in range(0,2):
        b[i],b[i+2]=eval(input("请输入两个数(注意:每个数之间要用逗号连接！！)："))
    for i in range(3,-1,-1):
        print(b[i])

def zhaoyaoshi():
    a=[4,3,-1,5,1,2]
    print("老师",end='')
    i=a[0]
    while a[i]!=-1:
        print('---->',i,end='')
        i=a[i]
    print('---->',i)
    print()
    print("钥匙找到了！")

if __name__=="__main__":
    zhaoyaoshi()
    # daozhedashu()
    # laoyongzhuoxiaoji()