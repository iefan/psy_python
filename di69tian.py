def digui1(n):
    if n==7:
        return 1
    else:
        return digui1(n+1)+1

def digui2():
    print(digui1(1))

def oushu1(n):
    if n==1:
        return 0
    else:
        return oushu1(n-1)+2

def oushu2():
    print(oushu1(10))

def toulan1(n):
    if n!=1:
        t=toulan1(n-1)+5
    else:
        t=0
    return t

def toulan2():
    print(toulan1(4))

if __name__=="__main__":
    toulan2()
    # oushu2()
    # digui2()