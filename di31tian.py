def hanzichengfabiao():
    a=["","一","二","三","四","五","六","七","八","九"]
    b=["","一十","二十","三十","四十","五十","六十","七十","八十"]
    box=[]
    for ib in b:
        for ia in a:
            box.append(ib+ia)
    for i in range(1,10):
        for j in range(1,i+1):
            if i*j<10:
                print("%s%s得%s" % (box[j],box[i],box[i*j]),end='\t')
            else:
                print("%s%s%s" % (box[j],box[i],box[i*j]),end='\t')
        print()
if __name__=="__main__":
    hanzichengfabiao()