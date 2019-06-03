def mybin():
    # 这个函数的功能是输入十进制，输出二进制。
    num=eval(input("num="))
    b=num
    a=[]
    while num!=0:
        yushu=num%2
        a.append(yushu)
        num=num//2
    print('mybin({})='.format(b),end='')
    for i in range(len(a)-1,-1,-1):
        print(a[i],end='')

def myint():
    # 这个函数的功能是输入二进制，输出十进制。
    shijinzhi=0
    box=input("box=")
    for i in range(len(box)):
        #下面几句代码是完成：
        # len(box) 是返回输入的二进制数字的长度
        # range(0,len(box)-(i+1)) 是要计算某个位i上要乘的因子，
        # 比如当 box="1100", i=2时，上式变成 range(0, 1),
        # 即box的第3位要乘以因子2，（range(0,1)只循环一次，所以tmp=1*2=2）
        tmp = 1
        for _ in range(0,len(box)-(i+1)):
            # 该循环是计算二进制数某位要乘以的因子数
            # 如果是第1位，按1100来举例，则是乘以8，即8=2*2*2，
            # 此时该循环应循环3次，完成计算2的3次方
            tmp = tmp*2
        shijinzhi+=int(box[i])*tmp
        # print(shijinzhi, '--')
    print(shijinzhi)

if __name__=="__main__":
    myint()
    # mybin()