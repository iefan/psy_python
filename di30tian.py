def dadachengfabiao():
    for j in range(1,10):
        for i in range(1,10):
            print("%sx%s=%s" % (j,i,j*i),end='\t')
        print()

def daxiaochengfabiao():
    fh = open("chengfabiao.txt", 'w')
    for a in range(1,20):
        line_str = ""
        for b in range(1,a+1):
            line_str += "%2sx%2s=%3s\t" % (b,a,a*b)
            # fh.write("%sx%2s=%3s" % (b,a,a*b))
            print("%sx%2s=%3s" % (b,a,a*b),end='\t')
        line_str += "\n"
        fh.write(line_str)
        print()
    fh.close()

def dalaohu():
    i=1
    while i<=5:
        print(i,end=' ')
        i+=1

def dashuzi():
    i=0
    while i<=8:
        print(i,end=' ')
        i+=4

def qiuhe():
    i=6
    sum_int=0
    while i<=180:
        # print(i)
        sum_int+=i
        i=i+6
    print(sum_int)

def sixuinhuan():
    while 2>1:
        print(1)

if __name__=="__main__":
    # sixuinhuan()
    qiuhe()
    # dashuzi()
    # dalaohu()
    # daxiaochengfabiao()
    # dadachengfabiao()