def shuchubi():
    a=2
    b=0
    n=1
    while n<=2017:
        if n%2!=0:
            b=round(b+a*1/(n+1),2)
            a-=round(a*1/(n+1),2)
        else:
            a=round(a+b*1/(n+1),2)
            b-=round(b*1/(n+1),2)
        # print("%s====>%.2f:%.2f" % (n,a,b))
        print("{0}====>{1:.1f}:{2:.1f}".format(n,a,b))
        n+=1
    print(a,":",b)

if __name__=="__main__":
    shuchubi()