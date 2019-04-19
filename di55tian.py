def fenjiezhiyinshu():
    ans=0
    a=[]
    n=eval(input("n="))
    # n=12
    # print(n,'=',1,'x',1,'x',n,sep='',end='')
    # print()
    for i in range(1,n//2+1):
        if n%i==0:
            a.append(i)
    a.append(n)
    # print(a,'=====')

    # lst = []
    for b in a:
        for c in a:
            for d in a:
                if b*c*d==n and c>=b and d>=c:
                    # lst.append([b,c,d])
                    print(n,'=',b,'x',c,'x',d,'    ',(b*c+b*d+c*d)*2,sep='')
                    ans+=1
    # print(lst)
    # for item in lst:
        # print(item)
    print("{}的因数式有{}个。".format(n,ans))

def maopaopaixv():
    a=[0]*6
    for i in range(1,6):
        a[i]=eval(input("请输入一个整数:"))
    for i in range(1,5):
        for j in range(1,6-i):
            if a[j]<a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    for i in range(1,6):
        print(a[i],end='  ')

def shuzudejiafa():
    b=[5,1,2,2,2,5]
    a=[0,0,0,0,0,0]
    i=1
    while i<=b[0]:
        temp=b[i]
        a[temp]+=1
        i+=1
    for i in range(0,b[0]+1):
        print(a[i])

if __name__=="__main__":
    # shuzudejiafa()
    # maopaopaixv()
    fenjiezhiyinshu()