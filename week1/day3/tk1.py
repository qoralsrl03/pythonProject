#tkinter -- 파이썬에서 설치 없이 쉽게 사용 가능한 GUI
import tkinter
from tkinter import messagebox
import random

app=tkinter.Tk()
app.title('로또 생성기')

def btn_click():
    arr = []
    nm=int(txt.get())
    for v in range(nm):
        com_set = set()
        while True:
            com_set.add(random.randint(1, 45))
            if len(com_set) == 6:
                arr.append(com_set)
                break
    myList =''
    for i in range(len(arr)):
        myList += str(arr[i])+"\n"
    tkinter.messagebox.showinfo('수량:', myList)
txt = tkinter.Entry(app)
txt.grid(row = 0, column = 1)



lab = tkinter.Label(app, text="수량:")
lab.grid(row=0, column=0)
btn=tkinter.Button(app, text='ok', command=btn_click)
btn.grid(row=1, column=1)
app.mainloop()