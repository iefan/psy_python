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

def shuxiaoxiezimudegeshu():
    num=[0]*26
    ch1=input()
    i=0
    while i<len(ch1):
        if ch1[i]>='a' and ch1[i]<='z':
            k=ord(ch1[i])-ord('a')
            num[k]+=1
        i+=1
    for i in range(0,26):
        ch2=chr(97+i)
        print(ch2,':',num[i],end='  ',sep='')
        if i%5==4:
            print()

if __name__=="__main__":
    shuxiaoxiezimudegeshu()
    # shuchuzifuchuangeshu()
    # xuanzepaixu()