"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2
class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Samantha Davenport')
        self.main_window.title('Chapter 13')
        self.label.pack(ipadx=40, ipady=40)
        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2


# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3
class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame, text='Samantha Davenport')
        self.label2 = tkinter.Label(self.top_frame, text='Web and Mobile Design & Development')
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3 = tkinter.Label(self.bottom_frame, text='Programming Logic PRG-105')
        self.label4 = tkinter.Label(self.bottom_frame, text='Intro to Digital Legalities')
        self.label5 = tkinter.Label(self.bottom_frame, text='Graphic Design I')
        self.label6 = tkinter.Label(self.bottom_frame, text='HTML & CSS Web 115')
        self.label3.pack(side='left')
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()


if __name__ == '__main__':
    my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class Joke:
    def __init__(self):
        self.my_joke = tkinter.Tk()
        self.button = tkinter.Button(self.my_joke, text='Why was nine afraid of seven?', command=self.do_something)
        self.button.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Answer', 'Because seven eight nine!')


if __name__ == '__main__':
    joke_gui = Joke()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class Conversion:
    def __init__(self):
        self.conversion_box = tkinter.Tk()
        self.top_frame2 = tkinter.Frame(self.conversion_box)
        self.bottom_frame2 = tkinter.Frame(self.conversion_box)

        self.prompt_label = tkinter.Label(self.top_frame2, text='Enter distance in inches:')
        self.entry = tkinter.Entry(self.top_frame2, width=10)

        self.prompt_label.pack(side='left')
        self.entry.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame2, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame2, text='Quit', command=self.conversion_box.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame2.pack()
        self.bottom_frame2.pack()

        tkinter.mainloop()

    def convert(self):
        inches = float(self.entry.get())
        centimeters = inches * 2.54
        tkinter.messagebox.showinfo('Results', str(inches) + ' inches is equal to ' + str(centimeters) + ' centimeters')


if __name__ == '__main__':
    conversion_gui = Conversion()
