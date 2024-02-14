from tkinter import *
import math
import tkinter.messagebox
 
root = Tk()
root.title("Scientific Calculator")
root.configure(background = 'white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
calc = Frame(root)
calc.grid()
 
class Calc():
    # main
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False
 
    # Enter number
    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
 
    # Sum of total
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
 
    # Display
    def display(self, value):
        # Delete
        txtDisplay.delete(0, END)
        # Insert
        txtDisplay.insert(0, value)
 
    # Valid function
    def valid_function(self):
        # Add
        if self.op == "add":
            self.total += self.current
        # Sub
        if self.op == "sub":
            self.total -= self.current
        # Multi
        if self.op == "multi":
            self.total *= self.current
        # Devide
        if self.op == "divide":
            self.total /= self.current
        # Mod
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
 
    # Operations
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
 
    # Clean entry
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True
 
    # All clean entry
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
 
    # Pi
    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)
 
    # Tau
    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)
 
    # E
    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)
 
    # MathPM
    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
 
    # Squared
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
 
    # Cos
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    # Cosh
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    # Tan
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    # Tanh
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    # Sin
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    # Sinh
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    # Log
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
 
    # Exp
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)
 
    # Acosh
    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)
 
    # Asonh
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)
 
    # Expm1
    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)
 
    # Lgamma
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
 
    # Degrees
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
 
    # Log2
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)
 
    # Log10
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)
 
    # Log1p
    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)
 
added_value = Calc()
 
txtDisplay = Entry(calc, 
                   font=('Helvetica',20,'bold'),
                   bg='black',
                   fg='white',
                   bd=30,
                   width=28,
                   justify=RIGHT)
txtDisplay.grid(row=0,
                column=0, 
                columnspan=4, 
                pady=1)
txtDisplay.insert(0,"0")
 
numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, 
                          width=6, 
                          height=2,
                          bg='black',fg='white',
                          font=('Helvetica',20,'bold'),
                          bd=4,
                          text=numberpad[i]))
        btn[i].grid(row=j, 
                    column= k, 
                    pady = 1)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1
       
# Button clear
btnClear = Button(calc, 
                  text=chr(67),
                  width=6,
                  height=2,
                  bg='powder blue',
                  font=('Helvetica',20,'bold'),
                  bd=4, 
                  command=added_value.Clear_Entry
                 ).grid(row=1, 
                        column= 0, 
                        pady = 1)
 
# Button all clear
btnAllClear = Button(calc, 
                     text=chr(67)+chr(69),
                     width=6, 
                     height=2,
                     bg='powder blue', 
                     font=('Helvetica',20,'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                    ).grid(row=1, 
                           column= 1, 
                           pady = 1)
 
# Button squared
btnsq = Button(calc, 
               text="\u221A",
               width=6, 
               height=2,
               bg='powder blue', 
               font=('Helvetica',
                     20,
                     'bold'),
               bd=4,
               command=added_value.squared
              ).grid(row=1, 
                     column= 2, 
                     pady = 1)
 
# Button add
btnAdd = Button(calc, 
                text="+",
                width=6, 
                height=2,
                bg='powder blue',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=lambda:added_value.operation("add")
                ).grid(row=1, 
                       column= 3, 
                       pady = 1)
 
# Button sub
btnSub = Button(calc, 
                text="-",
                width=6,
                height=2,
                bg='powder blue',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=lambda:added_value.operation("sub")
                ).grid(row=2, 
                       column= 3, 
                       pady = 1)
 
# Button multi
btnMul = Button(calc, 
                text="x",
                width=6, 
                height=2,
                bg='powder blue', 
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=lambda:added_value.operation("multi")
                ).grid(row=3, 
                       column= 3, 
                       pady = 1)
 
# Button divide
btnDiv = Button(calc, 
                text="/",
                width=6, 
                height=2,
                bg='powder blue',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=lambda:added_value.operation("divide")
                ).grid(row=4, 
                       column= 3, 
                       pady = 1)
 
# Button 0
btnZero = Button(calc, 
                 text="0",
                 width=6,
                 height=2,
                 bg='black',
                 fg='white',
                 font=('Helvetica',
                       20,
                       'bold'),
                 bd=4,
                 command=lambda:added_value.numberEnter(0)
                 ).grid(row=5, 
                        column= 0, 
                        pady = 1)
 
# Button .
btnDot = Button(calc, 
                text=".",
                width=6,
                height=2,
                bg='powder blue', 
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=lambda:added_value.numberEnter(".")
                ).grid(row=5, 
                       column= 1, 
                       pady = 1)

# Button mathPM
btnPM = Button(calc, 
               text=chr(177),
               width=6, 
               height=2,
               bg='powder blue', 
               font=('Helvetica',
                     20,
                     'bold'),
               bd=4,
               command=added_value.mathPM
              ).grid(row=5, 
                     column= 2, 
                     pady = 1)
 
# Button sum of total
btnEquals = Button(calc, 
                   text="=",
                   width=6,
                   height=2,
                   bg='powder blue',
                   font=('Helvetica',
                         20,
                         'bold'),
                   bd=4,command=added_value.sum_of_total
                  ).grid(row=5, 
                         column= 3, 
                         pady = 1)

# ROW 1 :
# Button pi
btnPi = Button(calc, 
               text="pi",
               width=6,
               height=2,
               bg='black',
               fg='white', 
               font=('Helvetica',
                     20,
                     'bold'),
               bd=4,
               command=added_value.pi
              ).grid(row=1, 
                     column= 4, 
                     pady = 1)
 
# Button cos
btnCos = Button(calc, 
                text="Cos",
                width=6, 
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.cos
               ).grid(row=1, 
                      column= 5, 
                      pady = 1)
 
# Button tan
btntan = Button(calc, 
                text="tan",
                width=6, 
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.tan
               ).grid(row=1, 
                      column= 6, 
                      pady = 1)
 
# Button sin
btnsin = Button(calc, 
                text="sin",
                width=6,
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.sin
               ).grid(row=1, 
                      column= 7, 
                      pady = 1)
 
# ROW 2 :
# Button tau
btn2Pi = Button(calc, 
                text="2pi",
                width=6, 
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.tau
               ).grid(row=2, 
                      column= 4, 
                      pady = 1)
 
# Button cosh
btnCosh = Button(calc, 
                 text="Cosh",
                 width=6,
                 height=2,
                 bg='black',
                 fg='white',
                 font=('Helvetica',
                       20,
                       'bold'),
                 bd=4,
                 command=added_value.cosh
                ).grid(row=2, 
                       column= 5, 
                       pady = 1)
 
# Button tanh
btntanh = Button(calc, 
                 text="tanh",
                 width=6, 
                 height=2,
                 bg='black',
                 fg='white',
                 font=('Helvetica',
                       20,
                       'bold'),
                 bd=4,
                 command=added_value.tanh
                ).grid(row=2, 
                       column= 6, 
                       pady = 1)
 
# Button sinh
btnsinh = Button(calc, 
                 text="sinh",
                 width=6, 
                 height=2,
                 bg='black',
                 fg='white',
                 font=('Helvetica',
                       20,
                       'bold'),
                 bd=4,
                 command=added_value.sinh
                ).grid(row=2, 
                       column= 7, 
                       pady = 1)
 
# ROW 3 :
# Button log
btnlog = Button(calc, 
                text="log",
                width=6,
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.log
               ).grid(row=3, 
                      column= 4, 
                      pady = 1)
 
# Button exp
btnExp = Button(calc, 
                text="exp",
                width=6, 
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.exp
               ).grid(row=3, 
                      column= 5, 
                      pady = 1)
 
# Button mod
btnMod = Button(calc, 
                text="Mod",
                width=6,
                height=2,
                bg='black',
                fg='white', 
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=lambda:added_value.operation("mod")
                ).grid(row=3, 
                       column= 6, 
                       pady = 1)
 
# Button e
btnE   = Button(calc, 
                text="e",
                width=6, 
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.e
               ).grid(row=3, 
                      column= 7, 
                      pady = 1)
 
# ROW 4 :
# Button log10
btnlog10 = Button(calc, 
                  text="log10",
                  width=6, 
                  height=2,
                  bg='black',
                  fg='white', 
                  font=('Helvetica',
                        20,
                        'bold'),
                  bd=4,
                  command=added_value.log10
                 ).grid(row=4, 
                        column= 4, 
                        pady = 1)
 
# Button log1p
btncos   = Button(calc, 
                  text="log1p",
                  width=6,
                  height=2,
                  bg='black',
                  fg='white',
                  font=('Helvetica',
                        20,
                        'bold'),
                  bd=4,
                  command=added_value.log1p
                 ).grid(row=4, 
                        column= 5, 
                        pady = 1)
 
# Button expm1
btnexpm1 = Button(calc, 
                  text="expm1",
                  width=6,
                  height=2,
                  bg='black',
                  fg='white',
                  font=('Helvetica',
                        20,
                        'bold'),
                  bd = 4,
                  command=added_value.expm1
                 ).grid(row=4, 
                        column= 6, 
                        pady = 1)
 
# Button gamma
btngamma = Button(calc, 
                  text="gamma",
                  width=6,
                  height=2,
                  bg='black',
                  fg='white',
                  font=('Helvetica',
                        20,
                        'bold'),
                  bd=4,
                  command=added_value.lgamma
                 ).grid(row=4, 
                        column= 7, 
                        pady = 1)

# ROW 5 :
# Button log2
btnlog2 = Button(calc, 
                 text="log2",
                 width=6, 
                 height=2,
                 bg='black',
                 fg='white',
                 font=('Helvetica',
                       20,
                       'bold'),
                 bd=4,
                 command=added_value.log2
                ).grid(row=5, 
                       column= 4, 
                       pady = 1)
 
# Button deg
btndeg = Button(calc, 
                text="deg",
                width=6, 
                height=2,
                bg='black',
                fg='white',
                font=('Helvetica',
                      20,
                      'bold'),
                bd=4,
                command=added_value.degrees
               ).grid(row=5, 
                      column= 5, 
                      pady = 1)
 
# Button acosh
btnacosh = Button(calc, 
                  text="acosh",
                  width=6,
                  height=2,
                  bg='black',
                  fg='white',
                  font=('Helvetica',
                        20,
                        'bold'),
                  bd=4,
                  command=added_value.acosh
                 ).grid(row=5, 
                        column= 6, 
                        pady = 1)
 
# Button asinh
btnasinh = Button(calc, 
                  text="asinh",
                  width=6, 
                  height=2,
                  bg='black',
                  fg='white',
                  font=('Helvetica',
                        20,
                        'bold'),
                  bd=4,
                  command=added_value.asinh
                 ).grid(row=5, 
                        column= 7, 
                        pady = 1)
 
# Label Scientific Calculator
lblDisplay = Label(calc, 
                   text = "Scientific Calculator",
                   font=('Helvetica',
                         30,
                         'bold'),
                   bg='black',
                   fg='white',
                   justify=CENTER)
 
lblDisplay.grid(row=0, column= 4,columnspan=4)
 
# Exit
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return
 
# Scientific
def Scientific():
    root.resizable(width=False, 
                   height=False)
    root.geometry("944x568+0+0")
 
 
# Standard
def Standard():
    root.resizable(width=False, 
                   height=False)
    root.geometry("480x568+0+0")
 
menubar = Menu(calc)
 
# ManuBar 1 :
filemenu = Menu(menubar, 
                tearoff = 0)
# cascade File
menubar.add_cascade(label = 'File', 
                    menu = filemenu)
# command Standard
filemenu.add_command(label = "Standard", 
                     command = Standard)
# command Scientific
filemenu.add_command(label = "Scientific", 
                     command = Scientific) 
filemenu.add_separator()
# command Exit
filemenu.add_command(label = "Exit", 
                     command = iExit)
 
# ManuBar 2 :
editmenu = Menu(menubar, 
                tearoff = 0)
# cascade Edit
menubar.add_cascade(label = 'Edit', 
                    menu = editmenu)
# command Cut
editmenu.add_command(label = "Cut")
# command Copy
editmenu.add_command(label = "Copy")
editmenu.add_separator()
# command Paste
editmenu.add_command(label = "Paste")
 
root.config(menu=menubar)
 
root.mainloop()
