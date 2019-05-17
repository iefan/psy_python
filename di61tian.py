import os
def duxinshu():
    a=[0]*4
    t=[0]*4

    #第一部分：
    t[0]="1,2,3,4,5,6,7"
    t[1]="1,3,5,7"
    t[2]="2,3,6,7"
    t[3]="4,5,6,7"
    print("读心术猜数")
    print("请你从下面7个数中，选一个记在心里。")
    print(t[0])
    # print("请按任意键继续……(假设此时选了4)")
    os.system("pause")
    # for i in range(1,3):
    #     print()
    print("\n"*2)

    #第二、三、四部分：
    for i in range(1,4):
        # os.system("cls")
        # print(i,"问：下面的数中有你心中想的数吗？(0:没有;1:有)")
        print(t[i])
        a[i]=eval(input("问：上面的数中有你心中想的数吗？(0:没有;1:有)"))
        print()
        while a[i]!=0 and a[i]!=1:
            a[i]=eval(input("请输入0或1!!!  :"))
    # for i in range(1,3):
    #     print()
    print("\n\n")

    #第五部分：
    ans=4*a[3]+2*a[2]+a[1]
    # os.system("cls")
    print("你心中想的数是：{}".format(ans))

def moersima():
    a=[0]*10
    a[0]="11111"
    a[1]="01111"
    a[2]="00111"
    a[3]="00011"
    a[4]="00001"
    a[5]="00000"
    a[6]="10000"
    a[7]="11000"
    a[8]="11100"
    a[9]="11110"
    n=eval(input("请输入0~9之间的某个数："))
    while n<0 and n>9:
        n=eval(input("请输入0~9之间的某个数!!!! ："))
    for i in a[n]:
        if i=='0':
            print('.',end='')
        else:
            print('-',end='')

if __name__=="__main__":
    moersima()
    # duxinshu()