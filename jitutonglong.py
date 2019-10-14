def dayinxinghao():
    for i in range(2,6):
        print((i-1)*' '+' *')
        for j in range(i-2):
            print(' '*(i-2-j),end='')
            print(' *',end='')
            print('  '*j,end='')
            print(' *')
        print(' *'*i)
    print()

def dayinxinghao1():
    for i in range(2,6):
        for j in range(1,i+1):
            print((i-j)*' ',end='')
            print(' *'*j)

def  jitutonglong():
    print('鸡兔同笼游戏现在开始！！！')
    head = eval(input("请输入一共的头数："))
    foot=eval(input("请输入一共的脚数："))
    jitou=head-(foot-head*2)//2
    tutou=(foot-head*2)//2
    jijiao=jitou*2
    tujiao=tutou*4
##    if  jitou+tutou==head  and  jijiao+tujiao==foot  and  type(jitou)==type(2)  and  type(tutou)==type(2):
    if  jitou+tutou==head  and  jijiao+tujiao==foot  :
        print("鸡有{}只  ，  兔有{}只".format(int(jitou),int(tutou)))
    else:
        print("无解！！！")

if __name__=="__main__":
    # dayinxinghao1()
    jitutonglong()
    # dayinxinghao()