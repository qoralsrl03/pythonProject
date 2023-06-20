import tkinter as tk
from tkinter import filedialog, Text
import selenium

print(selenium.__version__)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        text.delete(1.0, tk.END)
        with open(filepath, "r") as file:
            text.insert(tk.INSERT, file.read())

root = tk.Tk()

# 스크롤바 생성
# scrollbar = tk.Scrollbar(root)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# text = Text(root,  wrap=tk.NONE, yscrollcommand=scrollbar.set)
text = Text(root)
text.pack()

# 스크롤바를 텍스트 상자에 연결
# scrollbar.config(command=text.yview)

open_button = tk.Button(root, text="Open file", command=open_file)
open_button.pack()

root.mainloop()