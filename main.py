# подключение библиотек
from datetime import datetime
from tkinter import *
from tkinter import ttk
import sqlite3 as db
from sqlite3 import Error
from tkinter import messagebox
import random

# окно админа
def Admin():
    # 1-я функция админа
    def registration():
        # отправка запроса
        def registration_sql():
            def send_sql():
                sql_insert = f"INSERT OR IGNORE INTO users(name,login,password,role) VALUES('{name}','{login}','{password}','{role}');"
                result = sqls.insert_sql(sql_insert)
                messagebox.showinfo(title="Успешно!", message="Вы успешно добавили!",parent= thirdwindow)
                thirdwindow.destroy()
                
            def default():
                messagebox.showerror(title="Ошибка!", message="Неправильно написали роль. Попробуйте еще раз!",parent= thirdwindow)
                
            name = name_entry_reg.get()
            login = login_entry_reg.get()
            password = password_entry_reg.get()
            role = role_cmb_reg.get()
            if name != "":
                if login != "" and password != "":
                    sql_roles = "SELECT DISTINCT role FROM users;"
                    result = sqls.select_sql(sql_roles)
                    roles = []
                    for i in result:
                        roles.append(i[0])
                    if role != "" and role in roles:
                        # пробовал синтаксис похожий на switch/case
                        switch = {
                        "admin": send_sql,
                        "chef": send_sql,
                        "waiter": send_sql
                        }
                        switch.get(role,default)()
                    else:
                        messagebox.showerror(title="Ошибка!", message="Пустое поле Роль, либо такой роли нет",parent= thirdwindow)
                else:
                        messagebox.showerror(title="Ошибка!", message="Пустое поле Логин и Пароль",parent= thirdwindow)
            else:
                messagebox.showerror(title="Ошибка!", message="Пустое поле Имя",parent= thirdwindow)
            
        thirdwindow = Tk()
        thirdwindow.title("Регистрация новых пользователей")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        
        btn_exit_reg = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        name_lable_reg = Label(thirdwindow,text='Имя пользователя',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        name_entry_reg = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 20')
        login_lable_reg = Label(thirdwindow,text='Логин пользователя',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        login_entry_reg = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 20')
        password_label_reg  = Label(thirdwindow,text='Пароль пользователя',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        password_entry_reg  = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 20')
        role_label_reg  = Label(thirdwindow,text='Роль пользователя (admin|waiter|chef)',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        sql_roles = "SELECT DISTINCT role FROM users;"
        result = sqls.select_sql(sql_roles)
        roles = []
        for i in result:
            roles.append(i[0])
        role_cmb_reg  = ttk.Combobox(thirdwindow,values=roles,state="readonly",font='Arial 20')
        btn_reg = Button(thirdwindow,text='Зарегистрировать', command=registration_sql,font='Arial 15 bold')
        
        for c in range(2): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(6): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_reg.grid(row=0,column=0, columnspan=2,sticky=NSEW)
        name_lable_reg.grid(row=1,column=0)
        login_lable_reg.grid(row=2,column=0)
        password_label_reg.grid(row=3,column=0)
        role_label_reg.grid(row=4,column=0)
        name_entry_reg.grid(row=1,column=1,sticky=EW)
        login_entry_reg.grid(row=2,column=1,sticky=EW)
        password_entry_reg.grid(row=3,column=1,sticky=EW)
        role_cmb_reg.grid(row=4,column=1,sticky=EW)
        btn_reg.grid(row=5,column=0,columnspan=2,sticky=NSEW)

        thirdwindow.mainloop()
    # 2-я функция админа
    def dismissal():
        def fire():
            login = login_entry_dism.get()
            if login != "":
                sql_update = f'UPDATE OR IGNORE users SET status = "Уволен" WHERE login = "{login}";'
                sqls.update_sql(sql_update)
                messagebox.showinfo(title="Успешно!",message=f"Статус у {login} был сменен на Уволен",parent=thirdwindow)
                thirdwindow.destroy()
            else:
                messagebox.showerror(title="Ошибка!",message="Пустое поле Логин",parent=thirdwindow)
        
        def returnuser():
            login = login_entry_dism.get()
            if login != "":
                sql_update = f'UPDATE OR IGNORE users SET status = "Работает" WHERE login = "{login}";'
                sqls.update_sql(sql_update)
                messagebox.showinfo(title="Успешно!",message=f"Статус у {login} был сменен на Работает",parent=thirdwindow)
                thirdwindow.destroy()
            else:
                messagebox.showerror(title="Ошибка!",message="Пустое поле Логин",parent=thirdwindow)
        
        thirdwindow = Tk()
        thirdwindow.title("Увольнение сотрудников")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        # подгрузка данных из бд
        sql_select = f"SELECT name,login,status FROM users;"
        users = sqls.select_sql(sql_select)
        
        columns = ("name","login","status")
        btn_exit_dism = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        login_lable_dism = Label(thirdwindow,text='Логин пользователя',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        login_entry_dism = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 20')
        btn_dism = Button(thirdwindow,text='Уволить',font='Arial 15 bold',command=fire)
        btn_rtn = Button(thirdwindow,text='Вернуть в должность',font='Arial 15 bold',command=returnuser)
        tree = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree.heading("name", text="Имя")
        tree.heading("login",text="Логин")
        tree.heading("status",text="Статус")
        for user in users:
            tree.insert("",END,values=user)
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
            
        for c in range(3): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(4): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_dism.grid(row=0,column=0, columnspan=4,sticky=NSEW)
        login_lable_dism.grid(row=1,column=0,sticky=NSEW)
        login_entry_dism.grid(row=1,column=1,columnspan=3,sticky=EW)
        btn_dism.grid(row=2,column=0,columnspan=2,sticky=NSEW)
        btn_rtn.grid(row=2,column=2,columnspan=2,sticky=NSEW)
        tree.grid(row=3,column=0,columnspan=3,sticky=NSEW)
        scrollbar.grid(row=3,column=3,sticky=NSEW)
        
        thirdwindow.mainloop()
    
    # 3 и 4-я функция
    def manage_shift():
        def create_shift():
            tables_id = random.randint(0,100000000)
            workers = workers_entry.get()
            table1 = table1_entry.get()
            table2 = table2_entry.get()
            table3 = table3_entry.get()
            table4 = table4_entry.get()
            table5 = table5_entry.get()
            table6 = table6_entry.get()
            if workers != "":
                if table1!="" and table2!="":
                    if table3!="" and table4!="":
                        if table5!="" and table6!="":
                            sql_insert_tables = f"INSERT OR IGNORE INTO tables VALUES({tables_id},'{table1}','{table2}','{table3}','{table4}','{table5}','{table6}');"
                            sql_insert_shift = f"INSERT OR IGNORE INTO shifts(datestart,datefinish,workers,tables_id) VALUES(datetime('now','localtime'),datetime('now','localtime','+10 hours'),'{workers}',{tables_id});"
                            sqls.insert_sql(sql_insert_tables)
                            sqls.insert_sql(sql_insert_shift)
                            messagebox.showinfo(title="Успешно!",message=f"Вы открыли смену!",parent=thirdwindow)
                            thirdwindow.destroy()
                        else:
                            messagebox.showerror(title="Ошибка!",message="Пустое поле Стол 5 и Стол 6",parent=thirdwindow)
                    else:
                            messagebox.showerror(title="Ошибка!",message="Пустое поле Стол 3 и Стол 4",parent=thirdwindow)
                else:
                            messagebox.showerror(title="Ошибка!",message="Пустое поле Стол 1 и Стол 2",parent=thirdwindow)
            else:
                messagebox.showerror(title="Ошибка!",message="Пустое поле Работники",parent=thirdwindow)
        
        thirdwindow = Tk()
        thirdwindow.title("Открытие смены")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        
        # подгрузка данных из бд
        sql_select_users = f"SELECT name,role,status FROM users WHERE role <> 'admin' AND status <> 'Уволен';"
        list_users = sqls.select_sql(sql_select_users)
        sql_select_shifts = f"SELECT datestart,datefinish,workers,tables_id FROM shifts;"
        list_shifts = sqls.select_sql(sql_select_shifts)
        sql_select_tables = f"SELECT * FROM tables;"
        list_tables = sqls.select_sql(sql_select_tables)
        sql_select_waiters = "SELECT name FROM users WHERE role='waiter' AND status <> 'Уволен';"
        sql_result_waiters = sqls.select_sql(sql_select_waiters)
        waiters=[]
        for i in sql_result_waiters:
            waiters.append(i[0])

        btn_exit_shift = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        workers_lable = Label(thirdwindow,text='Работники',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        workers_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 15')
        table1_lable = Label(thirdwindow,text='Стол 1',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table1_entry = ttk.Combobox(thirdwindow, font='Arial 15',values=waiters,state="readonly")
        table2_lable = Label(thirdwindow,text='Стол 2',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table2_entry = ttk.Combobox(thirdwindow, font='Arial 15',values=waiters,state="readonly")
        table3_lable = Label(thirdwindow,text='Стол 3',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table3_entry = ttk.Combobox(thirdwindow, font='Arial 15',values=waiters,state="readonly")
        table4_lable = Label(thirdwindow,text='Стол 4',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table4_entry = ttk.Combobox(thirdwindow, font='Arial 15',values=waiters,state="readonly")
        table5_lable = Label(thirdwindow,text='Стол 5',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table5_entry = ttk.Combobox(thirdwindow, font='Arial 15',values=waiters,state="readonly")
        table6_lable = Label(thirdwindow,text='Стол 6',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table6_entry = ttk.Combobox(thirdwindow, font='Arial 15',values=waiters,state="readonly")
        btn_shifts = Button(thirdwindow,text='Создать',font='Arial 15 bold',command=create_shift)
        columns1 = ("name","role","status")
        tree1 = ttk.Treeview(thirdwindow,columns=columns1,show="headings")
        tree1.heading("name", text="Имя")
        tree1.heading("role",text="Роль")
        tree1.heading("status",text="Статус")
        for user in list_users:
            tree1.insert("",END,values=user)
        scrollbar1 = Scrollbar(thirdwindow,orient=VERTICAL,command=tree1.yview)
        tree1.configure(yscrollcommand=scrollbar1.set)
        columns2 = ("datestart","datefinish","workers","tables_id")
        tree2 = ttk.Treeview(thirdwindow,columns=columns2,show="headings")
        tree2.heading("datestart", text="Начало смены")
        tree2.heading("datefinish",text="Конец смены")
        tree2.heading("workers",text="Работники")
        tree2.heading("tables_id",text="Id распорядка")
        if list_shifts != None:
            for shift in list_shifts:
                tree2.insert("",END,values=shift)
        scrollbar2 = Scrollbar(thirdwindow,orient=VERTICAL,command=tree2.yview)
        tree2.configure(yscrollcommand=scrollbar2.set)
        columns3 = ("id","table1","table2","table3","table4","table5","table6")
        tree3 = ttk.Treeview(thirdwindow,columns=columns3,show="headings")
        tree3.heading("id", text="Id")
        tree3.heading("table1", text="Стол 1")
        tree3.heading("table2", text="Стол 2")
        tree3.heading("table3", text="Стол 3")
        tree3.heading("table4", text="Стол 4")
        tree3.heading("table5", text="Стол 5")
        tree3.heading("table6", text="Стол 6")
        if list_tables != None:
            for table in list_tables:
                tree3.insert("",END,values=table)
        scrollbar3 = Scrollbar(thirdwindow,orient=VERTICAL,command=tree3.yview)
        tree3.configure(yscrollcommand=scrollbar3.set)
        
            
        for c in range(3): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(11): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_shift.grid(row=0,column=0, columnspan=4,sticky=NSEW)
        workers_lable.grid(row=1,column=0,sticky=EW)
        workers_entry.grid(row=1,column=1,sticky=EW)
        table1_lable.grid(row=2,column=0,sticky=EW)
        table1_entry.grid(row=2,column=1,sticky=EW)
        table2_lable.grid(row=3,column=0,sticky=EW)
        table2_entry.grid(row=3,column=1,sticky=EW)
        table3_lable.grid(row=4,column=0,sticky=EW)
        table3_entry.grid(row=4,column=1,sticky=EW)
        table4_lable.grid(row=5,column=0,sticky=EW)
        table4_entry.grid(row=5,column=1,sticky=EW)
        table5_lable.grid(row=6,column=0,sticky=EW)
        table5_entry.grid(row=6,column=1,sticky=EW)
        table6_lable.grid(row=7,column=0,sticky=EW)
        table6_entry.grid(row=7,column=1,sticky=EW)
        btn_shifts.grid(row=8,column=0,columnspan=4,sticky=NSEW)
        tree1.grid(row=9,column=0,columnspan=3,sticky=NSEW)
        scrollbar1.grid(row=9,column=3,sticky=NSEW)
        tree2.grid(row=10,column=0,columnspan=3,sticky=NSEW)
        scrollbar2.grid(row=10,column=3,sticky=NSEW)
        tree3.grid(row=11,column=0,columnspan=3,sticky=NSEW)
        scrollbar3.grid(row=11,column=3,sticky=NSEW)
        
        thirdwindow.mainloop()
    
    # 5-я функция
    def all_orders():
        thirdwindow = Tk()
        thirdwindow.title("Открытие смены")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        
        # подгрузка данных из бд
        sql_select_orders = "SELECT * FROM orders;"
        sql_result_orders = sqls.select_sql(sql_select_orders)
        list_orders=[]
        for i in sql_result_orders:
            list_orders.append(i)

        btn_exit_shift = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        columns = ("id","waiter_id","shift_id", "status", "table_number", "price", "dishes")
        tree = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree.heading("id", text="Номер заказа")
        tree.heading("waiter_id",text="Номер официанта")
        tree.heading("shift_id",text="Номер смены")
        tree.heading("status",text="Статус")
        tree.heading("table_number",text="Стол")
        tree.heading("price",text="Цена")
        tree.heading("dishes",text="Блюда")
        for order in list_orders:
            tree.insert("",END,values=order)
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        for c in range(1): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(2): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_shift.grid(row=0,column=0,columnspan=2,sticky=NSEW)
        tree.grid(row=1,column=0,sticky=NSEW)
        scrollbar.grid(row=1,column=1,sticky=NS)
        
        
        thirdwindow.mainloop()
    
    #6-я функция
    def change_order():
        thirdwindow = Tk()
        thirdwindow.title("Редактирование неоплаченных заказов")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        
        # подгрузка данных из бд
        sql_select_orders = "SELECT * FROM orders WHERE status <> 'Оплачен';"
        sql_result_orders = sqls.select_sql(sql_select_orders)
        list_orders=[]
        for i in sql_result_orders:
            list_orders.append(i)

        def item_select(event):
            waiter_id_entry.delete(0,END)
            shift_id_entry.delete(0,END)
            status_entry.delete(0,END)
            table_number_entry.delete(0,END)
            price_entry.delete(0,END)
            dishes_entry.delete(0,END)
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                order = item["values"]
                order_id_label["text"] = f"{order[0]}"
                waiter_id_entry.insert(0,f"{order[1]}")
                shift_id_entry.insert(0,f"{order[2]}")
                status_entry.insert(0,f"{order[3]}")
                table_number_entry.insert(0,f"{order[4]}")
                price_entry.insert(0,f"{order[5]}")
                dishes_entry.insert(0,f"{order[6]}")
        
        def change():
            sql_update_order = f"UPDATE OR IGNORE orders SET waiter_id = '{waiter_id_entry.get()}', shift_id = '{shift_id_entry.get()}', status = '{status_entry.get()}', table_number = '{table_number_entry.get()}', price = '{price_entry.get()}', dishes = '{dishes_entry.get()}' WHERE id = {order_id_label['text']};"
            sqls.update_sql(sql_update_order)
            messagebox.showinfo(title="Успешно!",message=f"Вы успешно изменили заказ №{order_id_label['text']}",parent=thirdwindow)
            thirdwindow.destroy()

        btn_exit_shift = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        order_id_label = Label(thirdwindow,font='Arial 15 bold',bg='#FF8CDF',fg='white')
        waiter_id_label = Label(thirdwindow,text="Номер официанта",font='Arial 15 bold',bg='#FF8CDF',fg='white')
        waiter_id_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 15')
        shift_id_label = Label(thirdwindow,text="Номер смены",font='Arial 15 bold',bg='#FF8CDF',fg='white')
        shift_id_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 15')
        status_label = Label(thirdwindow,text="Статус",font='Arial 15 bold',bg='#FF8CDF',fg='white')
        status_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 15')
        table_number_label = Label(thirdwindow,text="Номер стола",font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table_number_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 15')
        price_label = Label(thirdwindow,text="Цена заказа",font='Arial 15 bold',bg='#FF8CDF',fg='white')
        price_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 15')
        dishes_label = Label(thirdwindow,text="Блюда",font='Arial 15 bold',bg='#FF8CDF',fg='white')
        dishes_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 15')
        btn_change_order = Button(thirdwindow,text='Изменить',font='Arial 15 bold',command=change)
        columns = ("id","waiter_id","shift_id", "status", "table_number", "price", "dishes")
        tree = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree.heading("id", text="Номер заказа")
        tree.heading("waiter_id",text="Номер официанта")
        tree.heading("shift_id",text="Номер смены")
        tree.heading("status",text="Статус")
        tree.heading("table_number",text="Стол")
        tree.heading("price",text="Цена")
        tree.heading("dishes",text="Блюда")
        for order in list_orders:
            tree.insert("",END,values=order)
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        for c in range(2): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(9): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_shift.grid(row=0,column=0,columnspan=4,sticky=NSEW)
        order_id_label.grid(row=1,column=0,columnspan=2,sticky=EW)
        waiter_id_label.grid(row=2,column=0,sticky=NSEW)
        waiter_id_entry.grid(row=2,column=1,sticky=EW)
        shift_id_label.grid(row=3,column=0,sticky=NSEW)
        shift_id_entry.grid(row=3,column=1,sticky=EW)
        status_label.grid(row=4,column=0,sticky=NSEW)
        status_entry.grid(row=4,column=1,sticky=EW)
        table_number_label.grid(row=5,column=0,sticky=NSEW)
        table_number_entry.grid(row=5,column=1,sticky=EW)
        price_label.grid(row=6,column=0,sticky=NSEW)
        price_entry.grid(row=6,column=1,sticky=EW)
        dishes_label.grid(row=7,column=0,sticky=NSEW)
        dishes_entry.grid(row=7,column=1,sticky=EW)
        btn_change_order.grid(row=8,column=0,columnspan=4,sticky=NSEW)
        tree.grid(row=9,column=0,columnspan=2,sticky=NSEW)
        scrollbar.grid(row=9,column=3,sticky=NS)
        tree.bind("<<TreeviewSelect>>", item_select)
        
        thirdwindow.mainloop()
    
    #7-я функция
    def report_orders():
        sql_select_all_orders = f"SELECT * FROM orders;"
        result = sqls.select_sql(sql_select_all_orders)
        file = open(f"report_about_orders_{random.randint(0,100000000)}.txt","a+")
        file.write(f"Отчет о заказах №{random.randint(0,100000000)} от {datetime.now()} \n")
        for string in result:
            text = f"{string}"
            file.write(f"{text} \n")
        file.close()
        messagebox.showinfo(title="Успешно!",message="Успешно создан файл!", parent=secondwindow)
    
    #8-я функция
    def report_payment():
        sql_select_all_orders = f"SELECT * FROM orders WHERE status = 'Оплачен';"
        result = sqls.select_sql(sql_select_all_orders)
        file = open(f"report_payment_{random.randint(0,100000000)}.txt","a+")
        file.write(f"Отчет об оплаченных заказах №{random.randint(0,100000000)} от {datetime.now()} \n")
        for string in result:
            text = f"{string}"
            file.write(f"{text} \n")
        file.close()
        messagebox.showinfo(title="Успешно!",message="Успешно создан файл!", parent=secondwindow)
    
    # настройка окна админа  
    secondwindow = Tk()
    secondwindow.title("Меню админа")
    w = "1920"
    h = "1080"
    secondwindow.geometry(f"{w}x{h}")
    secondwindow.attributes('-fullscreen', True)
    secondwindow.attributes('-topmost', True)
    secondwindow.configure(bg='#FF8CDF')

    btn_exit = Button(secondwindow,text='Выход', command=secondwindow.destroy,font='Arial 15 bold')
    btn_reg = Button(secondwindow,text='Регистрация новых пользователей', command=registration,font='Arial 15 bold')
    btn_dis = Button(secondwindow,text='Увольнение пользователей', command=dismissal,font='Arial 15 bold')
    btn_shift = Button(secondwindow,text='Открыть смену',font='Arial 15 bold', command=manage_shift)
    btn_orders = Button(secondwindow,text='Просмотр всех заказов',font='Arial 15 bold', command=all_orders)
    btn_change_orders = Button(secondwindow,text='Изменение неоплаченных заказов',font='Arial 15 bold', command=change_order)
    btn_report_orders = Button(secondwindow,text="Создать отчет о заказах",font='Arial 15 bold',command=report_orders)
    btn_report_payment_orders = Button(secondwindow,text="Создать отчет об оплаченных заказах",font='Arial 15 bold',command=report_payment)
    
    for c in range(1): secondwindow.columnconfigure(index=c, weight=1)
    for r in range(8): secondwindow.rowconfigure(index=r, weight=1)
    
    btn_exit.grid(row=0,column=0,sticky=NSEW)
    btn_reg.grid(row=1,column=0,sticky=NSEW)
    btn_dis.grid(row=2,column=0,sticky=NSEW)
    btn_shift.grid(row=3,column=0,sticky=NSEW)
    btn_orders.grid(row=4,column=0,sticky=NSEW)
    btn_change_orders.grid(row=5,column=0,sticky=NSEW)
    btn_report_orders.grid(row=6,column=0,sticky=NSEW)
    btn_report_payment_orders.grid(row=7,column=0,sticky=NSEW)
    
    secondwindow.mainloop()

# окно повара
def Chef():
    def orders():
        def take_order():
            order_number = order_number_entry.get()
            if order_number != "":
                sql_update = f'UPDATE OR IGNORE orders SET status = "Готовится" WHERE id = "{order_number}";'
                sqls.update_sql(sql_update)
                messagebox.showinfo(title="Успешно!",message=f"Статус у заказа {order_number} был сменен",parent=thirdwindow)
                thirdwindow.destroy()
            else:
                messagebox.showerror(title="Ошибка!",message="Пустое поле Номер заказа",parent=thirdwindow)
        
        def give_order():
            order_number = order_number_entry.get()
            if order_number != "":
                sql_update = f'UPDATE OR IGNORE orders SET status = "Готово" WHERE id = "{order_number}";'
                sqls.update_sql(sql_update)
                messagebox.showinfo(title="Успешно!",message=f"Статус у заказа {order_number} был сменен",parent=thirdwindow)
                thirdwindow.destroy()
            else:
                messagebox.showerror(title="Ошибка!",message="Пустое поле Номер заказа",parent=thirdwindow)
        
        thirdwindow = Tk()
        thirdwindow.title("Заказы")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        # подгрузка данных из бд
        sql_select = f"SELECT * FROM orders;"
        orders = sqls.select_sql(sql_select)
        columns = ("id","dishes","table_number","status")
        btn_exit_dism = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        order_number_lable = Label(thirdwindow,text='Номер заказа',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        order_number_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 20')
        btn_take_order = Button(thirdwindow,text='Взять',font='Arial 15 bold',command=take_order)
        btn_give_order = Button(thirdwindow,text='Отдать',font='Arial 15 bold',command=give_order)
        tree = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree.heading("id", text="Номер заказа")
        tree.heading("dishes",text="Блюда")
        tree.heading("table_number",text="Номер стола")
        tree.heading("status",text="Статус")
        for order in orders:
            tree.insert("",END,values=order)
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
            
        for c in range(3): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(4): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_dism.grid(row=0,column=0, columnspan=4,sticky=NSEW)
        order_number_lable.grid(row=1,column=0,sticky=NSEW)
        order_number_entry.grid(row=1,column=1,columnspan=3,sticky=EW)
        btn_take_order.grid(row=2,column=0,columnspan=2,sticky=NSEW)
        btn_give_order.grid(row=2,column=2,columnspan=2,sticky=NSEW)
        tree.grid(row=3,column=0,columnspan=3,sticky=NSEW)
        scrollbar.grid(row=3,column=3,sticky=NSEW)
        
        thirdwindow.mainloop()
        
    secondwindow = Tk()
    secondwindow.title("Меню повара")
    w = "1920"
    h = "1080"
    secondwindow.geometry(f"{w}x{h}")
    secondwindow.attributes('-fullscreen', True)
    secondwindow.attributes('-topmost', True)
    secondwindow.configure(bg='#FF8CDF')
    
    btn_exit = Button(secondwindow,text='Выход', command=secondwindow.destroy,font='Arial 15 bold')
    btn_orders = Button(secondwindow,text='Заказы', command=orders,font='Arial 15 bold')
    
    for c in range(1): secondwindow.columnconfigure(index=c, weight=1)
    for r in range(2): secondwindow.rowconfigure(index=r, weight=1)
    
    btn_exit.grid(row=0,column=0,sticky=NSEW)
    btn_orders.grid(row=1,column=0,sticky=NSEW)
    
    secondwindow.mainloop()

# окно официанта
def Waiter():
    # 1-я функция
    def create_order():
        orders_id = random.randint(0,100000000)
        waiter_name = name_entry.get()
        sql_find_id = f"SELECT id FROM users WHERE login == '{waiter_name}';"
        sql_waiter_id = sqls.select_sql(sql_find_id)
        waiter_id = sql_waiter_id[0][0]
        sql_find_shift_id = f"SELECT id FROM shifts WHERE datetime(datestart) < datetime('now','localtime') AND datetime('now','localtime') < datetime(datefinish);"
        sql_shift_id = sqls.select_sql(sql_find_shift_id)
        shift_id = sql_shift_id[0][0]
        sql_inser_order = f"INSERT OR IGNORE INTO orders(id,waiter_id,shift_id) VALUES({orders_id},{waiter_id},{shift_id});"
        sqls.insert_sql(sql_inser_order)
        list_dishes = []
        
        def add_dish():
            dish = dishes_combo.get()
            if dish != '':
                list_dishes.append(dish)
                tree_order.insert("",END,values=dish)
                price = 0
                text = ""
                for i in list_dishes:
                    price = price + float(i.split(' ')[1])
                for i in list_dishes:
                    text = f"{text} {i.split(' ')[0]}"
                price1_entry.delete(0,END)
                price1_entry.insert(0,f"{price}")
                sql_update_order = f'UPDATE OR IGNORE orders SET table_number = {table_combo.get()}, price = {price}, dishes = "{text}" WHERE id = {orders_id};'
                sqls.update_sql(sql_update_order)
             
        thirdwindow = Tk()
        thirdwindow.title("Создание заказа")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        tables = [1,2,3,4,5,6]
        sql_select_dishes = "SELECT name,price FROM dishes;"
        result = sqls.select_sql(sql_select_dishes)
        dishes = []
        for i in result:
            dishes.append(i)
        columns=("dish","price")
        btn_exit_menu = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        table_lable = Label(thirdwindow,text='Стол №',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        table_combo = ttk.Combobox(thirdwindow, font='Arial 15',values=tables,state="readonly")
        dishes_lable = Label(thirdwindow,text='Выберете блюдо',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        dishes_combo = ttk.Combobox(thirdwindow, font='Arial 15',values=dishes,state="readonly")
        tree_order = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree_order.heading("dish", text="Блюдо")
        tree_order.heading("price",text="Цена") 
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree_order.yview)
        tree_order.configure(yscrollcommand=scrollbar.set)
        btn_accept = Button(thirdwindow,text='Добавить в список', command=add_dish,font='Arial 15 bold')
        price_label = Label(thirdwindow,text='Цена:',font='Arial 15 bold',bg='#FF8CDF',fg='white')
        price1_entry = Entry(thirdwindow,font='Arial 15 bold',bg='#FF8CDF',fg='white')
            
        for c in range(4): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(6): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_menu.grid(row=0,column=0, columnspan=5,sticky=NSEW)
        table_lable.grid(row=1,column=0,sticky=EW)
        table_combo.grid(row=1,column=1,columnspan=4,sticky=EW)
        dishes_lable.grid(row=2,column=0,sticky=EW)
        dishes_combo.grid(row=2,column=1,columnspan=2, sticky=EW)
        btn_accept.grid(row=2,column=3,columnspan=2,sticky=NSEW)
        tree_order.grid(row=3,column=0,columnspan=4,sticky=NSEW)
        scrollbar.grid(row=3,column=4,sticky=NS)
        price_label.grid(row=4,column=0,sticky=EW)
        price1_entry.grid(row=4,column=1,columnspan=4,sticky=EW)
        thirdwindow.mainloop()
    
    # 2-я функция
    def all_waiters_orders():
        thirdwindow = Tk()
        thirdwindow.title("Просмотр принятых заказов за смену")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        
        def update_orders():
            # подгрузка данных из бд
            waiter_name = name_entry.get()
            sql_find_id = f"SELECT id FROM users WHERE login == '{waiter_name}';"
            sql_waiter_id = sqls.select_sql(sql_find_id)
            waiter_id = sql_waiter_id[0][0]
            sql_find_shift_id = f"SELECT id FROM shifts WHERE datetime(datestart) < datetime('now','localtime') AND datetime('now','localtime') < datetime(datefinish);"
            sql_shift_id = sqls.select_sql(sql_find_shift_id)
            shift_id = sql_shift_id[0][0]
            if shift_id != None:
                sql_select_orders = f"SELECT id,shift_id,status,table_number,price,dishes FROM orders WHERE waiter_id = {waiter_id} AND shift_id = {shift_id};"
                sql_result_orders = sqls.select_sql(sql_select_orders)
                list_orders=[]
                for i in sql_result_orders:
                    list_orders.append(i)
                for order in list_orders:
                    tree.insert("",END,values=order)
            else:
                messagebox.showerror(title="Ошибка!",message="Сейчас нет открытой смены!",parent=thirdwindow)

        btn_exit_shift = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        btn_waiters_orders = Button(thirdwindow,text='Посмотреть', command=update_orders,font='Arial 15 bold')
        columns = ("id","shift_id", "status", "table_number", "price", "dishes")
        tree = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree.heading("id", text="Номер заказа")
        tree.heading("shift_id",text="Номер смены")
        tree.heading("status",text="Статус")
        tree.heading("table_number",text="Стол")
        tree.heading("price",text="Цена")
        tree.heading("dishes",text="Блюда")
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        for c in range(1): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(3): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_shift.grid(row=0,column=0,columnspan=2,sticky=NSEW)
        btn_waiters_orders.grid(row=1,column=0,columnspan=2,sticky=NSEW)
        tree.grid(row=2,column=0,sticky=NSEW)
        scrollbar.grid(row=2,column=1,sticky=NS)
        
        thirdwindow.mainloop()
    
    # 3-я функция
    def change_status():
        thirdwindow = Tk()
        thirdwindow.title("Увольнение сотрудников")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')
        
        def change():
            number_order = number_order_entry.get()
            if number_order != "":
                sql_update = f'UPDATE OR IGNORE orders SET status = "Оплачен" WHERE id = {number_order};'
                sqls.update_sql(sql_update)
                messagebox.showinfo(title="Успешно!",message=f"Статус у заказа №{number_order} был сменен.",parent=thirdwindow)
                thirdwindow.destroy()
            else:
                messagebox.showerror(title="Ошибка!",message="Пустое поле Номер заказа",parent=thirdwindow)
        
        btn_exit_change = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        number_order_lable = Label(thirdwindow,text='Номер заказа',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        number_order_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 20')
        btn_change = Button(thirdwindow,text='Изменить',font='Arial 15 bold',command=change)
        columns = ("id","shift_id", "status", "table_number", "price", "dishes")
        tree = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree.heading("id", text="Номер заказа")
        tree.heading("shift_id",text="Номер смены")
        tree.heading("status",text="Статус")
        tree.heading("table_number",text="Стол")
        tree.heading("price",text="Цена")
        tree.heading("dishes",text="Блюда")
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # подгрузка данных из бд
        waiter_name = name_entry.get()
        sql_find_id = f"SELECT id FROM users WHERE login == '{waiter_name}';"
        sql_waiter_id = sqls.select_sql(sql_find_id)
        waiter_id = sql_waiter_id[0][0]
        sql_find_shift_id = f"SELECT id FROM shifts WHERE datetime(datestart) < datetime('now','localtime') AND datetime('now','localtime') < datetime(datefinish);"
        sql_shift_id = sqls.select_sql(sql_find_shift_id)
        shift_id = sql_shift_id[0][0]
        if shift_id != None:
            sql_select_orders = f"SELECT id,shift_id,status,table_number,price,dishes FROM orders WHERE waiter_id = {waiter_id} AND shift_id = {shift_id};"
            sql_result_orders = sqls.select_sql(sql_select_orders)
            list_orders=[]
            for i in sql_result_orders:
                list_orders.append(i)
            for order in list_orders:
                 tree.insert("",END,values=order)
        else:
            messagebox.showerror(title="Ошибка!",message="Сейчас нет открытой смены!",parent=thirdwindow)

        for c in range(2): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(4): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_change.grid(row=0,column=0, columnspan=2,sticky=NSEW)
        number_order_lable.grid(row=1,column=0,sticky=NSEW)
        number_order_entry.grid(row=1,column=1,sticky=EW)
        btn_change.grid(row=2,column=0,columnspan=2,sticky=NSEW)
        tree.grid(row=3,column=0,columnspan=2,sticky=NSEW)
        scrollbar.grid(row=3,column=3,sticky=NSEW)
        
        thirdwindow.mainloop()
    
    #4-я функция
    def check():
        thirdwindow = Tk()
        thirdwindow.title("Увольнение сотрудников")
        w = "1920"
        h = "1080"
        thirdwindow.geometry(f"{w}x{h}")
        thirdwindow.attributes('-fullscreen', True)
        thirdwindow.attributes('-topmost', True)
        thirdwindow.configure(bg='#FF8CDF')  
        btn_exit_change = Button(thirdwindow,text='Вернуться в меню', command=thirdwindow.destroy,font='Arial 15 bold')
        number_order_lable = Label(thirdwindow,text='Номер заказа',font='Arial 20 bold',bg='#FF8CDF',fg='white')
        number_order_entry = Entry(thirdwindow, bg='#FF8CDF',fg='white',font='Arial 20')
        
        
        columns = ("id","dishes",  "table_number","price", "status")
        tree = ttk.Treeview(thirdwindow,columns=columns,show="headings")
        tree.heading("id", text="Номер заказа")
        tree.heading("dishes",text="Блюда")
        tree.heading("table_number",text="Стол")
        tree.heading("price",text="Цена")
        tree.heading("status",text="Статус")
        scrollbar = Scrollbar(thirdwindow,orient=VERTICAL,command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        sql_select_orders = f"SELECT id,dishes,table_number,price,status FROM orders WHERE status = 'Оплачен';"
        sql_result_orders = sqls.select_sql(sql_select_orders)
        list_orders=[]
        for i in sql_result_orders:
            list_orders.append(i)
        for order in list_orders:
            tree.insert("",END,values=order)
        def check_create():
            order_id = number_order_entry.get()
            if number_order_entry.get() != "":
                sql_select_all_orders = f"SELECT id,dishes,table_number,price FROM orders WHERE id = {order_id};"
                result = sqls.select_sql(sql_select_all_orders)
                file = open(f"check_{result[0][0]}.txt","a+")
                file.write(f"ПКО №{random.randint(0,100000000)} от {datetime.now()} \n")
                file.write(f"Номер заказа: {result[0][0]} \n")
                file.write(f"Блюда: {result[0][1]} \n")
                file.write(f"Номер стола: {result[0][2]} \n")
                file.write(f"Стоимость: {result[0][3]} \n")
                file.write("Способ оплаты: [] наличными | [] безналичными \n")
                file.close()
                messagebox.showinfo(title="Успешно!",message="Успешно создан файл!", parent=thirdwindow)
                thirdwindow.destroy()
            else:
                messagebox.showerror(title="Ошибка!",message="Пустое поле Номер заказа", parent=thirdwindow)
                
        btn_check = Button(thirdwindow,text='Создать чек',font='Arial 15 bold',command=check_create)        
        
        for c in range(2): thirdwindow.columnconfigure(index=c, weight=1)
        for r in range(4): thirdwindow.rowconfigure(index=r, weight=1)
        
        btn_exit_change.grid(row=0,column=0, columnspan=2,sticky=NSEW)
        number_order_lable.grid(row=1,column=0,sticky=NSEW)
        number_order_entry.grid(row=1,column=1,sticky=EW)
        btn_check.grid(row=2,column=0,columnspan=2,sticky=NSEW)
        tree.grid(row=3,column=0,columnspan=2,sticky=NSEW)
        scrollbar.grid(row=3,column=3,sticky=NSEW)
        
        thirdwindow.mainloop()
    
    def report_orders_shift():
        sql_select_all_orders = f"SELECT * FROM orders JOIN shifts ON shifts.id = orders.shift_id WHERE datetime(datestart) < datetime('now','localtime') AND datetime('now','localtime') < datetime(datefinish);"
        result = sqls.select_sql(sql_select_all_orders)
        file = open(f"waiters_report_about_orders_{random.randint(0,100000000)}.txt","a+")
        file.write(f"Отчет о заказах №{random.randint(0,100000000)} от {datetime.now()} \n")
        for string in result:
            text = f"{string}"
            file.write(f"{text} \n")
        file.close()
        messagebox.showinfo(title="Успешно!",message="Успешно создан файл!", parent=secondwindow)
    
    secondwindow = Tk()
    secondwindow.title("Меню официанта")
    w = "1920"
    h = "1080"
    secondwindow.geometry(f"{w}x{h}")
    secondwindow.attributes('-fullscreen', True)
    secondwindow.attributes('-topmost', True)
    secondwindow.configure(bg='#FF8CDF')
    
    btn_exit = Button(secondwindow,text='Выход', command=secondwindow.destroy,font='Arial 15 bold')
    btn_order = Button(secondwindow,text='Создание заказа', command=create_order,font='Arial 15 bold')
    btn_your_orders = Button(secondwindow,text='Просмотр всех принятых заказов за текущую смену', command=all_waiters_orders,font='Arial 15 bold')
    btn_change_status = Button(secondwindow,text='Изменение статуса заказам', command=change_status,font='Arial 15 bold')
    btn_check = Button(secondwindow,text='Создание ПКО', command=check,font='Arial 15 bold')
    btn_report= Button(secondwindow,text='Создание отчета за текущаю смену', command=report_orders_shift,font='Arial 15 bold')
    
    for c in range(1): secondwindow.columnconfigure(index=c, weight=1)
    for r in range(7): secondwindow.rowconfigure(index=r, weight=1)
    
    btn_exit.grid(row=0,column=0,sticky=NSEW)
    btn_order.grid(row=1,column=0,sticky=NSEW)
    btn_your_orders.grid(row=2,column=0,sticky=NSEW)
    btn_change_status.grid(row=3,column=0,sticky=NSEW)
    btn_check.grid(row=4,column=0,sticky=NSEW)
    btn_report.grid(row=5,column=0,sticky=NSEW)
    
    secondwindow.mainloop()

class sqls:
    # создание таблицы и добавление данных в бд
    def create_sql(sql_create):
        try:
            conn = db.connect("cafe.db",isolation_level=None)
            if conn is not None:
                c = conn.cursor()
                c.execute(sql_create)
                c.close()
            else:
                print("Ошибка: не удалось подключиться к базе.") 
        except Error as e:
            print(e)
            
    def insert_sql(sql_insert):
        try:
            conn = db.connect("cafe.db",isolation_level=None)
            if conn is not None:
                c = conn.cursor()
                result = c.execute(sql_insert).fetchall()
                c.close()
                return result
            else:
                print("Ошибка: не удалось подключиться к базе.")
        except Error as e:
            print(e)
        
    def select_sql(sql_select):
        try:
            conn = db.connect("cafe.db",isolation_level=None)
            if conn is not None:
                c = conn.cursor()
                result = c.execute(sql_select).fetchall()
                c.close()
                return result
            else:
                print("Ошибка: не удалось подключиться к базе.")
        except Error as e:
            print(e)
    def update_sql(sql_update):
        try:
            conn = db.connect("cafe.db",isolation_level=None)
            if conn is not None:
                c = conn.cursor()
                result = c.execute(sql_update)
                c.close()
            else:
                print("Ошибка: не удалось подключиться к базе.")
        except Error as e:
            print(e)

def main():
    # запросы для бд
    sql_create_users_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name text NOT NULL, login text NOT NULL,password text NOT NULL, role text NOT NULL, status text NOT NULL DEFAULT "Работает",UNIQUE(login));'
    sql_create_shifts_table = "CREATE TABLE IF NOT EXISTS shifts (id INTEGER PRIMARY KEY AUTOINCREMENT, datestart text NOT NULL, datefinish text NOT NULL, workers text NOT NULL, tables_id INTEGER, FOREIGN KEY (tables_id) REFERENCES tables (id));"
    sql_create_tables_table = "CREATE TABLE IF NOT EXISTS tables (id INTEGER PRIMARY KEY, table1 text NOT NULL, table2 text NOT NULL, table3 text NOT NULL, table4 text NOT NULL, table5 text NOT NULL, table6 text NOT NULL, UNIQUE(id));"
    sql_create_orders_table = 'CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, waiter_id INTEGER NOT NULL, shift_id INTEGER NOT NULL, status text NOT NULL DEFAULT "Принят", table_number INTEGER, price REAL, dishes text, FOREIGN KEY (shift_id) REFERENCES shifts (id), FOREIGN KEY (waiter_id) REFERENCES users (id));'
    sql_create_dishes_table = 'CREATE TABLE IF NOT EXISTS dishes (id INTEGER PRIMARY KEY AUTOINCREMENT, name text NOT NULL, price REAL NOT NULL, UNIQUE(name));'
    sql_insert_admin_user = 'INSERT OR IGNORE INTO users(name,login,password,role) VALUES("Коровин Н.В.","admin","admin","admin");'
    sql_insert_chef_user = 'INSERT OR IGNORE INTO users(name,login,password,role) VALUES("Коровина А.С.","chef","chef","chef");'
    sql_insert_waiter_user = 'INSERT OR IGNORE INTO users(name,login,password,role) VALUES("Коровин Е.В.","waiter","waiter","waiter");'
    sql_insert_dishes_water = 'INSERT OR IGNORE INTO dishes(name,price) VALUES("Вода",20.49);'
    sql_insert_dishes_cake = 'INSERT OR IGNORE INTO dishes(name,price) VALUES("Тортик",179.49);'
    sql_insert_dishes_tea = 'INSERT OR IGNORE INTO dishes(name,price) VALUES("Чай",15.99);'
    sql_insert_dishes_coffee = 'INSERT OR IGNORE INTO dishes(name,price) VALUES("Кофе",20.99);'
    
    # создание таблицы dictionary
    sqls.create_sql(sql_create_users_table)
    sqls.create_sql(sql_create_shifts_table)
    sqls.create_sql(sql_create_tables_table)
    sqls.create_sql(sql_create_orders_table)
    sqls.create_sql(sql_create_dishes_table)
    sqls.insert_sql(sql_insert_admin_user)
    sqls.insert_sql(sql_insert_chef_user)
    sqls.insert_sql(sql_insert_waiter_user)
    sqls.insert_sql(sql_insert_dishes_water)
    sqls.insert_sql(sql_insert_dishes_cake)
    sqls.insert_sql(sql_insert_dishes_tea)
    sqls.insert_sql(sql_insert_dishes_coffee)
    
if __name__ == '__main__':
    main()

# очистка и заполнение поля name_entry
def on_enter_name(e):
    text=name_entry.get()
    if text=='Username':
        name_entry.delete(0,END)
    else:
        return
def on_leave_name(e):
    text=name_entry.get()
    if text=='':
        name_entry.insert(0,'Username')   

# очистка и заполнение поля password_entry
def on_enter_pass(e):
    text=password_entry.get()
    if text=='Password':
        password_entry.delete(0,END)
    else:
        return
def on_leave_pass(e):
    text=password_entry.get()
    if text=='':
        password_entry.insert(0,'Password') 

# функция кнопки для авторизации
def click():
    username = name_entry.get()
    password = password_entry.get()
    if username != "Username" and password != "Password":
        sql_select_name_pass = f"SELECT * FROM users WHERE login='{username}' AND password='{password}';"
        result = sqls.select_sql(sql_select_name_pass)
        if result != []:
            tup = result[0]
            name = tup[2]
            passw = tup[3]
            role = tup[4]
            status = tup[5]
            if status=="Работает":
                if username==name and password==passw:
                    if role=="admin":
                        # открытие окна админа
                        Admin()
                    elif role=="chef":
                        # открытие окна повара
                        Chef()
                    elif role=="waiter":
                        # открытие окна официанта
                        Waiter()
            else:
                messagebox.showerror(title="Ошибка!",message="Вы были уволены!", parent=mainwindow)   
        else:
            messagebox.showerror(title="Ошибка!",message="Неверные данные", parent=mainwindow)
    else:
        messagebox.showerror(title="Ошибка!",message="Введите данные сначала", parent=mainwindow)
      
# создание начального окна
mainwindow = Tk()
mainwindow.title('Авторизация')
#str(thirdwindow.winfo_screenwidth()/int(2))[:-2]
#thirdwindow.winfo_screenheight()
w = "1920"
h = "1080"
mainwindow.geometry(f"{w}x{h}")
mainwindow.attributes('-fullscreen', True)
mainwindow.attributes('-topmost', True)
mainwindow.configure(bg='#FF8CDF')

# содержимое окна
name_lable = Label(mainwindow,text='Логин',font='Arial 20 bold',bg='#FF8CDF',fg='white')
name_entry = Entry(mainwindow, bg='#FF8CDF',fg='white',font='Arial 20')
name_entry.insert(0,'Username')
name_entry.bind('<FocusIn>',on_enter_name)
name_entry.bind('<FocusOut>',on_leave_name)
password_label = Label(mainwindow,text='Пароль',font='Arial 20 bold',bg='#FF8CDF',fg='white')
password_entry = Entry(mainwindow, bg='#FF8CDF',fg='white',font='Arial 20',show='*')
password_entry.insert(0,'Password')
password_entry.bind('<FocusIn>',on_enter_pass)
password_entry.bind('<FocusOut>',on_leave_pass)

# кнопка входа      
login_btn = Button(mainwindow,text='Войти',height=10, command=click, cursor='hand2',font='Arial 15 bold')
btn_exit = Button(mainwindow,text='Закрыть приложение',height=10, command=mainwindow.destroy,cursor='hand2',font='Arial 15 bold')
# расположение по колонками и строкам
for c in range(2): mainwindow.columnconfigure(index=c, weight=1)
for r in range(4): mainwindow.rowconfigure(index=r, weight=1)

name_lable.grid(row=0,column=0,sticky=NSEW)
password_label.grid(row=1,column=0,sticky=NSEW)
name_entry.grid(row=0,column=1,sticky=EW)
password_entry.grid(row=1,column=1,sticky=EW)
login_btn.grid(row=2,column=0,columnspan=2,sticky=NSEW)
btn_exit.grid(row=3,column=0,columnspan=2,sticky=NSEW)

# запуск окна
mainwindow.mainloop()