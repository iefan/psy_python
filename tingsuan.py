from random import randint
import winsound
import time

def kousuandashi():
    print("="*30)
    print("100以内加减法听算小程序：1.0版")
    print("="*30)
    try:
        numpro = eval(input("\n请输入您要练习的听算题目数量(默认为 3 道)："))
    except:
        numpro = 3
    try:
        numtimes = eval(input("\n请输入您每道题目要听的次数(默认为 2 次)："))
    except:
        numtimes = 2
    print("\n\n下面听算开始，一共  {}  道题，请注意听题：\n".format(numpro))
    lst_pro = []
    for i in range(numpro):
        print("第{}题，请听题。".format(i+1))
        x=randint(0,99)
        y=randint(0,99)
        fuhao=randint(0,1) #0代表加法，1代表减法
        if fuhao==0:
            for _ in range(numtimes):
                dubiaodashi([x, "JIA", y, "DENGYU"])
                time.sleep(1)
            lst_pro.append("{}+{}".format(x,y))            
        else:
            if x>y:
                for _ in range(numtimes):
                    dubiaodashi([x, "JIAN", y, "DENGYU"])
                    time.sleep(1)
                lst_pro.append("{}-{}".format(x,y))  
            else:
                for _ in range(numtimes):
                    dubiaodashi([y, "JIAN", x, "DENGYU"])
                    time.sleep(1)
                lst_pro.append("{}-{}".format(y,x))  
        time.sleep(2)

    input("\n\n回车显示正确答案：")
    print("\n正确答案：\n")
    indx = 0
    for item in lst_pro:
        indx += 1
        print("第{}题：{}={}".format(indx, item, eval(item)))
    input("\n\n按任意键退出......")

def kousuandashi3():
    print("100以内加减法听算小程序：1.0版")
    print("="*20)
    numpro = eval(input("请输入您要练习的听算题目数量："))
    print("\n\n下面听算开始，请注意听题：\n\n")
    sum_int=0
    lst_pro = []
    for i in range(numpro):
        tmplst = []
        print(i+1,":",end=' ')
        x=randint(0,99)
        y=randint(0,99)
        fuhao=randint(0,1) #0代表加法，1代表减法
        if fuhao==0:
            dubiaodashi([x, "JIA", y, "DENGYU"])
            tmplst.append("{}+{}".format(x,y))            
            ans=int(input("%s+%s=" % (x,y)))
        else:
            if x>y:
                dubiaodashi([x, "JIAN", y, "DENGYU"])
                tmplst.append("{}+{}".format(x,y))  
                ans=int(input("%s-%s=" % (x,y)))
            else:
                dubiaodashi([y, "JIAN", x, "DENGYU"])
                tmplst.append("{}+{}".format(y,x))  
                ans=int(input("%s-%s=" % (y,x)))
        tmplst.append(ans)
        lst_pro.append(tmplst)


    print("\n正确答案：\n")
    indx = 0
    for item in lst_pro:
        indx += 1
        print(indx, " : ", item[0], "=", item[1], sep="", end="")
        if eval(item[0]) == item[1]:
            print(" (V)")
            sum_int += 1
        else:
            print(" (X)", "正确答案：", eval(item[0]))
    print("您一共答对了：{}道题目".format(sum_int))


def kousuandashi2():
    print("100以内加减法听算小程序：1.0版")
    print("="*20)
    numpro = eval(input("请输入您要练习的听算题目数量："))
    print("\n\n下面听算开始，请注意听题：\n\n")
    sum_int=0
    for i in range(numpro):
        print(i+1,":",end=' ')
        x=randint(0,99)
        y=randint(0,99)
        fuhao=randint(0,1) #0代表加法，1代表减法
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
                dubiaodashi([x, "JIAN", y, "DENGYU"])
                ans=int(input("%s-%s=" % (x,y)))
            else:
                dubiaodashi([y, "JIAN", x, "DENGYU"])
                ans=int(input("%s-%s=" % (y,x)))
            if ans == abs(x-y):
                print("对！")
                dubiaodashi(["正确"])
                sum_int+=1
            else:
                print("错！")
                dubiaodashi(["答案", abs(x-y), "错误"])

    print("您一共答对了：{}道题目".format(sum_int))

def dubiaodashi(lstname):
    for item in lstname:
        if type(item) == type(1): #如果是数字就读数
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

# def tingsuan():
#     # x = randint(0, 999)
#     x = int(input("请输入一个0~999之间的整数："))
#     y = int(input("请输入一个0~999之间的整数："))
    
#     dushu(x)
#     winsound.PlaySound("./NumberVoc/%s.wav" % "JIA", winsound.SND_FILENAME)
#     dushu(y)
#     winsound.PlaySound("./NumberVoc/%s.wav" % "DENGYU", winsound.SND_FILENAME)

#     ans = int(input("%s+%s=" % (x,y)))
#     if ans == x+y:
#         print("对！")
#         winsound.PlaySound("./NumberVoc/%s.wav" % "正确", winsound.SND_FILENAME)
#     else:
#         winsound.PlaySound("./NumberVoc/%s.wav" % "错误", winsound.SND_FILENAME)
#         winsound.PlaySound("./NumberVoc/%s.wav" % "答案", winsound.SND_FILENAME)
#         dushu(x+y)


if __name__=="__main__":
    # dubiaodashi([2,"JIA",3,"DENGYU"])
    # dushu(101)
    # tingsuan()
    # shitoujisndaobu()
    # jiaohuanshuwei()
    kousuandashi()
    # kousuandashi()