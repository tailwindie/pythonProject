from tkinter import *


#-----------------------------------

def btnNumber(numb):
    global num # кнопки с цифрами

    if numb == "0":
        num = int(numb)
        field.insert('end', num)
    if numb == "1":
        num = int(numb)
        field.insert('end', num)
    if numb == "2":
        num = int(numb)
        field.insert('end', num)
    if numb == "3":
        num = int(numb)
        field.insert('end', num)
    if numb == "4":
        num = int(numb)
        field.insert('end', num)
    if numb == "5":
        num = int(numb)
        field.insert('end', num)
    if numb == "6":
        num = int(numb)
        field.insert('end', num)
    if numb == "7":
        num = int(numb)
        field.insert('end', num)
    if numb == "8":
        num = int(numb)
        field.insert('end', num)
    if numb == "9":
        num = int(numb)
        field.insert('end', num)

#-----------------------------------

def btnFunc(type):
    global res
    global glres
    global a1

    res = ""
    glres = 0
    gltype = ""
    lbl.configure(text=res)
    a = " {}".format(field.get())
    if a == " ": # не написал число, но нажимает действие
        lbl.configure(text="Сначала впишите число!")
        pass
    else:
        a1 = float(format(field.get())) # считаем
        if type == "sqrt":
            glres = a1 ** 0.5
            lbl.configure(text="v" + a + " = " + str(glres))
        elif type == "deg":
            glres = a1 ** 2
            lbl.configure(text=a + "? = " + str(glres))
        elif type == "1/x":
            glres = 1 / a1
            lbl.configure(text="1 /" + a + " = " + str(glres))

        field.delete(0, 'end')

#-----------------------------------

def btnClicked(type):
    global res
    global glres
    global gltype
    global a1

    a = " {}".format(field.get())
    b = " " + type
    if a == " ": # не написал число, но нажимает действие
        lbl.configure(text="Сначала впишите число!")
        pass
    else:
        a1 = float(format(field.get()))
        if type != "=":
            if res == "" or gltype == "=":
                res = ""
                glres = a1
                if type == "+": # фиксирует предыдущую кнопку, чтоб посчитать
                    gltype = "+"
                if type == "*":
                    gltype = "*"
                if type == "-":
                    gltype = "-"
                if type == "/":
                    gltype = "/"
            else:
                if gltype == "+": # считает
                    glres += a1
                    gltype = type
                elif gltype == "*":
                    glres *= a1
                    gltype = type
                elif gltype == "-":
                    glres -= a1
                    gltype = type
                elif gltype == "/":
                    glres /= a1
                    gltype = type
                elif gltype == "=":
                    res = a1
                    glres = a1
                    if type == "+":  # фиксирует предыдущую кнопку, чтоб посчитать
                        gltype = "+"
                    if type == "*":
                        gltype = "*"
                    if type == "-":
                        gltype = "-"
                    if type == "/":
                        gltype = "/"
            res += a + b
            lbl.configure(text=res)
            field.delete(0, 'end')

        else:
            if res == "" or gltype == "=": # если нажали =, но ничего не вписали перед этим или перед этим нажали =
                res = ""
                lbl.configure(text="")
                glres = a1
            elif gltype == "+": # фиксирует предыдущую кнопку, чтоб посчитать
                glres += a1
                gltype = type
            elif gltype == "*":
                glres *= a1
                gltype = type
            elif gltype == "-":
                glres -= a1
                gltype = type
            elif gltype == "/":
                glres /= a1
                gltype = type
            res += a + b + " " + str(glres) # считаем перед выводом
            lbl.configure(text=res) # выводим
            field.delete(0, 'end') # очищаем поле

#-----------------------------------

def btnClear(clea):
    global res
    global glres
    global gltype
    global a1

    if clea == "clea":
        res = ""
        glres = 0
        gltype = ""
        a1 = 0
        lbl.configure(text="")
        field.delete(0, 'end')
        field.insert(0, "")


#-----------------------------------

window = Tk()
window.title("Калькулятор")
window.geometry('240x320')

res = ""
glres = 0
gltype = ""

field = Entry(window, width=20, font=("Arial Bold", 14))
field.place(x=10, y=32)

lbl = Label(window, text="", font=("Arial Bold", 14))
lbl.place(x=1, y=1)

#-----------------------------------------------------------------------------------

btnSum = Button(window, text="+", command=lambda:btnClicked("+"), font=("Arial", 12), width=2, height=1)
btnSum.pack()
btnSum.place(x=16, y=74)

btnSubt = Button(window, text="-", command=lambda:btnClicked("-"), font=("Arial", 12), width=2, height=1)
btnSubt.pack()
btnSubt.place(x=54, y=74)

btnMult = Button(window, text="*", command=lambda:btnClicked("*"), font=("Arial", 12), width=2, height=1)
btnMult.pack()
btnMult.place(x=92, y=74)

btnDiv = Button(window, text="/", command=lambda:btnClicked("/"), font=("Arial", 12), width=2, height=1)
btnDiv.pack()
btnDiv.place(x=130, y=74)

btnSqrt = Button(window, text="v", command=lambda:btnFunc("sqrt"), font=("Arial", 12), width=2, height=1)
btnSqrt.pack()
btnSqrt.place(x=130, y=114)

btnDiv = Button(window, text="x?", command=lambda:btnFunc("deg"), font=("Arial", 12), width=2, height=1)
btnDiv.pack()
btnDiv.place(x=92, y=114)

btnDiv = Button(window, text="1/x", command=lambda:btnFunc("1/x"), font=("Arial", 12), width=2, height=1)
btnDiv.pack()
btnDiv.place(x=54, y=114)

#-----------------------------------------------------------------------------------

btnEq= Button(window, text="=", command=lambda:btnClicked("="), font=("Arial", 12), width=4, height=2)
btnEq.pack()
btnEq.place(x=180, y=74)

btnCle= Button(window, text="C", command=lambda:btnClear("clea"), font=("Arial", 12), width=4, height=2)
btnCle.pack()
btnCle.place(x=180, y=130)

#-----------------------------------------------------------------------------------

btn1= Button(window, text="1", command=lambda:btnNumber("1"), font=("Arial", 12), width=2, height=1)
btn1.pack()
btn1.place(x=54, y=164)

btn2= Button(window, text="2", command=lambda:btnNumber("2"), font=("Arial", 12), width=2, height=1)
btn2.pack()
btn2.place(x=92, y=164)

btn3= Button(window, text="3", command=lambda:btnNumber("3"), font=("Arial", 12), width=2, height=1)
btn3.pack()
btn3.place(x=130, y=164)

btn4= Button(window, text="4", command=lambda:btnNumber("4"), font=("Arial", 12), width=2, height=1)
btn4.pack()
btn4.place(x=54, y=204)

btn5= Button(window, text="5", command=lambda:btnNumber("5"), font=("Arial", 12), width=2, height=1)
btn5.pack()
btn5.place(x=92, y=204)

btn6= Button(window, text="6", command=lambda:btnNumber("6"), font=("Arial", 12), width=2, height=1)
btn6.pack()
btn6.place(x=130, y=204)

btn7= Button(window, text="7", command=lambda:btnNumber("7"), font=("Arial", 12), width=2, height=1)
btn7.pack()
btn7.place(x=54, y=244)

btn8= Button(window, text="8", command=lambda:btnNumber("8"), font=("Arial", 12), width=2, height=1)
btn8.pack()
btn8.place(x=92, y=244)

btn9= Button(window, text="9", command=lambda:btnNumber("9"), font=("Arial", 12), width=2, height=1)
btn9.pack()
btn9.place(x=130, y=244)

btn0= Button(window, text="0", command=lambda:btnNumber("0"), font=("Arial", 12), width=2, height=1)
btn0.pack()
btn0.place(x=92, y=284)



#btnMult = Button()
#btnMult.pack()

window.mainloop()