'''
Дана масса М в килограммах. Используя операцию деления нацело,
найти количество полных тонн в ней (1 тонна = 1000 кг). Решить
задачу с использованием tkinter
'''
import tkinter as tk
from tkinter import messagebox

def calculate_tonnes():
    try:
        mass_kg = float(entry.get())
        tonnes = mass_kg // 1000  # Используем операцию деления нацело
        result_label.config(text=f"Полных тонн: {tonnes}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное значение для массы")

# Создаем графический интерфейс
root = tk.Tk()
root.title("Конвертер массы в тонны")

input_label = tk.Label(root, text="Введите массу в килограммах:")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_tonnes)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

