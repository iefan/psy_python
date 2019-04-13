def zhuangyuan():
    USER='iefan'
    PSW='psy101220'
    print("用户名：",end='')
    user=input()
    # user=int(user)
    
    if user==USER:
        print("密码：",end='')
        psw=input()
        # psw=int(psw)
        if psw==PSW:
            print("亲爱的小朋友，欢迎你！")
        else:
            print("密码错误！")
    else:
        print("用户名错误!")

def panduandaxiao():
    x,y=0,0
    x=input()
    x=int(x)
    if x<10:
        y=1
    else:
        if x<100:
            y=2
        else:
            y=3
    print(y)

def panduanshuzi():
    print("x=",end='')
    x=input()
    x=int(x)
    if x>0:
        print("正数。")
    else:
        if x==0:
            print("零。")
        else:
            print("负数。")

if __name__ == "__main__":
    panduanshuzi()
    # panduandaxiao()
    # zhuangyuan()