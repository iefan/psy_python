def jiamishu1():
    a=input("请输入一个字符串：")
    b=""
    for i in a:
        m1=ord(i)
        if (m1>=65 and m1<=90) or (m1>=97 and m1<=122):
            m2=m1+1
            if (m2>90 and m2<97) or (m2>122):
                m2-=26
            m3=chr(m2)
            b+=m3
        else:
            b+=i
    print("加密后的字符串：",b)

def shukonggeshu():
    a=input("请输入一个字符串：")
    box=0
    for i in a:
        if i==' ':
            box+=1
    print("{}里面的空格有{}个。".format(a,box))

def jiamishu2():
    a=input("请输入一个字符串：")
    b=""
    for i in a:
        m1=ord(i)
        if (m1>=65 and m1<=90) or (m1>=97 and m1<=122):
            m2=m1+3
            if (m2>90 and m2<97) or (m2>122):
                m2-=26
            m3=chr(m2)
            b+=m3
        else:
            b+=i
    print("加密后的字符串：",b)

def jiemishu1():
    a=input("请输入一个加密后字符串：")
    b=""
    for i in a:
        m1=ord(i)
        if (m1>=65 and m1<=90) or (m1>=97 and m1<=122):
            m2=m1-3
            if (m2>90 and m2<97) or (m2<65):
                m2-=26
            m3=chr(m2)
            b+=m3
        else:
            b+=i
    print("解密后的字符串：",b)

if __name__=="__main__":
    jiemishu1()
    # jiamishu2()
    # shukonggeshu()
    # jiamishu1()