def dingdangdingdang():
    for i in range(1,21):
        print(i,end=' ')
        if i%2==0:
            print("叮叮",end='')
            # print()
        if i%3==0:
            print("当当",end='')
        # print()
        if i%2==0 or i%3==0:
            print()

def daoushu():
    for i in range(1,21):
        if i%2==0:
            print('%02d' % i,end=' ')
    print()
    for i in range(1,21):
        if i%2!=0:
            print('%02d' % i,end=' ')

def daoushu1():
    for i in range(100,-1,-2):
        print('%3d' % i,end=' ')
    # print()
    n=int(input("\n你要打印第几个偶数："))
    if n>51:
        print("你所要的偶数不在此范围之内！")
    else:
        # print(100-(n-1)*2)
        print("你要打印的偶数是:",100-(n-1)*2)

        # if i%2==0:
        #     print('%3d' % i,end=' ')


def daoshu():
    n=int(input("n="))
    for i in range(n,0,-1):
        print('%3d' % i,end=' ')
        if (i-1)%10==0:
            print()

def baohuachengxu():
    for i in range(2,6):
        n=60%i
        print("老师报的数是%2s,剩余%s小朋友要表演节目" % (i,n))

if __name__=="__main__":
    daoushu1()
    # baohuachengxu()
    # daoshu()
    # daoushu()
    # dingdangdingdang()