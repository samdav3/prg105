import tkinter
import tkinter.messagebox


class Info:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.info_button = tkinter.Button(self.main_window, text='Show Info', command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        self.info_button.pack(padx=(10, 10), pady=(10, 10), side='left')
        self.quit_button.pack(padx=(10, 10), pady=(10, 10), side='left')

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('My Info', 'Samantha Davenport\n1 Hickory Rd, Oakwood Hills, IL 60013')


if __name__ == '__main__':
    my_info = Info()
