def bidaxiao():
    # print("a,b=",end='')
    # a=input()
    a=int(input("a="))
    # b=input()
    b=int(input("b="))
    if a<=b:
        print(a,b)
    else:
        print(b,a)

def bidaxiao2():
    a=int(input("a="))
    b=int(input("b="))
    if a>b:
        t=a
        a=b
        b=t
    print(a,b)

def shuchuzimushunxu():
    ch=input("请输入一个小写字母：")
    # sum=0
    if ch>='a' and ch<='z':
        sum=ord(ch)-ord('a')+1
    else:
        sum=27
    print("该字母在字母表中的顺序是：",sum)

def diantichengxu():
    n=int(input("当前电梯所停在的楼层层数是："))
    n1=int(input("需要服务的楼层一的楼层层数是："))
    n2=int(input("需要服务的楼层二的楼层层数是："))
    len1=abs(n-n1)
    len2=abs(n-n2)
    if len1>len2:
        print("要先去",n2,"层。")
    else:
        print("要先去",n1,"层。")

if __name__=="__main__":
    diantichengxu()
    # shuchuzimushunxu()
    # bidaxiao2()
    # bidaxiao()