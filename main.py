import tkinter as tk


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')

        self.main_gui = MainGUI(self)
        self.main_gui.grid(row=0, column=0, sticky='news')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class MainGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.child_windows = []

        self.new_button = tk.Button(self, text="New", command=self.new)
        self.message_label = tk.Label(self, text='Nothing yet')

        self.new_button.grid(row=0, column=0)
        self.message_label.grid(row=0, column=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def new(self):
        child_count = len(self.child_windows)

        self.child_windows.append(ChildWindow(self, f'Child number {child_count}'))

    def message(self, source, text):
        self.message_label.configure(text=text)

    def close_nicely(self, target):
        print(self.child_windows)
        self.message_label.configure(text=target.label + ' asked to close')
        self.child_windows.remove(target)
        print(self.child_windows)
        target.destroy()


class ChildWindow(tk.Toplevel):
    def __init__(self, parent, label):
        super().__init__()
        self.geometry('300x200')
        self.parent = parent
        self.label = label

        self.action_button = tk.Button(self, text=label, command=self.action)
        self.close_button = tk.Button(self, text='Close', command=self.close_nicely)

        self.action_button.grid(row=0, column=0)
        self.close_button.grid(row=0, column=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.protocol("WM_DELETE_WINDOW", self.close_nicely)

    def action(self):
        self.parent.message(self, self.label + ' says hi')

    def close_nicely(self):
        self.parent.close_nicely(self)


my_app = MyApp()

tk.mainloop()
