def bitechaoshi():
    num=0
    flag=True
    sum_int=0.0
    # n=eval(input("n="))
    while flag:
        sum_one=0.0
        n=eval(input("n="))
        while n!=0:
            # n=eval(input("n="))
            if n==-1:
                flag=False
                break
            sum_one+=n
            n=eval(input("n="))
        print("当前同学应付的货款：{}".format(sum_one))
        if sum_one!=0:
            num+=1
        sum_int+=sum_one
    print("今天的营业额：{}".format(sum_int))
    print("今天换购的人数：{}".format(num))

def jiachenghunhe():
    ans=0
    i=1
    while i<=3:
        p=1
        j=1
        while j<=5:
            p*=j
            j+=1
        ans+=p
        i+=1
    print(ans)

def yinshufenjieshi():
    n=eval(input("n="))
    print(n,'=',end='')
    i=2
    while n!=1:
        while n%i==0:
            print(i,end='')
            n=n//i
            if n!=1:
                print('x',end='')
        i+=1

if __name__=="__main__":
    yinshufenjieshi()
    # jiachenghunhe()
    # bitechaoshi()