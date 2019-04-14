def baiqianmaibaiji1():
    print("公鸡",' '*5,"母鸡",' '*5,"小鸡")
    for gongji in range(1,34):
        for muji in range(1,51):
            for xiaoji in range(1,101):
                if (gongji+muji+xiaoji==100) and (abs(gongji*3+muji*2+xiaoji/3-100)<1e-9):
                    print(gongji,' '*5,muji,' '*5,xiaoji)

def baiqianmaibaiji2():
    print("公鸡",' '*5,"母鸡",' '*5,"小鸡")
    for gongji in range(1,34):
        for muji in range(1,51):
            xiaoji=100-muji-gongji
            if (gongji+muji+xiaoji==100) and (abs(gongji*3+muji*2+xiaoji/3-100)<1e-9):
                print(gongji,' '*5,muji,' '*5,xiaoji)

def lianjiachengxu():
    ans=0
    i=1
    while i<=3:
        for j in range(1,6):
            ans+=j
        i+=1
    print(ans)

def qiusanweishu():
    for shi in range(1,8):
        for bai in range(shi+1,9):
            for ge in range(bai+1,10):
                if shi+bai+ge==shi*bai*ge:
                    print(bai*100+shi*10+ge,end='')

def bitetongbi():
    for a4 in range(0,2):
        for a3 in range(0,2):
            for a2 in range(0,2):
                for a1 in range(0,2):
                    n=a4*8+a3*4+a2*2+a1*1
                    print(a4,a3,a2,a1,'B','   ',n,sep='')

def jiapingfang():
    ans=0
    i=1
    while i<=3:
        j=1
        while j<=5:
            ans+=i*i
            j+=1
        i+=1
    print(ans)

def sanweishudejishu():
    count=0
    for b in range(1,8):
        for s in range(0,8):
            for g in range(1,8,2):
                shu=b*100+s*10+g
                print(shu,end='        ')
                count+=1
    print()
    print("个数:%s" % count)

if __name__=="__main__":
    sanweishudejishu()
    # jiapingfang()
    # bitetongbi()
    # qiusanweishu()
    # lianjiachengxu()
    # baiqianmaibaiji2()
    # baiqianmaibaiji1()