def luojiyunsuanbiao():
    tbwidth = 33
    print('-'*tbwidth)
    print("|逻辑与运算表：\t\t\t|")
    print('-'*tbwidth)
    print("|True  and True |","\t",True and True,"\t|")
    print('-'*tbwidth)
    print("|True  and False|","\t",True and False,"\t|")
    print('-'*tbwidth)
    print("|False and True |","\t",False and True,"\t|")
    print('-'*tbwidth)
    print("|False and False|","\t",False and False,"\t|")
    print('-'*tbwidth)
    print(' '*tbwidth)
    print('-'*tbwidth)
    print("|逻辑或运算表：\t\t\t|")
    print('-'*tbwidth)
    print("|True  or  True |","\t",True or True,"\t|")
    print('-'*tbwidth)
    print("|True  or  False|","\t",True or False,"\t|")
    print('-'*tbwidth)
    print("|False or  True |","\t",False or True,"\t|")
    print('-'*tbwidth)
    print("|False or  False|","\t",False or False,"\t|")
    print('-'*tbwidth)
    print(' '*tbwidth)
    print('-'*tbwidth)
    print("|逻辑非运算表：\t\t\t|")
    print('-'*tbwidth)
    print("|not True \t|","\t",not True,"\t|")
    print('-'*tbwidth)
    print("|not False\t|","\t",not False,"\t|")
    print('-'*tbwidth)

def luojiyunsuanbiao2():
    tbwidth = 65
    tbwidth2 = 33
    print('-'*tbwidth)
    print("|逻辑与、或运算表：\t\t\t\t\t\t|")
    print('-'*tbwidth)
    print("|    真值     |","\t","与\t\t|","\t  或\t\t|")
    print('-'*tbwidth)
    print("|True  , True |","\t",True and True,"\t\t|\t",True or True," \t\t|")
    print('-'*tbwidth)
    print("|True  , False|","\t",True and False,"\t\t|\t",True or False," \t\t|")
    print('-'*tbwidth)
    print("|False , True |","\t",False and True,"\t\t|\t",False or True," \t\t|")
    print('-'*tbwidth)
    print("|False , False|","\t",False and False,"\t\t|\t",False or False," \t|")
    print('-'*tbwidth)
    print(' '*tbwidth)
    print('-'*tbwidth2)
    print("|逻辑非运算表：\t\t\t|")
    print('-'*tbwidth2)
    print("|not True \t|","\t",not True,"\t|")
    print('-'*tbwidth2)
    print("|not False\t|","\t",not False,"\t|")
    print('-'*tbwidth2)

def remember_poems():
    poem1='''
       春晓
    （唐）孟浩然
    春眠不觉晓，
    处处闻啼鸟。
    夜来风雨声，
    花落知多少。
    '''
    poem2='''
       悯农
    （唐）李绅
    锄禾日当午，
    汗滴禾下土。
    谁知盘中餐，
    粒粒皆辛苦。
    '''
    poem3='''
        风
    （唐）李峤
    解落三秋叶，
    能开二月花。
    过江千尺浪，
    入竹万杆斜。
    '''
    poem4='''
        咏柳
    （唐）贺知章
    碧玉妆成一树高，
    万条垂下绿丝绦。
    不知细叶谁裁出，
    二月春风似剪刀。
    '''
    poem5='''
       赠汪伦
     （唐）李白
    李白乘舟将欲行，
    忽闻岸上踏歌声。
    桃花潭水深千尺，
    不及汪伦送我情。
    '''
    poem6='''
    野望
    （唐）王绩
    东皋薄暮望，徙倚欲何依。
    树树皆秋色，山山唯落晖。
    牧人驱犊返，猎马带禽归。
    相顾无相识，长歌怀采薇。
    '''
    poem7='''
    山中
    （唐）王勃
    长江悲已滞，
    万里念将归。
    况属高风晚，
    山山黄叶飞。
    '''
    poem8='''
      易水送别
   （唐）骆宾王
    此地别燕丹，
    壮士发冲冠。
    昔时人已没，
    今日水犹寒。
    '''
    poem9='''
       咏鹅
   （唐）骆宾王
    鹅  鹅  鹅，
    曲项向天歌。
    白毛浮绿水，
    红掌拨清波。
    '''
    poem10='''
     登幽州台歌
   （唐）陈子昂
    前不见古人，
    后不见来者。
    念天地之悠悠，
    独怆然而涕下。
    '''
    poem11='''
       渡汉江
   （唐）宋之问
    岭外音书断，
    经东复历春。
    近乡情更怯，
    不敢问来人。
    '''
    poem12='''
        边词
    （唐）张敬忠
    五原春色旧来迟，
    二月垂杨未挂丝。
    即今河畔冰开日，
    正是长安花落时。
    '''
    print("请输入你想背诵的古诗序号：")
    print("1，春晓\n2，悯农\n3，风\n4，咏柳\n5，赠汪伦\n6，野望\n7，山中\n8，易水送别\n9，咏鹅\n10，登幽州台歌\n11，渡汉江\n12，边词")
    
    n=int(input("序号："))
    if n==1:
        print(poem1)
    if n==2:
        print(poem2)
    if n==3:
        print(poem3)
    if n==4:
        print(poem4)
    if n==5:
        print(poem5)
    if n==6:
        print(poem6)
    if n==7:
        print(poem7)
    if n==8:
        print(poem8)
    if n==9:
        print(poem9)
    if n==10:
        print(poem10)
    if n==11:
        print(poem11)
    if n==12:
        print(poem12)

if __name__ == "__main__":
    remember_poems()
    # luojiyunsuanbiao2()
    # luojiyunsuanbiao()    