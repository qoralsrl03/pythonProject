from tkinter import *
# pip install pillow
from PIL import Image, ImageTk


def create_ball(canvas):
    # x0, y0=  100, 150
    # x1, y1 = 150, 200
    # canvas.create_oval(x0,y0,x1,y1,fill='red',tag='redBall')
    global ho_img
    # img=PhotoImage(fill='hoho.png')
    # canvas.create_image(200,200,image=img,tag='redBall')
    img = Image.open('hoho.png')
    img = img.resize((50, 50), Image.LANCZOS)
    ho_img = ImageTk.PhotoImage(img)
    canvas.create_image(100, 250, image=ho_img, tag='redBall')


def move_left(event):
    canvas.move('redBall', -deltax, 0)
    canvas.after(5)
    canvas.update()


def move_right(event):
    canvas.move('redBall', deltax, 0)
    canvas.after(5)
    canvas.update()


def move_up(event):
    canvas.move('redBall', 0, -deltay)
    canvas.after(5)
    canvas.update()


def move_down(event):
    canvas.move('redBall', 0, deltay)
    canvas.after(5)
    canvas.update()
def move_jump(event):
    for _ in range(10):
        canvas.move('redBall', 0, -5)  # 10번 동안 5씩 위로 이동
        canvas.after(10)
        canvas.update()
    for _ in range(10):
        canvas.move('redBall', 0, 5)  # 10번 동안 5씩 아래로 이동
        canvas.after(10)
        canvas.update()

deltax = 10
deltay = 10

app = Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack()
create_ball(canvas)
canvas.bind('<Left>', move_left)

canvas.bind('<Right>', move_right)

canvas.bind('<Up>', move_up)

canvas.bind('<Down>', move_down)

canvas.bind('<space>', move_jump)


canvas.focus_set()
canvas.pack()

app.mainloop()
