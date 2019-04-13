def feng7biguo1():
    for i in range(1,21):
        if i%7==0 or i%10==7:
            print("过",end=' ')
        else:
            print(i,end=' ')

def feng7biguo2():
    for i in range(1,21):
        if i%7==0 or i%10==7:
            print("过",end=' ')
            continue
        print(i,end=' ')

def dayin7zhi5zhongdejishu():
    for i in range(7,0,-1):
        if i%2==0:
            continue
        print(i,end='')
        if i==1:
            continue
        print(',',end='')

if __name__=="__main__":
    dayin7zhi5zhongdejishu()
    # feng7biguo2()
    # feng7biguo1()