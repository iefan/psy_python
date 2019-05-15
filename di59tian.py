def sheidasheixiao():
    tj=[0]*4
    for make in range(1,5):
        for boli in range(1,5):
            for mani in range(1,5):
                nike=10-(make+boli+mani)
                if make*boli*mani*nike==1*2*3*4:
                    tj[0]=[make==1,boli==4,mani==3,nike==2].count(True)==2
                    tj[1]=[make==4,boli==1,mani==2,nike==3].count(True)==2
                    tj[2]=[make==2,boli==4].count(True)==1
                    tj[3]=[make==1,boli==3,mani==2,nike==4].count(True)==2
                    if tj[0] and tj[1] and tj[2] and tj[3]:
                        print("马克：{}".format(make))
                        print("波力：{}".format(boli))
                        print("马尼：{}".format(mani))
                        print("尼克：{}".format(nike))

def jiafajisuan():
    a=[0]*3
    ans=0
    for i in range(3):
        a[i]=eval(input("请输入一个整数："))
    ans+=a[0]*(a[0]>a[1] and a[0]>a[2])
    ans+=a[1]*(a[1]>a[0] and a[1]>a[2])
    ans+=a[2]*(a[2]>a[0] and a[2]>a[1])
    print(ans)

def panduanzhanjia():
    for foxlaoshi in range(1,4):
        for nike in range(1,4):
            for glair in range(1,4):
                if [nike==2,glair==3,foxlaoshi==3,glair!=3].count(True)==3:
                    if nike*foxlaoshi*glair==1*2*3:
                        print("狐狸老师：{}".format(foxlaoshi))
                        print("尼克：{}".format(nike))
                        print("格莱尔：{}".format(glair))

if __name__=="__main__":
    panduanzhanjia()
    # jiafajisuan()
    # sheidasheixiao()