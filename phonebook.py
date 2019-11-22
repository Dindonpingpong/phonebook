import pickle
import os
from tkinter import *
from tkinter import messagebox as mb
from datetime import date

class Phone: 
    def __init__(self, surname, name,  number, country, city, date): #констуктор 
#       атрибуты класса
        self.surname = surname
        self.name = name 
        self.number = number
        self.country = country
        self.city = city
        self.date = date

        
    def __str__(self): #вызывается функциями str, print и format и возвращает строковое представление объекта
        return '{} {} {} {} {} {}'.format(self.surname, self.name, self.number, self.country, self.city, self.date)

#----------------------------------------------------------------------        



#------------------------------------------------------------------------------

try:
    with open('phonebook_data', 'rb') as i:
        data = pickle.load(i)
except:
    data = []


#------------------------------------------------------------------------------
root = Tk()
root.configure(bg = "#263140")

#-----------------------------------------------------------------------------
lbl1 = Label(root, text = 'Телефонный справочник')
lbl2 = Label(root, text = 'Фамилия')
lbl3 = Label(root, text = 'Имя')
lbl4 = Label(root, text = 'Номер')
lbl5 = Label(root, text = 'Страна')
lbl6 = Label(root, text = 'Город')
lbl7 = Label(root, text = 'Дата рождения')
lbl8 = Label(root, text = 'Фамилия')
lbl9 = Label(root, text = 'Имя')
lbl10 = Label(root, text = 'Номер')
lbl11 = Label(root, text = 'Страна')
lbl12 = Label(root, text = 'Город')
lbl13 = Label(root, text = 'Дата рождения')

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

box = Listbox(root, selectmode = SINGLE, height = 40, width = 125)

#------------------------------------------------------------------------------

def check_corr_date(day,month,year):
    try:
        date(year, month, day)
        return False
    except:
        return True

def check_input_for_add(record):
    if len(record.surname) == 0:
        mb.showerror('Ошибка','Заполните поле Фамилия')
        return (1)
    else:
        if record.surname.islower():
            mb.showerror('Ошибка','Введите фамилию с заглавной буквы')
            return(1)
    if len(record.name) == 0:
        mb.showerror('Ошибка','Заполните поле Имя')
        return (1)
    else:
        if record.name.islower():
            mb.showerror('Ошибка','Введите имя с заглавной буквы')
            return(1)
    if len(record.number) == 0:
        mb.showerror('Ошибка','Заполните поле Номер')
        return (1)
    else:
        if record.number[0] != '+' and record.number[1] != '7':
            mb.showerror('Ошибка','Введите номер в формате: +7')
            return (1)
        if len(record.number) != 12:    
            mb.showerror('Ошибка','Введите 11 цифр')
            return (1)
    if len(record.country) > 0:
        if record.country.islower():
            mb.showerror('Ошибка','Введите страну с заглавной буквы')
            return (1)
    if len(record.city) > 0:
        if record.city.islower():
            mb.showerror('Ошибка','Введите город с заглавной буквы')
            return (1)
    if len(record.date) > 0:
        if len(record.date) != 10:
            mb.showerror('Ошибка','Введите дату рождения в формате: ДД.ММ.ГГГГ')
            return (1)
        if check_corr_date(int(record.date[0:2]),int(record.date[3:5]),int(record.date[6:8])):
            mb.showerror('Ошибка','Введите корректную дату')
            return (1)
    return (0)

def add_record(event):
    record = Phone(ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get())
    if check_input_for_add(record) == 1:
        return
    else:
        box.insert(END, record)
        data.append(record)



#------

for record in data:
    box.insert(END, record)

#------------------------------------------------------------------------------

lbl1.grid(columnspan = 6)
lbl2.grid(row = 1, column = 0)
lbl3.grid(row = 1, column = 1)
lbl4.grid(row = 1, column = 2)
lbl5.grid(row = 1, column = 3)
lbl6.grid(row = 1, column = 4)
lbl7.grid(row = 1, column = 5)
lbl8.grid(row = 4, column = 0)
lbl9.grid(row = 4, column = 1)
lbl10.grid(row = 4, column = 2)
lbl11.grid(row = 4, column = 3)
lbl12.grid(row = 4, column = 4)
lbl13.grid(row = 4, column = 5)

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

btn2.bind("<Button-1>", add_record)

root.mainloop()