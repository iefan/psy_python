def guzhangchaxunxitong():
    print("LG洗衣机故障代码查询系统")
    n=input("请输入代码：")
    if n=='E1' or n=='e1':
        print("排水故障")
    elif n=='E2' or n=='e2':
        print("未关好门")
    elif n=='E4' or n=='e4':
        print("进水异常")
    elif n=='E8' or n=='e8':
        print("超过报警水位")
    else:
        print("未查询到此代码，请联系当地经商")

def chengjidengji():
    n=int(input("请输入你的成绩："))
    if n>=90:
        print("你的成绩等级是A")
    elif n>=70:
        print("你的成绩等级是B")
    elif n>=60:
        print("你的成绩等级是C")
    else:
        print("你的成绩等级是D")

def jisuancifang():
    m=int(input("m="))
    n=int(input("n="))
    if n==0:
        ans=1
    elif n==1:
        ans=m
    elif n==2:
        ans=m*m
    elif n==3:
        ans=m*m*m
    elif n==4:
        ans=m*m*m*m
    else:
        ans=-1
        # print("???")

    # print(ans)

    if ans==-1:
        print("???")
    else:
        print(ans)

def chutichengxu():
    print("诗词大赛")
    print("请选题：\n","1\n","2\n","3\n")
    n=int(input())
    if n==1:
        print("( )( )带雨晚来急，野渡无人舟自横。")#(春)(潮)
    elif n==2:
        print("忽如一夜( )( )来，千树万树梨花开。")#(春)(风)
    elif n==3:
        print("( )( )满园关不住，一枝红杏出墙来。")#(春)(色)
    else:
        print("无此序号的题目。")

if __name__ == "__main__":
    chutichengxu()
    # jisuancifang()
    # chengjidengji()
    # guzhangchaxunxitong()
