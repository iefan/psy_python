def dayin99chengfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print("{}*{}={:2}".format(i,j,i*j),end='  ')
            # print(i,'*',j,'=',' '*1,i*j,' '*2,end='')
        print()

def lianjiaqiuhechengxu():
    ans=0
    for _ in range(1,4):
        for _ in range(1,6):
            ans+=1
    print(ans)

def jisuanweishu():
    ans=0
    for i in range(1,100):
        for j in range(1,i+1):
            ans+=1
            if i==99 and j==9:
                break
    print(ans)

def jitufonglong():
    for ji in range(1,35):
        for tu in range(1,24):
            if ji+tu==35 and ji*2+tu*4==94:
                print("鸡：",ji,"兔：",tu)

if __name__=="__main__":
    jitufonglong()
    # jisuanweishu()
    # lianjiaqiuhechengxu()
    # dayin99chengfabiao()