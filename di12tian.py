def kongrongrangli1():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c=")) 
    if a<=b and a<=c:
        min_num=a
    if b<=a and b<=c:
        min_num=b
    if c<=a and c<=b:
        min_num=c
    print("min_num=",min_num)

def kongrongrangli2():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    if a<b:
        min_num=a
    else:
        min_num=b
    if c<min_num:
        min_num=c
    print("min_num=",min_num)

def kongrongrangli3():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    min_num=a
    if b<min_num:
        min_num=b
    if c<min_num:
        min_num=c
    print("min_num=",min_num)

def sanshuqiuda():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    max_num=a
    if b>max_num:
        max_num=b
    if c>max_num:
        max_num=c
    print("max_num=",max_num)

def sishuqiuda():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    d=int(input("d="))
    max_num=a
    if b>max_num:
        max_num=b
    if c>max_num:
        max_num=c
    if d>max_num:
        max_num=d
    print("max_num=",max_num)

if __name__=="__main__":
    # sishuqiuda()
    # sanshuqiuda()
    kongrongrangli3()
    # kongrongrangli2()
    # kongrongrangli1()