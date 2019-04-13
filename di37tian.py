def hudiexiaoying():
    n=1
    n1=n-0.01
    n2=n+0.01
    print("   ",n1,end='')
    print("    ",n2)
    i=1
    while i<=15:
        n1*=n1
        n2*=n2
        print(i," ",n1," ",n2)
        i+=1

def qiumochu3dengyuyideshu():
    s=0
    x=1
    n=eval(input())
    while x<=n:
        if x%3==1:
            s+=x
            # print(s,x)
        x+=1
    print(s)

def qiuxingcunshibingderenshu():
    i=1000
    while True:
        if i%3==2 and i%5==4 and i%7==6:
            break
        i+=1
    print(i)

if __name__=="__main__":
    qiuxingcunshibingderenshu()
    # qiumochu3dengyuyideshu()
    # hudiexiaoying()