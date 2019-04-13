def zimuzhuanhuan():
    print("输入a-z:",end='')
    n=input()
    # n=int(n)
    print(n.upper())

def zimubianshuzi():
    ch=input()
    n=ord(ch)
    print(ch,' ',n)

def yigebiansange():
    ch=input()
    b=ord(ch)
    a=chr(b-1)
    c=chr(b+1)
    b=ch
    print(a+b+c)

def yigebianwuge():
    ch=input()
    c=ord(ch)
    a=chr(c-2)
    b=chr(c-1)
    d=chr(c+1)
    e=chr(c+2)
    c=ch
    print(a+b+c+d+e)

def yixiaobianwuda():
    ch=input()
    c=ord(ch)
    a=chr(c-2)
    A=a.upper()
    b=chr(c-1)
    B=b.upper()
    d=chr(c+1)
    D=d.upper()
    e=chr(c+2)
    E=e.upper()
    c=ch
    C=c.upper()
    print(A+B+C+D+E)

def panduan1():
    print("IQ:",end='')
    iq=input()
    iq=int(iq)
    if iq>=140 :
        print("恭喜您，您是天才！")
    if iq<140 :
        print("哇哦！您的智商过低，该好好学习哦！")

def dati():
    print("3+2=",end='')
    daan=input()
    daan=int(daan)
    if daan==5:
        print("您答对了！")
    if daan!=5:
        print("您答错了!")

def dati1():
    sum=0
    print("1,3+5=",end='')
    daan=input()
    daan=int(daan)
    if daan==8:
        sum+=1

    print("2,7+5=",end='')
    daan=input()
    daan=int(daan)
    if daan==12:
        sum+=1

    print("3,9+17=",end='')
    daan=input()
    daan=int(daan)
    if daan==26:
        sum+=1

    print("4,42+9=",end='')
    daan=input()
    daan=int(daan)
    if daan==51:
        sum+=1

    print("5,16*15=",end='')
    daan=input()
    daan=int(daan)
    if daan==240:
        sum+=1

    print("你一共答对了：",sum,"道题。")
    if sum==5:
        print("你真厉害！")
    if sum!=5:
        print("你还要加油哦！")




if __name__=="__main__":
    dati1()
    # dati()
    # panduan1()
    # yixiaobianwuda()
    # yigebianwuge()
    # yigebiansange()
    # zimubianshuzi()
    # zimuzhuanhuan()