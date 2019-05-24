def shutangshu():
    for i in range(160,201):
        if i%4==2 and i%6==4 and i%9==7:
            print(i)
        i+=1

if __name__=="__main__":
    shutangshu()