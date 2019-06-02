class artist:
    def __init__(self):
        self.name = ""
        self.age = ""

    def set(self, studentname, studentage):
        # if type(studentage) == type(""):
        #     print("设置年龄失败")
        #     return
        self.name = studentname
        self.age = studentage

    def display(self):
        print("编程是一门艺术")
        print("小艺术家的姓名：{}".format(self.name))
        print("小艺术家的年龄：{}".format(self.age))
        print("-"*20)
     
def diaoyong():
    stud1 = artist()
    stud2 = artist()
    stud1.set("nike", 11)
    stud1.display()
    stud2.set("glair", "rr")
    stud2.display()

    # stud2.age = "panpan"
    # print(stud2.age)
    
class student:
    def __init__(self):
        self.name=None
        self.age=None

def diaoyong1():
    st1=student()
    st1.name=input("请输入小艺术家的名字：")
    st1.age=eval(input("请输入小艺术家的年龄："))
    print(st1.name,' ',st1.age)

class mydate:
    def __init__(self):
        self.year=None
        self.month=None
        self.day=None
    def display1(self):
        print(self.year,'/',self.month,'/',self.day)

def diaoyong2():
    dt1=mydate()
    dt1.year=eval(input("请输入年份："))
    dt1.month=eval(input("请输入月份："))
    dt1.day=eval(input("请输入日期："))
    dt1.display1()

if __name__ == "__main__":
    diaoyong2()
    # diaoyong1()
    # diaoyong()