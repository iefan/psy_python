def dayin():
    for i in range(1,5):
        print((4-i)*' '+i*'* ')

def jiefangcheng():
    sum_int=0
    x=0
    y=0
    for x in range(0,19):
        for y in range(0,19):
            if x+y==18:
                print('x=',x,' ','y=',y)
                sum_int+=1
    print("共有{}组解。".format(sum_int))

def digui1(f):
    if f>=4:
        return digui1(f-1)+digui1(f-3)
    else:
        if f==1 or f==2:
            return 1
        if f==3:
            return 2

def digui2():
    n=eval(input('n='))
    for i in range(1,n+1):
        print(digui1(i),end='  ')
        
if __name__=="__main__":
    digui2()
    # jiefangcheng()
    # dayin()