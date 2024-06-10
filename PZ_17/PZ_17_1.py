'''
В соответствии с номером варианта перейти по ссылке на прототип.
Реализовать его в IDE PyCharm Community с применением пакета tk.
Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).
'''
import tkinter as tk
from tkinter import ttk

def register():
    print("Registration submitted")

root = tk.Tk()
root.title("Registration Form")
root.geometry("600x300")  # Устанавливаем размер окна

# Name Section
name_label = ttk.Label(root, text="Name")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
last_name_entry = ttk.Entry(root)
last_name_entry.grid(row=0, column=1, padx=5, pady=5)
first_name_entry = ttk.Entry(root)
first_name_entry.grid(row=0, column=2, padx=5, pady=5)
label = ttk.Label(root, text="first name", font=("Arial", 7))
label.grid(row=1, column=1, padx=15, pady=1, sticky="W")
label = ttk.Label(root, text="last name", font=("Arial", 7))
label.grid(row=1, column=2, padx=10, pady=1, sticky="W")


# Company Section
company_label = ttk.Label(root, text="Company")
company_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
company_entry = ttk.Entry(root)
company_entry.grid(row=2, column=1, padx=5, pady=5)

# Email Section
email_label = ttk.Label(root, text="Email")
email_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")
email_entry = ttk.Entry(root)
email_entry.grid(row=3, column=1, padx=5, pady=5)

# Phone Section
phone_label = ttk.Label(root, text="Phone")
phone_label.grid(row=4, column=0, padx=5, pady=5, sticky="W")
area_code_entry = ttk.Entry(root,)
area_code_entry.grid(row=4, column=1, padx=5, pady=5)
phone_number_entry = ttk.Entry(root)
phone_number_entry.grid(row=4, column=2, padx=5, pady=5)
label = ttk.Label(root, text="Area Code", font=("Arial", 7))
label.grid(row=5, column=1, padx=15, pady=1, sticky="W")
label = ttk.Label(root, text="Phone Number", font=("Arial", 7))
label.grid(row=5, column=2, padx=10, pady=1, sticky="W")

# Subject Section
subject_label = ttk.Label(root, text="Subject")
subject_label.grid(row=6, column=0, padx=5, pady=5, sticky="W")
subject_combobox = ttk.Combobox(root, values=["Choose option", "Feedback", "Support"])
subject_combobox.set('Choose option')
subject_combobox.grid(row=6, column=1, padx=5, pady=5)

# Survey Section
survey_label = ttk.Label(root, text="Are you an existing customer?")
survey_label.grid(row=7, column=0, sticky="W")

survey_var = tk.StringVar()
survey_var.set("Yes")

yes_radio = ttk.Radiobutton(root, text="Yes", variable=survey_var, value="Yes")
yes_radio.grid(row=8, column=0, padx=5, pady=5, sticky="W")

no_radio = ttk.Radiobutton(root, text="No", variable=survey_var, value="No")
no_radio.grid(row=8, column=0, padx=100, pady=5, sticky="W")

# Register Button
style = ttk.Style()
style.configure("Red.TButton", foreground="black", background="red")

register_button = ttk.Button(root, text="Register", command=register, style="Red.TButton")
register_button.grid(row=9, column=0, padx=40, pady=5, sticky="W")

root.mainloop()
