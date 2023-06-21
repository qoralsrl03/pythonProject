import cx_Oracle
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import tkinter as tk

f = [f.name for f in fm.fontManager.ttflist]
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
print(len(font_list))

# 폰트 경로 지정
font_path = 'NanumGothic.ttf'  # 폰트 파일의 경로

plt.rc('font', family='Malgun Gothic')  # * 나눔 고딕 적용시 맑은 고딕으로 들어가는거 주의 *
print(plt.rcParams['font.family'])

# 데이터베이스 연결 설정
connection = cx_Oracle.connect('study', 'study', 'localhost:1521/xe', encoding='UTF-8')

# 커서 생성
cursor = connection.cursor()

def btn_click():
    text = txt.get()
    search_list(text)

def search_list(dong):
    # 데이터베이스에서 데이터 조회
    sql = "SELECT category, COUNT(*) as count FROM mystore WHERE dong LIKE '%' || :dong || '%' GROUP BY category"
    cursor.execute(sql, {'dong': dong})
    result = cursor.fetchall()

    # 조회한 데이터 가공 및 준비
    categories = []
    counts = []
    for row in result:
        category = row[0]
        count = row[1]
        categories.extend(category.split(','))
        counts.extend([count] * len(category.split(',')))

    # 데이터가 있는 경우에만 퍼센트 계산
    if counts:
        total = sum(counts)  # 데이터의 총합 계산
        percentages = [(count / total) * 100 for count in counts]
    else:
        percentages = []

    # 시각화 (막대 그래프)
    plt.bar(categories, percentages)
    plt.xlabel('Category')
    plt.ylabel('Percentage %')
    plt.title('Data Visualization')


    plt.show()

window = tk.Tk()
window.geometry("900x700+100+100")
window.title("키워드 데이터 시각화")
# 검색 텍스트 영역
txt = tk.Entry(window)
txt.grid(row=0, column=0, sticky='nsew')

# 검색 버튼
btn = tk.Button(window, text='검색', command=btn_click)
btn.grid(row=0, column=1, sticky='nsew')

# 글꼴 설정
txt.config(font=('helvetica', 30, 'bold'))

# 열과 행의 가중치를 설정하여 크기를 동일하게 키우기
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

window.mainloop()

# 연결 종료
cursor.close()
connection.close()
