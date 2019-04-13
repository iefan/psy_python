def hanzi(num):
    hanzinum=["","一","二","三","四","五","六","七","八","九","十"]
    if num<10:
        return hanzinum[num]
    elif num==10:
        return hanzinum[1]+hanzinum[10]
    else:
        shi=num//10
        ge=num%10
        if shi==1:
            returnstr=hanzinum[10]
        else:
            returnstr=hanzinum[shi]+hanzinum[10]
        if ge!=0:
            returnstr+=hanzinum[ge]
        return returnstr

def dayinhanzichengfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            if i*j<10:
                tmpstr = "%s%s得%s" % (hanzi(j),hanzi(i),hanzi(i*j))
                # print("%s%s得%s" % (hanzi(j),hanzi(i),hanzi(i*j)),end='\t')
            else:
                tmpstr = "%s%s%s" % (hanzi(j),hanzi(i),hanzi(i*j))
                # print("%7s" % tmpstr,end='')
                # print("%s%s%s" % (hanzi(j),hanzi(i),hanzi(i*j)),end='\t')
            if len(tmpstr)==4:
                tmpstr += " "*2
                print("%10s" % tmpstr,end='')
            else:
                print("%9s" % tmpstr,end='')
                
        print()

if __name__=="__main__":
    dayinhanzichengfabiao()
    # print(hanzi(15))