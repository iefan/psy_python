def datiangandizhi1():
    tiangan="甲乙丙丁戊己庚辛壬癸"*6
    dizhi="子丑寅卯辰巳午未申酉戌亥"*5
    for i in range(0,60):
        print(tiangan[i]+dizhi[i],end=' ')
        if (i+1)%10==0:
            print()

def daganzhinian2():
    tiangan="甲乙丙丁戊己庚辛壬癸"*6
    dizhi="子丑寅卯辰巳午未申酉戌亥"*5
    ganzhinian=[]
    for i in range(0,60):
        ganzhinian.append(tiangan[i]+dizhi[i])
        # print(ganzhinian)
    # for box in ganzhinian:
    #     print(box,end=' ')
    #     if (ganzhinian.index(box)+1)%10==0:
    #         print()
    # print()
    n26=ganzhinian.index("庚寅")
    n=int(input("请输入您要查询的年份："))
    if n<=2010:
        chazhi=2010-n
        print("%s年是%s年" % (n,ganzhinian[(n26-chazhi)%60]))
    else:
        chazhi=n-2010
        print("%s年是%s年" % (n,ganzhinian[(n26+chazhi)%60]))

if __name__ == "__main__":
    daganzhinian2()
    # datiangandizhi1()    