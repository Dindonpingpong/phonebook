"""
Created on Tue May 30 23:10:38 2017
Автор: Гостищева П.
Группа: ПМ1-4
Тема: 23. Кредиты
"""
#Необходимое условие: ФИО студента, балл за 1 аттестацию, балл за 2 аттестацию, оценка за экзамен, итоговая оценка
import pickle
import os
from tkinter import *
from tkinter import messagebox        #для вывода в окне сообщения
 
class Bank: 
    def __init__(self, name, credit_amount, term, percent): #констуктор 
#       атрибуты класса
        self.name = name 
        self.credit_amount  = int(credit_amount)
        self.term = int(term) 
        self.percent = int(percent)

        
    def __str__(self): #вызывается функциями str, print и format и возвращает строковое представление объекта
        return 'ФИО: {}, сумма кредита: {}, срок кредита(в годах): {}, процент: {}'.format(self.name,self.credit_amount,self.term, self.percent)

    def getVar(self): 
        return (int(self.credit_amount))  # чтение (свойство класса)
    cost = property(getVar)
    

#----------------------------------------------------------------------        
def total_cost(lst):
    s=0
    for i in lst:
        s+=i.cost
    return s


def h1(event):
    lab_cost['text'] = total_cost(credits_banks)


def h2(event):
    t=Bank(ent1.get(), ent2.get(), ent3.get(), ent4.get()) 
    lst.insert(END, t)
    credits_banks.append(t)
    
def h3(event):
    idx = lst.curselection()
    if (idx == tuple()):
        print('Чтобы удалить объект, его надо предварительно выделить!')
        return
    else:
        lst.delete(idx)   
        credits_banks.pop(idx[0])
    
    
def h4(event):
    f = open('credits_banks', 'wb')
    pickle.dump(credits_banks, f)
    f.close()    
    
def maxpercent(event):
    data=[]
    for i in credits_banks:
        data.append(i.percent)
    lab_max_percent['text']=max(data)
    
def lencr(event):
    lab_credits['text']=len(credits_banks)
#------------------------------------------------------------------------------
try:
    # Десериализуем объекты из файла
    with open('credits_banks', 'rb') as i:
                credits_banks=pickle.load(i)
except:
    # Создаем список вручную
    t1 = Bank('Путин Владимир Владимирович', 10000000, 15, 33)
    t2 = Bank('Медведев Дмитрий Анатольевич', 600000, 3, 40)
    t3 = Bank('Ленин Владимир Ильич', 5500000, 5, 13)
    t4 = Bank('Усманов Алишер Бухманович', 990000000, 3, 41)
    credits_banks = [t1,t2,t3,t4]

#------------------------------------------------------------------------------
root = Tk()
root.configure(bg="#1876FF")

lst = Listbox(root, selectmode=SINGLE, height = 10, width = 80)

scroll = Scrollbar(command = lst.yview)
#scroll.pack(side = LEFT, fill = Y)

butSum = Button(root, text="Общая задолженность банку",bg="#1876FF", fg="#263140", height= 15)
lab_cost = Label(root, font="Arial 12", text="0",bg="#1876FF", fg="#263140")
lab_max_percent = Label(root, font="Arial 12", text="0",bg="#1876FF", fg="#263140")
lab_credits = Label(root, font="Arial 12", text="0",bg="#1876FF", fg="#263140")

lab_name = Label(root, font="Algerian 20", text = "Gorelov Bank",bg="#1876FF", fg="#263140")
lab_tagline = Label(root, font="Gabriola 14", text = "С нами не прогоришь",bg="#1876FF", fg="#263140")
#-----------------------------------------------------------------------------
lab1 = Label(root, text="ФИО",bg="#1876FF", fg="#263140")
ent1 = Entry(root, width=16)
lab2 = Label(root, text="Сумма кредита", bg="#1876FF", fg="#263140")
ent2 = Entry(root, width=16)
lab3 = Label(root, text="Срок кредита", bg="#1876FF", fg="#263140")
ent3 = Entry(root, width=15)
lab4 = Label(root, text="Процент", bg="#1876FF", fg="#263140")
ent4 = Entry(root, width=12)
butAdd = Button(root, text="Создать объект", bg="#1876FF", fg="#263140")
butDel = Button(root, text="Удалить объект", bg="#1876FF", fg="#263140")
butSave = Button(root, text="Сохранить список", bg="#1876FF", fg="#263140")
butMaxPer = Button(root, text="Максимальный процент", bg="#1876FF", fg="#263140")
butLen = Button(root, text="Количество кредитов", bg="#1876FF", fg="#263140")
lab5 = Label(root)

for i in credits_banks:
     lst.insert(END, i) 

#------------------------------------------------------------------------------
lst.grid(row=0, column=0, rowspan=3, padx=10, pady=10)     
scroll.grid(row = 5, column = 0)
butSum.grid(row=0, column=1, sticky = "nsew")
butMaxPer.grid(row=1, column=1, sticky = "nsew")
butLen.grid(row=2, column=1, sticky = "nsew")

lab_cost.grid(row=0, column=2, sticky='nsew')
lab_max_percent.grid(row=1, column=2, sticky='nsew')
lab_credits.grid(row=2, column=2, sticky='nsew')

lab_name.grid(row=0, column=3, padx=10)
lab_tagline.grid(row=1, column=3, padx=10)

lab1.grid(row=3, column=1, padx=10)
lab2.grid(row=3, column=2, padx=10)
lab3.grid(row=3, column=3, padx=10)
lab4.grid(row=3, column=4, padx=10)


ent1.grid(row=4, column=1, padx=10)
ent2.grid(row=4, column=2, padx=10)
ent3.grid(row=4, column=3, padx=10)
ent4.grid(row=4, column=4, padx=10)
butAdd.grid(row=6, column=2, columnspan=2, padx=10)

butDel.grid(row=3, column=0)
butSave.grid(row=4, column=0)

butSum.bind("<Button-1>",h1)
butAdd.bind("<Button-1>",h2)
butDel.bind("<Button-1>",h3)
butSave.bind("<Button-1>",h4)
butMaxPer.bind('<Button-1>', maxpercent)
butLen.bind('<Button-1>', lencr)


root.mainloop()