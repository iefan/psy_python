def jiaohuan():
    a=10
    b=20
    # t=0
    print("a=",a,"b=",b)
    t=a
    a=b
    b=t
    print("a=",a,"b=",b)

def shuzi():
    b=3
    c=3+1
    a=c*2
    d=100*c+10*b+a
    print("d=",d)

def shushi1():
    a=18
    b=870
    s=a+b
    print(' '*10,a)
    print(' '*4,'+',' '*2,b)
    print(' '*3,"-"*11)
    print(' '*9,s)

def shushi2():
    a=15
    b=3
    c=a-b
    print(' '*4,a)
    print(' '*-1,'-',' '*2,b)
    print("——————————")
    print(' '*4,c)

def zhishu():
    print("请输入人数和平均每人种的树:")
    a=input()
    b=input()
    a=int(a)
    b=int(b)
    s=a*b
    print("总的棵数：",s)

def jiaohuan1():
    print("a,b=")
    a=input()
    b=input()
    a=int(a)
    b=int(b)
    print("a=",a,"b=",b)
    t=a
    a=b
    b=t
    print("a=",a,"b=",b)

def jianfa1():
    a=input()
    b=input()
    c=input()
    s=input()
    a=int(a)
    b=int(b)
    c=int(c)
    s=int(s)
    s-=a
    s-=b
    s-=c
    print("ans=",s)

def mianji1():
    a=input()
    b=input()
    a=int(a)
    b=int(b)
    s=(a+b)*2
    print("周长：",s)
    

def youpiao_benbu(keshu):
    # 本埠
    # keshu = input("请输入您要寄送信件的质量：")
    keshu = int(keshu)
    if keshu <= 100:
        money = (int((keshu-1)/20)+1)*0.8
    elif keshu > 100 and keshu <=2000:
        money = 5*0.8 + int((keshu-1)/100)*1.2

    # print("邮费为：", round(money,1))
    return(round(money, 1))

def youpiao_waibu(keshu):
    # 本埠
    # keshu = input("请输入您要寄送信件的质量：")
    keshu = int(keshu)
    if keshu <= 100:
        money = (int((keshu-1)/20)+1)*1.2
    elif keshu > 100 and keshu <=2000:
        money = 5*1.2 + int((keshu-1)/100)*2.0

    # print("邮费为：", round(money,1))
    return(round(money, 1))

import itertools
def youpiao_benbu_1():
    benbu_moneylst = []
    benbu_keshulst = []
    waibu_moneylst = []
    waibu_keshulst = []
    for keshu in range(1, 401):
        money = youpiao_benbu(keshu)
        if money not in benbu_moneylst:
            benbu_moneylst.append(money)
            benbu_keshulst.append(keshu-1)

        money = youpiao_waibu(keshu)
        if money not in waibu_moneylst:
            waibu_moneylst.append(money)
            waibu_keshulst.append(keshu)


    benbu_keshulst.append(400)
    waibu_keshulst.append(400)
    benbu_keshulst[0] = 0
    # print(benbu_keshulst)
    # print(benbu_moneylst)

    g_lst_value = []
    g_lst_value.extend(benbu_moneylst)
    g_lst_value.extend(waibu_moneylst)


    for i in range(len(benbu_keshulst)-1):
        print(str(benbu_keshulst[i]+1)+"-"+str(benbu_keshulst[i+1])+":", benbu_moneylst[i], waibu_moneylst[i])


    print(g_lst_value, len(g_lst_value))
    # return;

    g_lst_value_2 = []
    for item in g_lst_value:
        g_lst_value_2.append(int(item*10))

    # print(g_lst_value_2, len(g_lst_value_2))
    print('='*20)
    # return

    g_g_g = []
    # for num1 in range(40, 41):
    # 三个面值的邮票
    for num1 in range(0, 120):
        if num1 in [8, 12]:
            continue
        lst4nums = [num1,8,12,0,num1,8,12,0,num1,8,12,0,num1,8,12,0]
        jcounter = 0
        print(lst4nums)
        for jsums in g_lst_value_2:
            for item in itertools.product(lst4nums,repeat= 4):
                if sum(item) == jsums:
                    jcounter += 1
                    break
        if jcounter == 16:
            print("@@@@"*4, [0, num1, 8, 12])
            g_g_g.append([0, num1, 8, 12])
            continue
    # for item in g_g_g:
    #     print(item)
    # return        

    for num1 in range(0, 120):
        if num1 in [8, 12]:
            continue
        flag1 = 0
        for iitteemm in g_g_g:
            if num1 in iitteemm[:2]:
                flag1 = 1
                break
        if flag1 == 1:
            continue
        for num2 in range(num1+1, 121):
            # print(num2)
            if num2 in  [num1, 8, 12]:
                continue
            flag = 0
            for iitteemm in g_g_g:
                if num2 in iitteemm[:2] or num1 in iitteemm[:2]:
                    flag = 1
                    break
            if flag == 1:
                continue
            lst4nums = [num1,num2,8,12,0,num1,num2,8,12,0,num1,num2,8,12,0,num1,num2,8,12,0]
            print(lst4nums)
           
            # print(lst4nums, g_lst_value_2)
            # return
            jcounter = 0
            for jsums in g_lst_value_2:
                for item in itertools.product(lst4nums,repeat= 4):
                    if sum(item) == jsums:
                        jcounter += 1
                        break
            if jcounter == 16:
                print("@@@@"*4, [num1, num2, 8, 12])
                g_g_g.append([num1, num2, 8, 12])
                continue
                
    for item in g_g_g:
        print(item)

    g_g_g_data2 = [[0, 40, 8, 12],
    [2, 48, 8, 12],
    [10, 30, 8, 12],
    [14, 36, 8, 12],
    [16, 44, 8, 12],
    [18, 52, 8, 12],
    [20, 56, 8, 12],
    [22, 38, 8, 12],
    [24, 32, 8, 12],
    [26, 42, 8, 12],
    [28, 46, 8, 12],]
    g_g_g_data = [[0, 40, 8, 12],
    [2, 48, 8, 12],
    [10, 30, 8, 12],
    [14, 36, 8, 12],
    [16, 44, 8, 12],
    [18, 52, 8, 12],
    [20, 56, 8, 12],
    [22, 38, 8, 12],
    [24, 32, 8, 12],
    [26, 42, 8, 12],
    [28, 46, 8, 12],
    [32, 50, 8, 12],
    [36, 64, 8, 12],
    [40, 41, 8, 12],
    [44, 54, 8, 12],
    [52, 68, 8, 12],]  
    print("=="*20,"\n", g_g_g_data, "\n", g_g_g_data2) 


    # for i in itertools.product([1,2,3,4],repeat= 4):
    #     print(i)


if __name__=="__main__":
    youpiao_benbu_1()
    # youpiao_waibu()
    # youpiao_benbu()
    # mianji1()
    # jianfa1()
    # jiaohuan1()
    # zhishu()
    # shushi2()
    # shushi1()
    # shuzi()
    # jiaohuan()

