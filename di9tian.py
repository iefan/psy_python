def runnianpingnian2():
    # print("n=",end='')
    n=input("请输入一个年份：")
    n=int(n)
    if (n%400==0) or (n%100!=0 and n%4==0):
        print(n,"是闰年。")
    else:
        print(n,"是平年。")

def chufa1():
    x=input()
    x=int(x)
    y=input()
    y=int(y)
    if x>y and y!=0:
        print(x/y)
    else:
        if x!=0:
            print(y/x)

def pinggu1():
    eat=int(input("吃："))    
    sleep=int(input("睡："))
    mood=int(input("心情："))
    if eat>=80 and sleep>=80 and mood>=80:
        print("新三好。")
    else:
        if (eat<80 and sleep>=80 and mood>=80) or (eat>=80 and sleep<80 and mood>=80) or (eat>=80 and sleep>=80 and mood<80):
            print("双优生。")
        
        if (eat<80 and sleep<80 and mood>=80) or (eat>=80 and sleep<80 and mood<80) or (eat<80 and sleep>=80 and mood<80):
            print("单优生。")

        if (eat<80 and sleep<80 and mood<80):
            print("差生。")

if __name__=="__main__":
    pinggu1()
    # chufa1()
    # runnianpingnian2()