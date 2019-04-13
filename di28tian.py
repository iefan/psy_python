def panduanTrueheFalse1():
    for i in range(1,5):
        xiaotou=[]
        xiaotou.append(i!=1)
        xiaotou.append(i==3)
        xiaotou.append(i==4)
        xiaotou.append(i!=4)
        if xiaotou.count(True)==3:
            print("小偷是：",chr(64+i))
            break

def jisuan():
    n=int(input())
    ans=0
    for i in range(1,n):
        suan=[]
        suan.append(i%3==0)
        suan.append(i%5==0)
        suan.append(i%2==0)
        if suan.count(True)==2:
            ans+=1
    print(ans)

def panduanTrueheFalse2():
    for i in range(1,4):
        box=[]
        box.append(i==2)
        box.append(i!=2)
        box.append(i!=3)
        if box.count(True)==1:
            # print(i)
            break
    if i==1:
        print("狐狸老师做的。")
    elif i==2:
        print("尼克做的。")
    else:
        print("格莱尔做的。")

def panduanTrueheFalse3():
    for i in range(1,5):
        fox=[]
        fox.append(i!=1)
        fox.append(i==4)
        fox.append(i!=3)
        fox.append(i==1)
        if fox.count(True)==1:
            break
    if i==1:
        print("甲是主谋。")
    if i==2:
        print("乙是主谋。")
    if i==3:
        print("丙是主谋。")
    if i==4:
        print("丁是主谋。")

if __name__=="__main__":
    panduanTrueheFalse3()
    # panduanTrueheFalse2()
    # jisuan()
    # panduanTrueheFalse1()