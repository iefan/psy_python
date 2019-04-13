def daxinghao():
    for i in range(1,6):
        for _ in range(1,i+1):
            print('*',end='')
        print()

def daxinghao2():
    for i in range(1,6):
        print(' '*(5-i),end='')
        for _ in range(1,i*2):
            print('*',end='')
        print() 

def daxinghao3():
    t=0
    for i in range(1,5):
        print(' '*0,end='')
        for _ in range(1,i+1):
            print(t,end='')
            t+=1
        print()

if __name__=="__main__":
    daxinghao3()
    # daxinghao2()
    # daxinghao()