def dachefeiyong():
    feiyong=0
    lucheng=int(input("路程是："))
    if lucheng>10:
        feiyong=6+(10-2)*1.8+(lucheng-10)*1.8*1.5
    else:
        if lucheng>2:
            feiyong=6+(lucheng-2)*1.8
        else:
            feiyong=6
    shijian=int(input("时间是："))
    feiyong+=int(shijian/3)*1
    print("您要付",round(feiyong, 2),"元钱。")

def jisuan():
    x=int(input())
    if x==10:
        x+=1
    else:
        x-=1
    if x>10:
        x+=1
    else:
        x-=1
    if x<10:
        x+=1
    else:
        x-=1
    if x!=10:
        x+=1
    else:
        x-=1
    print("x=",x)

def jisuanjiaqian():
    n=int(input("请输入您需要购买的商品总价："))
    if n<=50:
        m=n
    else:
        if n<=150:
            m=50+(n-50)*0.9
        else:
            m=50+100*0.9+(n-150)*0.8
    print("您现需付",round(m, 2),"元。")

def jisuantizhi():
    height=int(input("您的身高是(cm)："))
    weight=int(input("您的体重是(kg)："))
    height = height/100 #转换为米
    bmi=round(weight/(height*height), 2)
    print("您的BMI值是：",bmi,"您的体型：",end='')
    if bmi<18.5:
        print("偏瘦。")
    else:
        if bmi<24:
            print("正常。")
        else:
            if bmi<28:
                print("偏胖。")
            else:
                if bmi<40:
                    print("肥胖。")
                else:
                    print("极重度肥胖。")

def dachefeiyong1():
    feiyong=0
    lucheng=int(input("路程是："))
    if lucheng>10:
        feiyong=6+(10-2)*1.8+(lucheng-10)*1.8*1.5
    else:
        if lucheng>2:
            feiyong=6+(lucheng-2)*1.8
        else:
            feiyong=6
    shijian=int(input("时间是："))
    feiyong+=int(shijian/3)*1
    print("您要付",round(feiyong, 2),"元钱。")

def jisuan2():
    x=int(input())
    if x==10:
        x+=1
    else:
        x-=1
    if x>10:
        x+=1
    else:
        x-=1
    if x<10:
        x+=1
    else:
        x-=1
    if x!=10:
        x+=1
    else:
        x-=1
    print("x=",x)

def jisuanjiaqian1():
    n=int(input("请输入您需要购买的商品总价："))
    if n<=50:
        m=n
    else:
        if n<=150:
            m=50+(n-50)*0.9
        else:
            m=50+100*0.9+(n-150)*0.8
    print("您现需付",round(m, 2),"元。")

def jisuantizhi1():
    height=int(input("您的身高是(cm)："))
    weight=int(input("您的体重是(kg)："))
    height = height/100 #转换为米
    bmi=round(weight/(height*height), 2)
    print("您的BMI值是：",bmi,"您的体型：",end='')
    if bmi<18.5:
        print("偏瘦。")
    else:
        if bmi<24:
            print("正常。")
        else:
            if bmi<28:
                print("偏胖。")
            else:
                if bmi<40:
                    print("肥胖。")
                else:
                    print("极重度肥胖。")

def jisuan1():
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    if b!=0:
        if a/b>c:
            # print(a,'/',b,'-',c,'=',round(a/b-c, 2))
            print("%.0f/%.0f-%.0f=%.0f" % (a, b, c, a/b-c))
            # print("%d/%d-%d=%d" % (a, b, c, a/b-c))
        else:
            # print(c,'-',a,'/',b,'=',round(c-a/b, 2))
            print("%.0f-%.0f/%.0f=%.0f" % (c, a, b, c-a/b))

def guzhangchaxunxitong():
    print("LG洗衣机故障代码查询系统")
    n=input("请输入代码：")
    if n=='E1' or n=='e1':
        print("排水故障")
        return
    if n=='E2' or n=='e2':
        print("未关好门")
        return
    if n=='E4' or n=='e4':
        print("进水异常")
        return
    if n=='E8' or n=='e8':
        print("超过报警水位")
        return
    
    print("未查询到此代码，请联系当地经商")

if __name__ == "__main__":
    guzhangchaxunxitong()
    # jisuan1()
    # jisuantizhi()
    # jisuanjiaqian()
    # jisuan()
    # dachefeiyong()