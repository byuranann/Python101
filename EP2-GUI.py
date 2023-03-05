import tkinter as tk

class RecordGUI:
    def __init__(self, master):
        self.master = master
        master.title("Record GUI")
        master.geometry("500x800")  # set the width and height of the window

        self.record_label = tk.Label(master, text="Record:")
        self.record_label.pack()

        self.record_text = tk.Text(master)
        self.record_text.pack()

        # self.record_entry = tk.Entry(master, width=50)
        # self.record_entry.pack()

        self.record_button = tk.Button(master, text="Record", command=self.record)
        self.record_button.pack()

        self.read_button = tk.Button(master, text="Read", command=self.read)
        self.read_button.pack()

       # self.quit_button = tk.Button(master, text="Quit", command=master.quit)
       # self.quit_button.pack()

   # def record(self):
   #     record = self.record_entry.get()
   #     with open('records.txt', 'a') as f:
   #         f.write(record + '\n')

    def record(self):
        record = self.record_text.get("1.0",'end-1c')
        with open('records.txt', 'a') as f:
            f.write(record + '\n')

    def read(self):
        with open('records.txt', 'r') as f:
            records = f.read()
        self.record_label.config(text="Records:\n" + records)

root = tk.Tk()
my_gui = RecordGUI(root)
root.mainloop()
