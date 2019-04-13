def jiajiale():
    sum_BOX=0
    BOX=eval(input("请输入一个整数："))
    while BOX!=0:
        a=BOX%10
        sum_BOX+=a
        BOX=BOX//10
    print("各个位数之和：",sum_BOX)

def erjinzhidezhuanhuan():
    sum_int=0
    n=int(input("n="))
    while n!=0:
        a=n%2
        sum_int+=a
        print(a,end='')
        n=n//2
    print()
    print(sum_int)

def shuweishu():
    sum_fox=0
    n=eval(input("n="))
    while n>0:
        sum_fox+=1
        n=n//10
    print("位数是：%s" % sum_fox)

if __name__=="__main__":
    shuweishu()
    # erjinzhidezhuanhuan()
    # jiajiale()