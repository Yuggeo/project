import tkinter as tk
from tkinter import ttk

def calculate_mortgage():
    principal = float(principal_entry.get())
    annual_rate = float(rate_entry.get()) / 100
    years = int(years_entry.get())
    monthly_rate = annual_rate / 12
    num_payments = years * 12

    if monthly_rate == 0:
        monthly_payment = principal / num_payments
    else:
        monthly_payment = principal * monthly_rate * (1 + monthly_rate) ** num_payments / ((1 + monthly_rate) ** num_payments - 1)

    result_label.config(text=f"Ежемесячный платеж: {monthly_payment:.2f}")

# Создаем основное окно
# Создаем основное окно2222
# Создаем основное окно3333
# Создаем основное окно1111
root = tk.Tk()
root.title("Калькулятор ипотеки")

# Создаем и размещаем виджеты
tk.Label(root, text="Сумма кредита:").grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Годовая процентная ставка (%):").grid(row=1, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Срок кредита (лет):").grid(row=2, column=0, padx=10, pady=10)
years_entry = tk.Entry(root)
years_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_mortgage)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Ежемесячный платеж: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Запускаем главный цикл
root.mainloop()

