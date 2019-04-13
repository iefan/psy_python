def wangzhailiuwei():
    print("请输入您想点的菜的编号：\n","1","2","3","4","5","6")
    n=int(input())
    if n==1:
        print("寿仙菇。")
    elif n==2:
        print("酒糟鱼。")
    elif n==3:
        print("下山笋。")
    elif n==4:
        print("太师豆腐。")
    elif n==5:
        print("孝子鱼。")
    elif n==6:
        print("猪全福。")
    else:
        print("无此编号的菜。")

def jisuantianshu1():
    year=int(input())
    month=int(input())
    day=int(input())
    if month==1:
        sumday=0
    elif month==2:
        sumday=31
    elif month==3:
        sumday=59
    elif month==4:
        sumday=90
    elif month==5:
        sumday=120
    elif month==6:
        sumday=151
    elif month==7:
        sumday=181
    elif month==8:
        sumday=212
    elif month==9:
        sumday=243
    elif month==10:
        sumday=273
    elif month==11:
        sumday=304
    elif month==12:
        sumday=334
    else:
        print("输入有误！")
        return
    sumday+=day
    if (year%400==0) or (year%4==0 and year%100!=0):
        leap=1
    else:
        leap=0
    if leap==1 and month>2:
        sumday+=1
    # print("从今年一月一号开始，直到今天是",sumday,"天。")   
    print("从%s年1月1号开始，直到%s年%s月%s日是这一年的第" % (year, year, month, day),sumday,"天。")  


def jisuantianshu2():
    year = int(input("year=")) 
    month = int(input("month="))
    day = int(input("day="))
    sumday = 0

    if month > 1:
        sumday += 31
    if month > 2:
        sumday += 28
    if month > 3:
        sumday += 31
    if month > 4:
        sumday += 30
    if month > 5:
        sumday += 31
    if month > 6:
        sumday += 30
    if month > 7:
        sumday += 31
    if month > 8:
        sumday += 31
    if month > 9:
        sumday += 30
    if month > 10:
        sumday += 31
    if month > 11:
        sumday += 30
    if month > 12:
        print("输入错误！！！")
        return

    sumday+=day
    if (year%400==0) or (year%4==0 and year%100!=0):
        leap=1
    else:
        leap=0
    if leap==1 and month>2:
        sumday+=1
    print("从%s年1月1号开始，直到%s年%s月%s日是这一年的第" % (year, year, month, day),sumday,"天。")  

def jisuanqi():
    try:
        x=int(input("请输入第一个数："))
    except:
        print("必须输入一个整数！本程序即将结束。")
        return
    y=int(input("请输入第二个数："))
    f=input("请输入一个运算符：")
    ans=0
    if f=='+':
        ans=x+y
    elif f=='-':
        ans=x-y
    elif f=='*':
        ans=x*y
    elif f=='/':
        if y!=0:
            ans=round(x/y, 1)
        else:
            print("除数不能为0！")
    else:
        print("您输入的符号不是加减乘除中的一个！")
        return
    if f!='/' or y!=0:
        print("得数是：",ans)
    
if __name__ == "__main__":
    # jisuanqi()
    # jisuantianshu2()
    # jisuantianshu1()
    wangzhailiuwei()