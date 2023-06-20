import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as messagebox

def create_custom_messagebox(window, title, message, font_size):
    result = messagebox.askokcancel(title, message, parent=window)
    if result:
        # [확인] 버튼을 클릭한 경우 처리할 작업을 수행합니다.
        print("확인 버튼을 클릭했습니다.")
    else:
        # [취소] 버튼을 클릭한 경우 처리할 작업을 수행합니다.
        print("취소 버튼을 클릭했습니다.")

def btn_click():
    text = txt.get()
    selected_indices = listbox.curselection()
    selected_categories = [listbox.get(idx) for idx in selected_indices]
    create_custom_messagebox(window, 'Go Search', f'입력된 텍스트: {text}\n선택된 카테고리: {selected_categories}', 30)

window = tk.Tk()
window.geometry("900x700+100+100")

# 검색 텍스트 영역
txt = tk.Entry(window)
txt.grid(row=0, column=0, sticky='nsew')

# 검색 버튼
btn = tk.Button(window, text='검색', command=btn_click)
btn.grid(row=0, column=1, sticky='nsew')

# 카테고리 리스트 박스
listbox = tk.Listbox(window, selectmode='extended', height=0)
listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

# 카테고리 데이터 추가 예시
categories = ['음식점', '카페', '주차장', '주유소', '은행', '마트', '헤어샵', '병원']
for category in categories:
    listbox.insert(tk.END, category)

# 글꼴 설정
txt.config(font=('helvetica', 30, 'bold'))
btn.config(font=('helvetica', 30, 'bold'))
listbox.config(font=('helvetica', 30, 'bold'))

# 열과 행의 가중치를 설정하여 크기를 동일하게 키우기
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()
