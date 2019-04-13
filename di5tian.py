def jiajianqi():
    x=input()
    x=int(x)
    if x>100:
        x-=10
    if x<100:
        x+=10
    print(x)

def panduanshuzi():
    print("请输入一个数：")
    n=input()
    n=int(n)
    if n%2==0:
        print("它是偶数。")
    if n%2==1:
        print("它是奇数。")

def tiaosheng():
    print("请输入1分钟跳绳次数：")
    n=input()
    n=int(n)
    if n>=200:
        print("跳绳达人！")
    else:
        print("继续努力！")

def jiajianqi1():
    x=input()
    x=int(x)
    if x==10:
        x+=1
    else:
        x-=1
    print("x=",x)

def panduanshuzi2():
    print("请输入一个整数：")
    n=input()
    n=int(n)
    if n%2==1:
        print("奇数。")
    else:
        print("偶数。")


if __name__ == "__main__":
    panduanshuzi2()
    # jiajianqi1()
    # tiaosheng()
    # panduanshuzi()
    #  jiajianqi()
     