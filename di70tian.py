def show1(n):
    if n!=1:
        show1(n-1)
    print(' ',n,end='')

def show2():
    n=100
    show1(n)

def feibonaqishulie1(n):
    if n==0 or n==1:
        return 1
    else:
        return feibonaqishulie1(n-1)+feibonaqishulie1(n-2)

def feibonaqishulie2():
    print(feibonaqishulie1(feibonaqishulie1(4)))

def shudaoxushu1(n):
    if n<10:
        print(n)
    else:
        print(n%10,end='')
        shudaoxushu1(n//10)

def shudaoxushu2():
    n=eval(input("n="))
    shudaoxushu1(n)

if __name__=="__main__":
    shudaoxushu2()
    # feibonaqishulie2()
    # show2()