from random import randint
import winsound
def kousuandashi():
    sum_int=0
    for i in range(10):
        print(i+1,":",end=' ')
        x=randint(0,99)
        y=randint(0,99)
        fuhao=randint(0,1)
        if fuhao==0:
            ans=int(input("%s+%s=" % (x,y)))
            if ans==x+y:
                sum_int+=10
                print("对！")
            else:
                print("错！")
        else:
            if x>y:
                ans=int(input("%s-%s=" % (x,y)))
                if ans==x-y:
                    sum_int+=10
                    print("对！")
                else:
                    print("错！")
            else:
                box=x
                x=y
                y=box
                ans=int(input("%s-%s=" % (x,y)))
                if ans==x-y:
                    sum_int+=10
                    print("对！")
                else:
                    print("错！")
    print("得分：",sum_int)

def kousuandashi2():
    sum_int=0
    for i in range(10):
        print(i+1,":",end=' ')
        x=randint(0,99)
        y=randint(0,99)
        fuhao=randint(0,1)
        if fuhao==0:
            dubiaodashi([x, "JIA", y, "DENGYU"])
            ans=int(input("%s+%s=" % (x,y)))
            if ans==x+y:
                sum_int+=10
                print("对！")
                dubiaodashi(["正确"])
            else:
                print("错！")
                dubiaodashi(["答案", x+y, "错误"])
        else:
            if x>y:
                ans=int(input("%s-%s=" % (x,y)))
            else:
                box=x
                x=y
                y=box
                ans=int(input("%s-%s=" % (x,y)))
            if ans==x-y:
                sum_int+=10
                print("对！")
            else:
                print("错！")
    print("得分：",sum_int)

def jiaohuanshuwei():
    ans=0
    for i in range(50,61):
        x=i%10
        y=int(i/10)
        n=x*10+y
        if i+n<100:
            ans+=1
            print(i,n)
    print(ans)

def shitoujisndaobu():
    MAX=10
    countm=0
    countn=0
    countpingju=0
    for i in range(0,MAX):
        m=randint(1,3)
        print("第%s局，请你出招：" % (i+1),end=' ')
        print("1，剪刀","2，石头","3，布")
        n=int(input())
        if n<1 or n>3:
            print("请输入3以内的数(包括3)！此局无效！")
        else:
            if m-n==-1 or m-n==2:
                print("你赢了！")
                countn+=1
            elif m-n==1 or m-n==-2:
                print("好遗憾！你输了！")
                countm+=1
            else:
                print("平局！")
                countpingju+=1
    print('-------------------------------------------------')
    print("计算机赢%s次" % countm)
    print("你赢%s次" % countn)
    print("平局%s次" % countpingju)

def dubiaodashi(lstname):
    for item in lstname:
        if type(item) == type(1):
            dushu(item)
        else:
            winsound.PlaySound("./NumberVoc/%s.wav" % item, winsound.SND_FILENAME)

def dushu(x):
    if x<0 or x>=10000:
        print("请输入0~9999以内的整数！")
    # x = randint(0, 999)
    qian = x//1000
    bai = x%1000//100
    shi = x%100//10
    ge = x%10
    lstSound = []
    # print(x)
    if qian != 0:
        lstSound.append(str(qian))
        lstSound.append("QIAN")
    if qian != 0 and bai == 0 and (shi!=0 or ge !=0):
        lstSound.append("0")
    if bai != 0:
        lstSound.append(str(bai))
        lstSound.append("BAI")
    if bai != 0 and shi == 0 and ge != 0:
        lstSound.append("0")
    if shi != 0:
        if shi == 1 and bai==0:
            lstSound.append("SHI")
        else:
            lstSound.append(str(shi))
            lstSound.append("SHI")
    if ge != 0:
        lstSound.append(str(ge))

    for item in lstSound:
        tmpsoundname = "./NumberVoc/%s.wav" % item
        winsound.PlaySound(tmpsoundname, winsound.SND_FILENAME)

def tingsuan():
    # x = randint(0, 999)
    x = int(input("请输入一个0~999之间的整数："))
    y = int(input("请输入一个0~999之间的整数："))
    
    dushu(x)
    winsound.PlaySound("./NumberVoc/%s.wav" % "JIA", winsound.SND_FILENAME)
    dushu(y)
    winsound.PlaySound("./NumberVoc/%s.wav" % "DENGYU", winsound.SND_FILENAME)

    ans = int(input("%s+%s=" % (x,y)))
    if ans == x+y:
        print("对！")
        winsound.PlaySound("./NumberVoc/%s.wav" % "正确", winsound.SND_FILENAME)
    else:
        winsound.PlaySound("./NumberVoc/%s.wav" % "错误", winsound.SND_FILENAME)
        winsound.PlaySound("./NumberVoc/%s.wav" % "答案", winsound.SND_FILENAME)
        dushu(x+y)


if __name__=="__main__":
    # dubiaodashi([2,"JIA",3,"DENGYU"])
    # dushu(101)
    # tingsuan()
    # shitoujisndaobu()
    # jiaohuanshuwei()
    kousuandashi2()
    # kousuandashi()