def dayinxinghao():
    for i in range(2,6):
        print((i-1)*' '+' *')
        for j in range(i-2):
            print(' '*(i-2-j),end='')
            print(' *',end='')
            print('  '*j,end='')
            print(' *')
        print(' *'*i)
    print()

def dayinxinghao1():
    for i in range(2,6):
        for j in range(1,i+1):
            print((i-j)*' ',end='')
            print(' *'*j)

if __name__=="__main__":
    dayinxinghao1()
    # dayinxinghao()