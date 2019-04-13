import string
def dayin26gexiaoxiezimu():
    for i in string.ascii_lowercase:
        print(i,end=' ')

def yihangdaxieyihangxiaoxie():
    for i in range(0,26):
        print(string.ascii_lowercase[i],end=' ')
    print()
    for i in range(-1,-27,-1):
        print(string.ascii_uppercase[i],end=' ')

def qiudeshu():
    for i in range(0,6):
        # print(string.ascii_lowercase[i])
        tmp = string.ascii_lowercase[i]
        print(tmp, end=" ")
        x=ord(tmp)-ord('a')+1
        if x%2==1:
            y=ord(tmp)+1
        else:
            y=ord(tmp)-1
        ans=y
        print(ans)

def dayindaxiaozimu():
    for i in range(0,26):
        print(string.ascii_uppercase[i]+string.ascii_lowercase[i],end=' ')
    
if __name__ == "__main__":
    dayindaxiaozimu()
    # qiudeshu()
    # yihangdaxieyihangxiaoxie()
    # dayin26gexiaoxiezimu()