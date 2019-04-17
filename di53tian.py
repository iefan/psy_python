def zhuomicang():
    a=[0]*11
    for i in range(1,11):
        a[i]=True
    i=10
    a[i]=False
    cishu=1
    while cishu<=1000:
        i=(i+cishu)%10
        if i==0:
            i=10
        a[i]=False
        cishu+=1
    for i in range(1,11):
        if a[i]:
            print(i)

def qiulianjiadeshu():
    a=[0]*10
    for i in range(0,10):
        a[i]=i
    for i in range(1,10):
        a[0]+=a[i]
    ans=a[0]
    print(ans)

def kaiguanmenchangxu():
    num=0
    a=[0]*97
    for i in range(1,97):
        a[i]=False
    for i in range(1,43):
        j=1
        while j<=96:
            if j%i==0:
                a[j]=not a[j]
            j+=1
        # print(a[1:11])
    for i in range(1,97):
        if a[i]:
            num+=1
            # print(num)
    print("共有{}扇。".format(num))

if __name__=="__main__":
    kaiguanmenchangxu()
    # qiulianjiadeshu()
    # zhuomicang()