def fordeqiantao1():
    for _ in range(1,6):
        print('*',end='')

def fordeqiantao2():
    for _ in range(1,4):
        for _ in range(1,6):
            print('*',end='')
        print()

def fordeqiantao3():
    for _ in range(1,4):
        for i in range(1,6):
            print(i,end='')
        print()

def fordeqiantao4():
    for i in range(1,5):
        for _ in range(1,5):
            print(i,end='')
        print()

if __name__=="__main__":
    fordeqiantao4()
    # fordeqiantao3()
    # fordeqiantao2()
    # fordeqiantao1()