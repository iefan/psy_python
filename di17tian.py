def jidianzhong():
    for i in range(1,13):
        print("老狼老狼几点钟？",i,"点钟。")
    print("狼来了！快跑！")

def daxinghao1():
    for i in range(1,6):
        print('*'*i)
    print(i)

def daxinghao2():
    n=12
    for i in range(1,n+1):
        print(' '*(n-i)+'*'+' *'*(i-1))

    for i in range(1,n):
        print(' '*i+'*'+' *'*(n-i-1))

def dazhengfangxing():
    n=5
    print('* '*n)
    for i in range(1,n-1):
        print('*'+'  '*(n-2)+' *'*(i-i+1))
    print('* '*n)

def dapingxingsibianxing():
    m=20
    n=12
    for i in range(1,n+1):
        print(' '*(n-i)+' *'*m)

def liezhengshu2():
    for i in range(1,101):
        print("%3d" % i,end=' ')
        # print("%-3s" % i,end='\t')
        if i%10==0:
            print()

def liezhengshu():
    for j in range(1,11):
        for i in range(1,11):
            print(i+(j-1)*10,end='\t')
        print()


if __name__ == "__main__":
    liezhengshu2()
    # dapingxingsibianxing()
    # dazhengfangxing()
    # daxinghao2()
    # liezhengshu()
    # daxinghao1()
    # jidianzhong()