def runnianpingnian():
    print("n=",end='')
    n=input()
    n=int(n)
    if n%100==0:
        if n%400==0:
            print("闰年。")
        else:
            print("平年。")
    else:
        if n%4==0:
            print("闰年。")
        else:
            print("平年。")

def kaiguandeng1():
    light=True
    light=not light
    light=not light
    light=not light
    light=not light
    light=not light
    if light:
        print("灯亮。")
    else:
        print("灯灭。")

def kaiguandeng2():
    n=input()
    n=int(n)
    if n%2==0:
        print("灯灭。")
    else:
        print("灯亮。")

def qishanmen():
    s=0
    door1=door2=door3=door4=door5=door6=door7=True

    door2=not door2
    door4=not door4
    door6=not door6

    door3=not door3
    door6=not door6

    if door1:
        s+=1
    if door2:
        s+=1
    if door3:
        s+=1
    if door4:
        s+=1
    if door5:
        s+=1
    if door6:
        s+=1
    if door7:
        s+=1
    print("s=",s)


if __name__ == "__main__":
    qishanmen()
    # kaiguandeng2()
    # kaiguandeng1()
    # runnianpingnian()