from tkinter import *

root = Tk()
root.title("Calculator")
canv = Canvas(root, height=455, width=525, bg="lightgray")
canv.pack()
m = Menu(root)
fm = Menu(m)
m.add_cascade(label='About', menu=fm)
canv.create_rectangle(3, 3, 525, 150, fill="white", outline="black", width=3)
s = ''
exemple = []
i = 0
flag = True


def about():
    new_window = Toplevel()
    lab = Label(new_window, text='''Этот калькулятор был создан Шариповым Андреем.
    Программа способна автоматически выявить порядок действий для примера. После вывода ответа возможна дальнейшая работа
    с этим ответом, либо ввод нового примера путем нажатия любой цифровой кнопки.
    ©Copyright
    2019''')
    lab.pack()


def f_btn_1(event):
    global s
    global global_lab
    s += '1'
    global_lab['text'] += '1'


def pop_elems(temp):
    global exemple
    global i
    global res
    exemple.pop(i - 1)
    exemple.pop(i - 1)
    exemple.pop(i - 1)
    exemple.insert(i - 1, temp)
    i -= 1
    res = temp


def calculator():
    global i
    global exemple
    global global_lab
    global s
    global temp
    res = 0
    i = 0
    while i < len(exemple):
        if exemple[i] == '*':
            temp = exemple[i - 1] * exemple[i + 1]
            pop_elems(temp)
        elif exemple[i] == '/':
            try:
                exemple[i - 1] / exemple[i + 1]
            except(ZeroDivisionError):
                global_lab['text'] = 'ZeroDivisionError'
                s = ''
                exemple = []
                break
            temp = exemple[i - 1] / exemple[i + 1]
            pop_elems(temp)
        i += 1
    i = 0
    while i < len(exemple):
        if exemple[i] == '+':
            temp = exemple[i - 1] + exemple[i + 1]
            pop_elems(temp)
        elif exemple[i] == '-':
            temp = exemple[i - 1] - exemple[i + 1]
            pop_elems(temp)
        i += 1
    global_lab['text'] = str(temp)
    s = str(temp)


def f_btn_c(event):
    global s
    global global_lab
    global exemple
    s = ''
    exemple = []
    global_lab['text'] = ''


def f_btn_4(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag == True:
        s += '4'
        global_lab['text'] += '4'
    else:
        flag = True
        s = '4'
        global_lab['text'] = '4'
        exemple = []


def f_btn_7(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag == True:
        s += '7'
        global_lab['text'] += '7'
    else:
        flag = True
        s = '7'
        global_lab['text'] = '7'
        exemple = []


def f_btn_(event):
    global s
    global global_lab
    s += '.'
    global_lab['text'] += '.'


def f_btn_sqrt(event):
    global s
    global global_lab
    global_lab['text'] = str(float(s) ** 0.5)
    s = str(float((s)) ** 0.5)


def f_btn_2(event):
    global s
    global global_lab
    global flag
    global exemple
    if flag:
        s += '2'
        global_lab['text'] += '2'
    else:
        flag = True
        s = '2'
        global_lab['text'] = '2'
        exemple = []


def f_btn_5(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag:
        s += '5'
        global_lab['text'] += '5'
    else:
        flag = True
        s = '5'
        global_lab['text'] = '5'
        exemple = []


def f_btn_8(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag == True:
        s += '8'
        global_lab['text'] += '8'
    else:
        flag = True
        s = '8'
        global_lab['text'] = '8'
        exemple = []


def f_btn_0(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag:
        s += '0'
        global_lab['text'] += '0'
    else:
        flag = True
        s = '0'
        global_lab['text'] = '0'
        exemple = []


def f_btn_sq(event):
    global s
    global global_lab
    global_lab['text'] = str(float(s) ** 2)
    s = str(float(s) ** 2)


def f_btn_3(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag:
        s += '3'
        global_lab['text'] += '3'
    else:
        flag = True
        s = '3'
        global_lab['text'] = '3'
        exemple = []


def f_btn_6(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag:
        s += '6'
        global_lab['text'] += '6'
    else:
        flag = True
        s = '6'
        global_lab['text'] = '6'
        exemple = []


def f_btn_9(event):
    global exemple
    global s
    global global_lab
    global flag
    if flag:
        s += '9'
        global_lab['text'] += '9'
    else:
        flag = True
        s = '9'
        global_lab['text'] = '9'
        exemple = []


def f_btn_eq(event):
    global s
    global global_lab
    global exemple
    global flag
    flag = False
    exemple.append(float(s))
    calculator()


def f_btn_plus(event):
    global s
    global global_lab
    global exemple
    global flag
    flag = True
    exemple.append(float(s))
    exemple.append('+')
    s = ''
    global_lab['text'] += '+'


def f_btn_min(event):
    global s
    global global_lab
    global exemple
    global flag
    flag = True
    exemple.append(float(s))
    exemple.append('-')
    s = ''
    global_lab['text'] += '-'


def f_btn_mul(event):
    global s
    global global_lab
    global exemple
    global flag
    flag = True
    exemple.append(float(s))
    exemple.append('*')
    s = ''
    global_lab['text'] += '*'


def f_btn_div(event):
    global s
    global global_lab
    global exemple
    global flag
    flag = True
    exemple.append(float(s))
    exemple.append('/')
    s = ''
    global_lab['text'] += '/'


fm.add_command(label='Inforation', command=about)
global_lab = Label(canv, text='', width=22, height=3, font='Arial 30', bg='white')
global_lab.place(x=5, y=8)

btn_c = Button(canv, text='C', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_c.place(x=5, y=155)
btn_c.bind('<Button-1>', f_btn_c)
btn_1 = Button(canv, text='1', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_1.place(x=5, y=215)
btn_1.bind('<Button-1>', f_btn_1)
btn_4 = Button(canv, text='4', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_4.place(x=5, y=275)
btn_4.bind('<Button-1>', f_btn_4)
btn_7 = Button(canv, text='7', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_7.place(x=5, y=335)
btn_7.bind('<Button-1>', f_btn_7)
btn_ = Button(canv, text=',', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_.place(x=5, y=395)
btn_.bind('<Button-1>', f_btn_)

btn_sqrt = Button(canv, text='√', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_sqrt.place(x=135, y=155)
btn_sqrt.bind('<Button-1>', f_btn_sqrt)
btn_2 = Button(canv, text='2', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_2.place(x=135, y=215)
btn_2.bind('<Button-1>', f_btn_2)
btn_5 = Button(canv, text='5', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_5.place(x=135, y=275)
btn_5.bind('<Button-1>', f_btn_5)
btn_8 = Button(canv, text='8', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_8.place(x=135, y=335)
btn_8.bind('<Button-1>', f_btn_8)
btn_0 = Button(canv, text='0', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_0.place(x=135, y=395)
btn_0.bind('<Button-1>', f_btn_0)

btn_sq = Button(canv, text='x^2', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_sq.place(x=265, y=155)
btn_sq.bind('<Button-1>', f_btn_sq)
btn_3 = Button(canv, text='3', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_3.place(x=265, y=215)
btn_3.bind('<Button-1>', f_btn_3)
btn_6 = Button(canv, text='6', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_6.place(x=265, y=275)
btn_6.bind('<Button-1>', f_btn_6)
btn_9 = Button(canv, text='9', width=15, height=3, font='Arial 10', bg='white', bd=1)
btn_9.place(x=265, y=335)
btn_9.bind('<Button-1>', f_btn_9)

btn_div = Button(canv, text='/', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_div.place(x=395, y=155)
btn_div.bind('<Button-1>', f_btn_div)
btn_mul = Button(canv, text='*', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_mul.place(x=395, y=215)
btn_mul.bind('<Button-1>', f_btn_mul)
btn_min = Button(canv, text='-', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_min.place(x=395, y=275)
btn_min.bind('<Button-1>', f_btn_min)
btn_plus = Button(canv, text='+', width=15, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_plus.place(x=395, y=335)
btn_plus.bind('<Button-1>', f_btn_plus)
btn_eq = Button(canv, text='=', width=31, height=3, font='Arial 10', bg='lightgray', bd=1)
btn_eq.place(x=265, y=395)
btn_eq.bind('<Button-1>', f_btn_eq)

root.config(menu=m)
root.mainloop()