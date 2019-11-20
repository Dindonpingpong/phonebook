import pickle
import os
from tkinter import *
from tkinter import messagebox
 
class Phone: 
    def __init__(self, surname, name,  number, DD, MM, YY): #констуктор 
#       атрибуты класса
        self.surname = surname
        self.name = name 
        self.number = number
        self.day = MM
        self.month = MM
        self.year = YY

        
    def __str__(self): #вызывается функциями str, print и format и возвращает строковое представление объекта
        return 'Name: {} {}, number: {}, date: {}'.format(self.surname, self.name, self.number, self.year)

#----------------------------------------------------------------------        

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
root = Tk()
root.configure(bg = "#263140")

#-----------------------------------------------------------------------------
lbl1 = Label(root, text = 'Телефонный справочник')
lbl2 = Label(root, text = 'Фамилия')
lbl3 = Label(root, text = 'Имя')
lbl4 = Label(root, text = 'Номер')
lbl5 = Label(root, text = 'День')
lbl6 = Label(root, text = 'Месяц')
lbl7 = Label(root, text = 'Год')
lbl8 = Label(root, text = 'Фамилия')
lbl9 = Label(root, text = 'Имя')
lbl10 = Label(root, text = 'Дата рождения')

ent1 = Entry(root)
ent2 = Entry(root)
ent3 = Entry(root)
ent4 = Entry(root)
ent5 = Entry(root)
ent6 = Entry(root)

btn1 = Button(root, text = 'Найти')
btn2 = Button(root, text = 'Добавить')
btn3 = Button(root, text = 'Изменить')
btn4 = Button(root, text = 'Удалить')

box = Listbox(root, selectmode = SINGLE, height = 50, width = 120)

#------------------------------------------------------------------------------



#------------------------------------------------------------------------------

lbl1.grid(columnspan = 6)
lbl2.grid(row = 1, column = 0)
lbl3.grid(row = 1, column = 1)
lbl4.grid(row = 1, column = 2)
lbl5.grid(row = 1, column = 3)
lbl6.grid(row = 1, column = 4)
lbl7.grid(row = 1, column = 5)
lbl8.grid(row = 4, column = 1)
lbl9.grid(row = 4, column = 2)
lbl10.grid(row = 4, column = 3, columnspan = 3)

ent1.grid(row = 2, column = 0)
ent2.grid(row = 2, column = 1)
ent3.grid(row = 2, column = 2)
ent4.grid(row = 2, column = 3)
ent5.grid(row = 2, column = 4)
ent6.grid(row = 2, column = 5)

btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)
btn4.grid(row = 3, column = 5)

box.grid(row = 5, columnspan = 6, padx = 5, pady = 10)

root.mainloop()