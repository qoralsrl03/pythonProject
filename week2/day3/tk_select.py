import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

# 임시로 사용할 종목 코드
stocks = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Google LLC',
}

def plot_stock():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()

    stock_code = stock_combobox.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    data = yf.download(stock_code, start=start_date, end=end_date)
    data['Close'].plot()
    plt.title(f'{stock_code} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

def clear_graph():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()
        plt.clf()

root = tk.Tk()

tk.Label(root, text="Stock Code").pack()
stock_combobox = ttk.Combobox(root, values=list(stocks.keys()))
stock_combobox.pack()

tk.Label(root, text="Start Date (YYYY-MM-DD)").pack()
start_date_entry = tk.Entry(root)
start_date_entry.pack()

tk.Label(root, text="End Date (YYYY-MM-DD)").pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()

plot_button = tk.Button(root, text="Plot", command=plot_stock)
plot_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_graph)
clear_button.pack()

canvas = None

root.mainloop()
