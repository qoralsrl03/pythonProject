from tkinter import *
from tkinter import filedialog
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        text.delete(1.0,END)
        with open(filepath,'r') as f:
            text.insert(INSERT, f.read())

app=Tk()
# 스크롤 생성
scrollbar = Scrollbar(app)
scrollbar.pack(side=RIGHT, fill=Y)
text=Text(app, wrap=NONE, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
btn=Button(app, text='open file', command=open_file)
btn.pack()
app.mainloop()