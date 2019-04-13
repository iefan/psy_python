def ouyeouye():
    n=input()
    n=int(n)
    if n%3==0:
        if n%5==0:
            print("欧耶欧耶！")

def ouyeouye2():
    n=input()
    n=int(n)
    if n%3==0 and n%5==0:
        print("oye oye!")
    else:
        print("ono ono!")

def sangeshu():
    s=0
    n=input()
    n=int(n)
    if n%3==0 or n%5==0:
        s+=1
    n=input()
    n=int(n)
    if n%3==0 and n%5==0:
        s+=1
    n=input()
    n=int(n)
    if not(n%5==0):
        s+=1
    print("s=",s)

def zhuangyuan1():
    USER=201902
    PSW=951618
    print("用户名：",end='')
    user=input()
    user=int(user)
    print("密码：",end='')
    psw=input()
    psw=int(psw)
    if USER==user and PSW==psw:
        print("亲爱的小朋友，欢迎你！")
    else:
        print("用户名或密码不正确！")

if __name__ == "__main__":
    zhuangyuan1()
    # sangeshu()
    # ouyeouye2()
    # ouyeouye()
    