def baiqianmaibaiji1():
    print("公鸡",' '*5,"母鸡",' '*5,"小鸡")
    for gongji in range(1,34):
        for muji in range(1,51):
            for xiaoji in range(1,101):
                if (gongji+muji+xiaoji==100) and (abs(gongji*3+muji*2+xiaoji/3-100)<1e-9):
                    print(gongji,' '*5,muji,' '*5,xiaoji)

def baiqianmaibaiji2():
    print("公鸡",' '*5,"母鸡",' '*5,"小鸡")
    for gongji in range(1,34):
        for muji in range(1,51):
            xiaoji=100-muji-gongji
            if (gongji+muji+xiaoji==100) and (abs(gongji*3+muji*2+xiaoji/3-100)<1e-9):
                print(gongji,' '*5,muji,' '*5,xiaoji)

if __name__=="__main__":
    baiqianmaibaiji2()
    # baiqianmaibaiji1()