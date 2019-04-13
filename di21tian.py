def caishengri1():
    days=0
    print('\n',1,3,5,7,'\n',9,11,13,15,'\n',17,19,21,23,'\n',25,27,29,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=1
    print('\n',2,3,6,7,'\n',10,11,13,15,'\n',18,19,22,23,'\n',26,27,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=2
    print('\n',4,5,6,7,'\n',12,13,14,15,'\n',20,21,22,23,'\n',28,29,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=4
    print('\n',8,9,10,11,'\n',12,13,14,15,'\n',24,25,26,27,'\n',28,29,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=8
    print('\n',16,17,18,19,'\n',20,21,22,23,'\n',24,25,26,27,'\n',28,29,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=16
    print("您的生日日期是",days)

def caishengri2():
    month=0
    print("一、猜您的生日月份")
    print(1,3,5,7,9)
    ans=input("您的生日月份在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        month+=1
    print(2,3,6,7,10,11)
    ans=input("您的生日月份在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        month+=2
    print(4,5,6,7,12)
    ans=input("您的生日月份在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        month+=4
    print(8,9,10,11,12)
    ans=input("您的生日月份在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        month+=8
    print("二、猜您的生日日期")
    days=0
    print('\n',1,3,5,7,'\n',9,11,13,15,'\n',17,19,21,23,'\n',25,27,29,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=1
    print('\n',2,3,6,7,'\n',10,11,13,15,'\n',18,19,22,23,'\n',26,27,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=2
    print('\n',4,5,6,7,'\n',12,13,14,15,'\n',20,21,22,23,'\n',28,29,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=4
    print('\n',8,9,10,11,'\n',12,13,14,15,'\n',24,25,26,27,'\n',28,29,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=8
    print('\n',16,17,18,19,'\n',20,21,22,23,'\n',24,25,26,27,'\n',28,29,30,31)
    ans=input("您的生日日期在上面的数字里吗？是请回答y，否请回答n:")
    if ans=='y' or ans=='Y':
        days+=16
    print("您的生日是%s月%s日" % (month,days))

if __name__=="__main__":
    caishengri2()
    # caishengri1()