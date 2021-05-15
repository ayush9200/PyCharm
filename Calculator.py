from tkinter import *
from tkinter import messagebox # message box lib has all sort of predefind window that you can take adv.
# By - Ayush Kumar Singh C0799530

class CalculatorGUI:
    def __init__(self):
        #-----------------------creating a window ---------------------
        self.window = Tk()
        self.window.title("tk")
        self.window.geometry("300x200")

        #--------------------------Frames------------------------------------
        self.test1_frame = Frame()
        self.test2_frame = Frame()
        self.test3_frame = Frame()
        self.bottom_frame = Frame()
        self.result_frame = Frame()
        #---------------------------Widgets---------------------------------
        self.prompt_label1 = Label(self.test1_frame,text ="Enter the score for test 1: ", fg = "black")
        self.prompt_label2 = Label(self.test2_frame, text="Enter the score for test 2: ", fg="black")
        self.prompt_label3 = Label(self.test3_frame, text="Enter the score for test 3: ", fg="black")
        self.kilo_test1_entry = Entry(self.test1_frame)
        self.kilo_test2_entry = Entry(self.test2_frame)
        self.kilo_test3_entry = Entry(self.test3_frame)
        self.calc_button = Button(self.bottom_frame, text ="Average" , padx = 10, command = self.calculate)
        self.cancel_button = Button(self.bottom_frame, text = "Quit", padx = 10, command = self.window.destroy)
        self.result = StringVar()
        self.result.set("Result: N/A")
        self.result_label =Label(self.result_frame, textvariable =self.result, fg ="black")
        #---------------------------pack() widgits ---------------------------
        self.prompt_label1.pack(side = "left", padx = 10, pady = 10)
        self.prompt_label2.pack(side="left", padx=10, pady=10)
        self.prompt_label3.pack(side="left", padx=10, pady=10)
        self.kilo_test1_entry.pack(padx = 10, pady = 10)
        self.kilo_test2_entry.pack(padx=10, pady=10)
        self.kilo_test3_entry.pack(padx=10, pady=10)
        self.calc_button.pack(side ="left" ,padx = 10, pady = 10)
        self.cancel_button.pack(padx = 10, pady = 10)
        self.result_label.pack()

        #---------------------------pack() Frame --------------------------------
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.bottom_frame.pack()
        self.result_frame.pack()

        mainloop()
    def calculate(self):
        try:
            test_entry1 = int(self.kilo_test1_entry.get())
            test_entry2 = int(self.kilo_test2_entry.get())
            test_entry3 = int(self.kilo_test3_entry.get())
            average =  (test_entry1+test_entry2+test_entry3)/3
            print(f'Average for all three test is {average}')
            self.result.set(f'Average: {average}')
        except:
            messagebox.showerror("Input error","The input has to be a number")


cal = CalculatorGUI()