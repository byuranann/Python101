import tkinter as tk

my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

def check_value():
    value = value_entry.get()
    if value in my_dict:
        result_label.config(text="Found!")
    else:
        result_label.config(text="Don't found.")

root = tk.Tk()
root.title("Stock Check")
root.geometry('310x300')

value_label = tk.Label(root, text="Enter here to check:")
value_label.pack(side="left")
value_entry = tk.Entry(root)
value_entry.pack(side="left")

check_button = tk.Button(root, text="Check", command=check_value)
check_button.place(x=120, y=200)

result_label = tk.Label(root, text="")
result_label.pack(side="left")

root.mainloop()