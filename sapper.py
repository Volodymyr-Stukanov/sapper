from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pickle
import random
import sys


def choise():
    buttonV_enter=Button(text='Войти',command=lambda:login(1))
    buttonZ_enter=Button(text='Зарегестрироваться',command=lambda:regestration())
    buttonV_enter.pack()
    buttonZ_enter.pack()    
    
def regestration():#функция
    root.destroy()
    levelWindow1=Tk()
    levelWindow1.geometry('300x500')
    levelWindow1.title('Войти')
    
    text=Label(text='Для входа в систему- зарегестрируйтесь!')
    text_login=Label(text="Введите ваш логин: ")
    registr_login=Entry()
    text_password1=Label(text="Введите ваш пароль: ")
    registr_password1=Entry()
    text_password2=Label(text="Ещё раз пароль: ")
    registr_password2=Entry(show="*")
    button_registr=Button(text='Зарегестрироваться!',command=lambda:save())
    
    text.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()
    button_enter=Button(text='Войти')
    
    def save():
        if registr_password1.get() == registr_password2.get():
            f=open("login.txt","rb")
            oneStr = f.readline()
            f.close()
            if len(oneStr) != 0:
                f=open("login.txt","rb")
                a=pickle.load(f)#загружаем из нашего файла
                f.close()
                if registr_login.get() not in a:
                    login_password_save={}#Создаем словарь
                    login_password_save[registr_login.get()]=registr_password1.get()
                    login_password_save['quantityWin'] = 0
                    login_password_save['quantityLose'] = 0
                    login_password_save['finishedGame'] = 1
                    login_password_save['currentGame'] = 0
                    login_password_save['currentGameLevel'] = 0
                    login_password_save['mines'] = {}
                    login_password_save['viewed'] = {}
                    temp = {}
                    temp[registr_login.get()] = login_password_save
                    people.update(temp)
                    f=open('login.txt',"wb")#текстовый документ
                    pickle.dump(people,f)#сохраняем наш введенный логин в текст
                    f.close()
                    register = True
                    levelWindow1.destroy()
                    login(0)
                else:
                    messagebox.showerror(message = 'Такий користувач вже є.')
            else:
                login_password_save={}#Создаем словарь
                login_password_save[registr_login.get()]=registr_password1.get()
                login_password_save['quantityWin'] = 0
                login_password_save['quantityLose'] = 0
                login_password_save['currentGame'] = 0
                login_password_save['currentGameLevel'] = 0
                login_password_save['mines'] = {}
                login_password_save['viewed'] = {}
                temp = {}
                temp[registr_login.get()] = login_password_save
                people.update(temp)
                f=open('login.txt',"wb")#текстовый документ
                pickle.dump(people,f)#сохраняем наш введенный логин в текст
                f.close()
                register = True
                levelWindow1.destroy()
                login(0)
        else:
            messagebox.showerror(message = 'Паролі не співпадають.')

def login(a):
    if a != 0:
        root.destroy()
    levelWindow1=Tk()
    levelWindow1.geometry('300x500')
    levelWindow1.title('Войти')
    
    text_login=Label(text="Поздравляем!")
    text_enter_login=Label(text='Введите ваш Логин: ')
    enter_login=Entry()
    text_enter_password=Label(text="Введите ваш пароль: ")
    enter_password=Entry(show="*")
    button_enter=Button(text="Войти",command=lambda:log_pass())
    
    text_login.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack() 

    def log_pass():
        f=open("login.txt","rb")
        oneStr = f.readline()
        f.close()
        if len(oneStr) != 0:
            f=open("login.txt","rb")
            a=pickle.load(f)#загружаем из нашего файла
            f.close()
            if enter_login.get() in a:# если наш логин соответствует тому что мы зарегестривовали
                currentGame = a[enter_login.get()]['currentGame']
                global person
                person = enter_login.get()
                if enter_password.get()==a[enter_login.get()][enter_login.get()]:#если пароль соответствует с именем в нашем загруженом файле
                    levelWindow1.destroy()
                    if currentGame == 1:
                        levelWin(-1)
                    else:
                        levelWin(0)
                else:
                    messagebox.showerror(message = 'Невірний пароль')
            else:
                messagebox.showerror(message = 'Такого користувача не має')
        else:
            messagebox.showerror(message = 'Такого користувача не має')

                    
def levelWin(a):
    def Game(save,level):
        class cell(object):#создаем класс для отрисовки поля, элемент класса - одна клеточка
            foundMines = 0
            foundCells = 0
            def __init__(self,height,width):
                self.button = Button(text = '   ', background="grey", height="1", width="2")
                self.mine = False #Переменная наличия мины в поле
                self.value = 0 #Кол-во мин вокруг
                self.viewed = False #Открыто/закрыто поле
                self.flag = 0 #0 - флага нет, 1 - флаг стоит, 2 - стоит "?"
                self.around = [] #Массив, содержащий координаты соседних клеток
                self.clr = 'black' #Цвет текста
                self.row = height #Строка
                self.column = width  #Столбец
                    
            def leftClick(self,event):
                if mines == []: #При первом нажатии
                    seter(0,self.row,self.column)
                if self.viewed == False and self.flag == 0:
                    self.viewed = True
                    cell.foundCells+=1
                    global person
                    labelQuantityCells.config(text = height*width-cell.foundCells - quantityMines)
                    if self.value == 0:
                        self.button.config(text = ' ', bg = 'lightgrey')
                    else:
                        self.button.config(text = self.value, bg = 'lightgrey')
                    if self.mine == True:
                        self.button.config(text = ' ', bg = 'Red')
                        messagebox.showinfo('Вы проиграли!')
                        f=open("login.txt","rb")
                        temp=pickle.load(f)#загружаем из нашего файла
                        temp[person]['quantityLose'] += 1
                        temp[person]['currentGame'] = 0
                        f.close()
                        f=open("login.txt","wb")
                        del people[person]
                        people.update(temp)
                        pickle.dump(people,f)
                        f.close()
                        gameWindow.destroy()
                        levelWin(0)
                    elif cell.foundCells == height*width-quantityMines:
                        messagebox.showinfo('Победа!')
                        f=open("login.txt","rb")
                        temp=pickle.load(f)#загружаем из нашего файла
                        temp[person]['quantityWin'] += 1
                        temp[person]['currentGame'] = 0
                        f.close()
                        f=open("login.txt","wb")
                        del people[person]
                        people.update(temp)
                        pickle.dump(people,f)
                        f.close()
                        gameWindow.destroy()
                        levelWin(0)
                    if self.value == 0:
                        for k in self.around:
                            cells[k[0]][k[1]].leftClick('<Button-1>')

            def saveLeftClick(self):
                    if self.value == 0:
                        self.button.config(text = ' ', bg = 'lightgrey')
                    else:
                        self.button.config(text = self.value, bg = 'lightgrey')
                    if self.value == 0:
                        for k in self.around:
                            cells[k[0]][k[1]].leftClick('<Button-1>')

            def rightClick(self,event):
                if self.viewed == False:
                    if self.flag == 2:
                        self.button.config(text = ' ')
                        self.flag = 0
                        cell.foundMines-=1
                        labelQuantityMines.config(text = quantityMines-cell.foundMines)
                    elif self.flag == 1:
                        self.button.config(text = '!')
                        self.flag = 2
                        cell.foundMines+=1
                        labelQuantityMines.config(text = quantityMines-cell.foundMines)
                    else:
                        self.button.config(text = '?')
                        self.flag = 1
                 
        def aroundMine(x,y): #x y координаты мины
            if x-1 >= 0:
                cells[x-1][y].value+=1
            if x-1 >= 0 and y-1 >= 0:
                cells[x-1][y-1].value+=1
            if x-1 >= 0 and y+1 <= height-1:
                cells[x-1][y+1].value+=1
            if y-1 >= 0:
                cells[x][y-1].value+=1
            if y+1 <= height-1:
                cells[x][y+1].value+=1
            if x+1 <= width-1:
                cells[x+1][y].value+=1
            if x+1 <= width-1 and y+1 <= height-1:
                cells[x+1][y+1].value+=1
            if x+1 <= width-1 and y-1 >= 0:
                cells[x+1][y-1].value+=1

        def seter(quantityNow,row,column):
            if quantityNow != quantityMines:
                randRow = random.randint(0,height-1)    #выбираем рандомно места мин
                randColumn = random.randint(0,width-1)
                if [randColumn,randRow] not in mines and [randColumn,randRow] != [column,row]:
                    #проверяем есть ли у нас уже мина в этом месте и не сюда ли мы нажали в первый раз
                    cells[randColumn][randRow].mine = True      #ставим мину меняя значение поля
                    mines.append([randColumn,randRow])   #добавляем мину в массив мин
                    aroundMine(randColumn,randRow)# вызываем функцию для определения количества мин вокруг каждой клеточки вокруг нашей мины
                    seter(quantityNow+1,row,column) #Вызываем установщик, сказав, что одна мина уже есть
                else:
                    seter(quantityNow,row,column) #Вызываем установщик еще раз     
            
        def saveExit():
            viewedCells = []
            for i in range(height):
                for j in range(width):
                    if cells[j][i].viewed == True:
                        viewedCells.append([j,i])
            f=open("login.txt","rb")
            temp=pickle.load(f)#загружаем из нашего файла
            temp[person]['currentGame'] = 1
            temp[person]['mines'] = mines
            temp[person]['viewed'] = viewedCells
            temp[person]['currentGameLevel'] = level
            f.close()
            f=open("login.txt","wb")
            del people[person]
            people.update(temp)
            pickle.dump(people,f)
            f.close()
            gameWindow.destroy()
            sys.exit()

        def setAround(x,y):
            if x-1 >= 0:
                cells[x][y].around.append([x-1,y])
            if x-1 >= 0 and y-1 >= 0:
                cells[x][y].around.append([x-1,y-1])
            if x-1 >= 0 and y+1 <= height-1:
                cells[x][y].around.append([x-1,y+1])
            if y-1 >= 0:
                cells[x][y].around.append([x,y-1])
            if y+1 <= height-1:
                cells[x][y].around.append([x,y+1])
            if x+1 <= width-1:
                cells[x][y].around.append([x+1,y])
            if x+1 <= width-1 and y+1 <= height-1:
                cells[x][y].around.append([x+1,y+1])
            if x+1 <= width-1 and y-1 >= 0:
                cells[x][y].around.append([x+1,y-1])
        
        mines = []
        viewedcell = []
        if save>-1:
            levelWindow.destroy()
            if level == 0:
                quantityMines = 10
                height = 9
                width = 9
                gameWindow=Tk()# окно программы
                gameWindow.title('Гра Сапер')# Название окна
                gameWindow.geometry('420x270')
            if level == 1:
                quantityMines = 40
                height = 16
                width = 16
                gameWindow=Tk()# окно программы
                gameWindow.title('Гра Сапер')# Название окна
                gameWindow.geometry('630x480')
            if level == 2:
                quantityMines = 90
                height = 16
                width = 30
                gameWindow=Tk()# окно программы
                gameWindow.title('Гра Сапер')# Название окна
                gameWindow.geometry('1050x480')
        else:
            if level == 0:
                quantityMines = 10
                height = 9
                width = 9
                gameWindow=Tk()# окно программы
                gameWindow.title('Гра Сапер')# Название окна
                gameWindow.geometry('420x270')
                mines = temp[person]['mines']
                viewedcell = temp[person]['viewed']
            if level == 1:
                quantityMines = 40
                height = 16
                width = 16
                gameWindow=Tk()# окно программы
                gameWindow.title('Гра Сапер')# Название окна
                gameWindow.geometry('630x480')
                mines = temp[person]['mines']
                viewedcell = temp[person]['viewed']
            if level == 2:
                quantityMines = 90
                height = 16
                width = 30
                gameWindow=Tk()# окно программы
                gameWindow.title('Гра Сапер')# Название окна
                gameWindow.geometry('1050x480')
                mines = temp[person]['mines']
                viewedcell = temp[person]['viewed']
            f=open("login.txt","wb")
            del people[person]
            #temp[person]['currentGame'] = 0
            people.update(temp)
            pickle.dump(people,f)
            f.close()

        cells = [[cell(i,j) for i in range(height)] for j in range(width)]
  
        labelMines = Label(text = "Осталось мин: ")
        labelQuantityMines = Label(text = quantityMines-cell.foundMines)

        labelMines1 = Label(text = "Осталось открыть ячеек: ")
        labelQuantityCells = Label(text = height*width - cell.foundCells - quantityMines)

        for i in range(height):
            for j in range(width):
                if [j,i] in mines:
                    cells[j][i].mine = True
                    aroundMine(j,i)
                    
        for i in range(height):
            for j in range(width):
                cells[j][i].button.grid(row=i, column=j, ipadx=1, ipady=1, padx=1, pady=1)
                cells[j][i].button.bind('<Button-1>', cells[j][i].leftClick) #Биндим открывание клетки
                cells[j][i].button.bind('<Button-3>', cells[j][i].rightClick) #Установка флажка
                setAround(j,i)
                if [j,i] in viewedcell:
                    cells[j][i].saveLeftClick()

        if level == 0:
            labelMines.place(x=260, y=0)
            labelQuantityMines.place(x=260, y=15)
            labelMines1.place(x=260, y=50)
            labelQuantityCells.place(x=260, y=65)
            saveExitButton = Button(height="2", width="15",bg='#0021de', text = 'зберігти \nта вийти', command=lambda: saveExit())
            saveExitButton.place(x=260, y=95)
        if level == 1:
            labelMines.place(x=460, y=0)
            labelQuantityMines.place(x=460, y=15)
            labelMines1.place(x=460, y=50)
            labelQuantityCells.place(x=460, y=65)
            saveExitButton = Button(height="2", width="15",bg='#0021de', text = 'зберігти \nта вийти', command=lambda: saveExit())
            saveExitButton.place(x=460, y=95)
        if level == 2:
            labelMines.place(x=850, y=0)
            labelQuantityMines.place(x=850, y=15)
            labelMines1.place(x=850, y=50)
            labelQuantityCells.place(x=850, y=65)
            saveExitButton = Button(height="2", width="15",bg='#0021de',text='Зберігти\nі вийти', command=lambda: saveExit())
            saveExitButton.place(x=850, y=95)
        gameWindow.mainloop()
        
    if a < 0:
        f=open("login.txt","rb")
        temp=pickle.load(f)
        level = temp[person]['currentGameLevel']
        f.close()
        Game(a,level)
    else:
        levelWindow=Tk()
        levelWindow.geometry('200x160')
        levelWindow.title('Уровень')

        tabs = ttk.Notebook(levelWindow)
        
        tabLevel = ttk.Frame(tabs)
        tabStatistic = ttk.Frame(tabs)

        tabs.add(tabLevel, text='Выбор сложности')
        tabs.add(tabStatistic, text='Статистика')
        
        button1_enter=Button(tabLevel,text='НОВАЧОК\n9x9, мин: 10', height="2", width="15",bg='Green',command=lambda:Game(0,0))
        button2_enter=Button(tabLevel,text='ЛЮБИТЕЛЬ\n16x16, мин: 40',height="2", width="15",bg='Yellow',command=lambda:Game(0,1))
        button3_enter=Button(tabLevel,text='ПРОФЕСІОНАЛ\n16х30, мин: 90',height="2", width="15",bg='Red',command=lambda:Game(0,2))

        button1_enter.grid(column=0,row=0)
        button2_enter.grid(column=0,row=1)
        button3_enter.grid(column=0,row=2)

        quantityWinLabel = Label(tabStatistic, font = '15', text = 'Кількість перемог:')
        quantityWinLabel.grid(column=0,row=0)
        numberWinLabel = Label(tabStatistic, font = '15',text = people[person]['quantityWin'])
        numberWinLabel.grid(column=1,row=0)
        quantityLoseLabel = Label(tabStatistic, font = '15',text = 'Кількість поразок:')
        quantityLoseLabel.grid(column=0,row=1)
        numberLoseLabel = Label(tabStatistic, font = '15',text = people[person]['quantityLose'])
        numberLoseLabel.grid(column=1,row=1)

        tabs.pack()

root=Tk()
root.geometry('200x200')
root.title('Войти')
person = ' '
people = {}
f=open("login.txt","rb")
oneStr = f.readline()
f.close()
if len(oneStr) != 0:
    f=open("login.txt","rb")
    people=pickle.load(f)#загружаем из нашего файла
    f.close()
choise()
root.mainloop()
