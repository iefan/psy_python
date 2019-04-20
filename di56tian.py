def xuanzepaixu():
    a=[0]*6
    for i in range(1,6):
        a[i]=eval(input("请输入一个整数："))
    for i in range(1,5):
        t=i
        for j in range(i+1,6):
            if a[j]>a[t]:
                t=j
        if t!=i:
            a[0]=a[i]
            a[i]=a[t]
            a[t]=a[0]
    for i in range(1,6):
        print(a[i],end='  ')

def shuchuzifuchuangeshu():
    num=numa=0
    zifuchuan=input("请输入一个字符串：")
    for i in zifuchuan:
        num+=1
        if i=='.':
            numa+=1
    print(zifuchuan)
    print("字符个数：{}".format(num))
    print("点('.')的个数：{}".format(numa))

if __name__=="__main__":
    shuchuzifuchuangeshu()
    # xuanzepaixu()