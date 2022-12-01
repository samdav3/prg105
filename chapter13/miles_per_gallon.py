import tkinter
import tkinter.messagebox


class GasMileage:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_line = tkinter.Label(self.top_frame, text='Enter how many gallons your car holds:')
        self.gas_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_line2 = tkinter.Label(self.top_frame, text='How many miles have ypu traveled?')
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_line.pack(side='top')
        self.gas_entry.pack(side='top')
        self.prompt_line2.pack(side='top')
        self.miles_entry.pack(side='top')

        self.prompt_line3 = tkinter.Label(self.mid_frame, text='Converted to miles per gallons: ')
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.convert_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.conversion)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.prompt_line3.pack(side='left')
        self.miles_label.pack(side='left')
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def conversion(self):
        gallons = float(self.gas_entry.get())
        miles = float(self.miles_entry.get())
        gas_mileage = miles / gallons
        self.value.set(f'{gas_mileage}')


if __name__ == '__main__':
    gas_miles = GasMileage()
