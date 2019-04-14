import turtle as tt
def xiaowugui():
    tt.screensize(800,800,"green")
    tt.penup()
    tt.goto(0,-200)
    tt.fillcolor("white")
    tt.begin_fill()
    tt.circle(100)
    tt.end_fill()

    tt.goto(0,0)
    tt.fillcolor("white")
    tt.begin_fill()
    tt.circle(60)
    tt.end_fill()




    # tt.pendown()
    # tt.pensize(3)
    # tt.pencolor("red")
    # tt.speed(3)
    # tt.circle(20)s
    # tt.circle(40)
    # tt.circle(80)
    # tt.circle(160)
    # tt.hideturtle()
    # tt.penup()
    # tt.goto(-40,80)
    # tt.pendown()
    # tt.write("同切圆",font=("",18))
    tt.done()


if __name__=="__main__":
    xiaowugui()