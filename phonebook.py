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

try:
    with open('phonebook_data', 'rb') as i:
        data = pickle.load(i)
except:
    data = []

#------------------------------------------------------------------------------
root = Tk()
root.configure(bg = '#263140')

                                                   
#-----------------------------------------------------------------------------
lbl1 = Label(root, text = 'Телефонный справочник', bg = "#263140", fg = '#f5f3f0')
lbl2 = Label(root, text = 'Фамилия', bg = "#263140", fg = '#f5f3f0')
lbl3 = Label(root, text = 'Имя', bg = "#263140", fg = '#f5f3f0')
lbl4 = Label(root, text = 'Номер', bg = "#263140", fg = '#f5f3f0')
lbl5 = Label(root, text = 'Страна', bg = "#263140", fg = '#f5f3f0')
lbl6 = Label(root, text = 'Город', bg = "#263140", fg = '#f5f3f0')
lbl7 = Label(root, text = 'Дата рождения', bg = "#263140", fg = '#f5f3f0')
lbl8 = Label(root, text = 'Фамилия', bg = "#263140", fg = '#f5f3f0')
lbl9 = Label(root, text = 'Имя', bg = "#263140", fg = '#f5f3f0')
lbl10 = Label(root, text = 'Номер', bg = "#263140", fg = '#f5f3f0')
lbl11 = Label(root, text = 'Страна', bg = "#263140", fg = '#f5f3f0')
lbl12 = Label(root, text = 'Город', bg = "#263140", fg = '#f5f3f0')
lbl13 = Label(root, text = 'Дата рождения', bg = "#263140", fg = '#f5f3f0')
lbl14 = Label(root, bg = "#5f718a", width = 110)

ent1 = Entry(root)
ent2 = Entry(root)
ent3 = Entry(root)
ent4 = Entry(root)
ent5 = Entry(root)
ent6 = Entry(root)

btn1 = Button(root, text = 'Сохранить')
btn2 = Button(root, text = 'Найти')
btn3 = Button(root, text = 'Добавить')
btn4 = Button(root, text = 'Изменить')
btn5 = Button(root, text = 'Показать всё')
btn6 = Button(root, text = 'Удалить')


box = Listbox(root, selectmode = SINGLE, height = 40, width = 125)
#------funtions------------------------------------------------------------------------

def check_corr_date(day,month,year):
    try:
        date(year, month, day)
        return False
    except:
        return True

def check_name_exist(record):
    for el in data:
        if el.surname == record.surname and el.name == record.name:
            mb.showerror('Ошибка','Уже существует в справочнике такой человек')
            return (1)
    return (0)

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
    if check_name_exist(record) == 1:
        return
    else:
        box.insert(END, record)
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)
        data.append(record)

def save_file(event):
    fd = open('phonebook_data', 'wb')
    pickle.dump(data, fd)
    fd.close()

def show_all(event):
    box.delete(0, END)
    for record in data:
        box.insert(END, record)

def find(event):
    
#--------------------------------------------------------------------------------



#------------------------------------------------------------------------------
lbl1.grid(columnspan = 5, pady = 6)
lbl2.grid(row = 1, column = 0, pady = 4)
lbl3.grid(row = 1, column = 1, pady = 4)
lbl4.grid(row = 1, column = 2, pady = 4)
lbl5.grid(row = 1, column = 3, pady = 4)
lbl6.grid(row = 1, column = 4, pady = 4)
lbl7.grid(row = 1, column = 5, pady = 2)
lbl8.grid(row = 5, column = 0, pady = 2)
lbl9.grid(row = 5, column = 1, pady = 2)
lbl10.grid(row = 5, column = 2, pady = 2)
lbl11.grid(row = 5, column = 3, pady = 2)
lbl12.grid(row = 5, column = 4, pady = 2)
lbl13.grid(row = 5, column = 5, pady = 2)
lbl14.grid(row = 4, columnspan = 6)

ent1.grid(row = 2, column = 0)
ent2.grid(row = 2, column = 1)
ent3.grid(row = 2, column = 2)
ent4.grid(row = 2, column = 3)
ent5.grid(row = 2, column = 4)
ent6.grid(row = 2, column = 5)

btn1.grid(row = 0, column = 5, pady = 4)
btn2.grid(row = 3, column = 0, pady = 4)
btn3.grid(row = 3, column = 1, pady = 4)
btn4.grid(row = 3, column = 2, pady = 4)
btn5.grid(row = 6, column = 0, columnspan = 2, pady = 2)
btn6.grid(row = 6, column = 5, pady = 4)


box.grid(row = 7, columnspan = 6, padx = 5, pady = 10)

btn1.bind('<Button-1>', save_file)
btn2.bind('<Button-1>')
btn3.bind('<Button-1>', add_record)
btn4.bind('<Button-1>')
btn5.bind('<Button-1>', show_all)
btn6.bind('<Button-1>')

root.mainloop()