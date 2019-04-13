from random import randint,sample

def paixu1():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    if a>b:
        temp=a
        a=b
        b=temp
    if a>c:
        temp=a
        a=c
        c=temp
    if b>c:
        temp=b
        b=c
        c=temp
    print(a,b,c)

def jisuan():
    y=0
    x=int(input("x="))
    if x<0:
        y=x
    else:
        y=x*x+(x+1)*(x+1)
    print("y=",y)

def paixu2():
    a1=input("a1=")
    a2=input("a2=")
    a3=input("a3=")
    a4=input("a4=")
    if a1>a2:
        temp=a1
        a1=a2
        a2=temp
    
    if a1>a3:
        temp=a1
        a1=a3
        a3=temp
    
    if a1>a4:
        temp=a1
        a1=a4
        a4=temp
    
    if a2>a3:
        temp=a2
        a2=a3
        a3=temp
    
    if a2>a4:
        temp=a2
        a2=a4
        a4=temp
    
    if a3>a4:
        temp=a3
        a3=a4
        a4=temp
    print(a1,a2,a3,a4)

def choujiang():
    a=randint(1,10)
    b=int(input("请输入一个1~10中的数字进行抽奖："))
    if b==a:
        print("中奖了！奖金10元。")
    else:
        print("没中奖，请付费2元。中奖号码是：",a)

def jisuan1():
    a=randint(10,99)
    b=randint(10,99)
    print(a,'x',b,'=',end='')
    n=int(input())
    if n==a*b:
        print("对。")
    else:
        print("错。")

def shuAB(a1,a2,a3,a4):
    # a1,a2,a3,a4=sample(range(0,10),4)
    # b1=int(input("b1="))
    # b2=int(input("b2="))
    # b3=int(input("b3="))
    # b4=int(input("b4="))
    b1, b2, b3, b4 = map(int, input().split(' '))
    A_num=0
    B_num=0
    if b1==a1:
        A_num+=1
    else:
        if b1==a2 or b1==a3 or b1==a4:
            B_num+=1
    if b2==a2:
        A_num+=1
    else:
        if b2==a1 or b2==a3 or b2==a4:
            B_num+=1
    if b3==a3:
        A_num+=1
    else:
        if b3==a1 or b3==a2 or b3==a4:
            B_num+=1
    if b4==a4:
        A_num+=1
    else:
        if b4==a1 or b4==a2 or b4==a3:
            B_num+=1
    print("结果是：",A_num,"A",B_num,"B")
    return(A_num)
    # print("原数是：",a1,a2,a3,a4)

def caishuzi():
    a1,a2,a3,a4=sample(range(0,10),4)
    print("第一次猜：")
    A_num = shuAB(a1,a2,a3,a4)
    if A_num==4:
        print("你一次就猜成功了！")
        print("原数是：",a1,a2,a3,a4)
        return

    print("第二次猜：")
    A_num = shuAB(a1,a2,a3,a4)
    if A_num==4:
        print("你两次就猜成功了！")
        print("原数是：",a1,a2,a3,a4)
        return

    print("第三次猜：")
    A_num = shuAB(a1,a2,a3,a4)
    if A_num==4:
        print("你三次就猜成功了！")
        print("原数是：",a1,a2,a3,a4)
        return

    print("第四次猜：")
    A_num = shuAB(a1,a2,a3,a4)
    if A_num==4:
        print("你四次就猜成功了！")
        print("原数是：",a1,a2,a3,a4)
        return

    print("第五次猜：")
    A_num = shuAB(a1,a2,a3,a4)
    if A_num==4:
        print("你五次就猜成功了！")
        print("原数是：",a1,a2,a3,a4)
        return

    print("第六次猜：")
    A_num = shuAB(a1,a2,a3,a4)
    if A_num==4:
        print("你六次就猜成功了！")
        print("原数是：",a1,a2,a3,a4)
        return

    print("第七次猜：")
    A_num = shuAB(a1,a2,a3,a4)
    if A_num==4:
        print("你七次就猜成功了！")
        print("原数是：",a1,a2,a3,a4)
        return

    print("="*20)
    print("你失败了。")
    print("原数是：",a1,a2,a3,a4)

    

    
if __name__=="__main__":
    caishuzi()
    # shuAB(3,7,6,8)
    # jisuan1()
    # choujiang()
    # paixu2()
    # jisuan()
    # paixu1()