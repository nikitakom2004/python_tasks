"""reg_auth_form_komiagin.py: Программа регистрации и аутентификации пользователей."""

__author__      = "Никита Комягин"
__copyright__   = "(с) 2024 РАНХиГС"

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json

root = Tk()
root.geometry('280x150')
root.title('Войти в систему')
root.resizable(False, False)

# список зарегистриванных пользователей
user_settings = []

# ф-я для загрузки данных пользователей из файла
def load_settings():
    # читаем файл с данными пользователей в json формате
    try:
        with open('user_settings.json', 'r') as openfile:
            global user_settings
            user_settings = json.load(openfile)
            return True
    except OSError:
        return False

# ф-я аутентификации пользователя по логину и паролю
def auth(login, password):
    global user_settings
    for user in user_settings:
        if user.get('login') == login and user.get('pwd') == password:
            return True # логин и пароль совпали - проверка пройдена

    # проверка не пройдена
    return False

# ф-я регистрации нового пользователя в системе
def add_user(user):
    # проверяем, что такого пользователя нет в списке зарегистрированных по логину
    for u in user_settings:
        if u.get('login') == user.get('login'):
            return False

    # добавляем нового пользователя в список зарегистрированных пользователей
    user_settings.append(user)

    # пишем обновленный список пользователей в файл в json формате
    try:
        with open('user_settings.json', "w") as outfile:
            outfile.write(json.dumps(user_settings))
    except OSError:
        return False

    return True

# ф-я проверки сложности пароля
def check_pwd_complexity(passwd):

    special = ['$', '@', '#', '%', '!']

    if len(passwd) < 6:
        messagebox.showerror('Регистрация', 'Длина пароля должна быть минимум 6 символов')
        return False

    if not any(char.isdigit() for char in passwd):
        messagebox.showerror('Регистрация', 'Пароль должен содержать хотя бы одну цифру')
        return False

    if not any(char.isupper() for char in passwd):
        messagebox.showerror('Регистрация', 'Пароль должен содержать хотя бы одну заглавную букву')
        return False

    if not any(char.islower() for char in passwd):
        messagebox.showerror('Регистрация', 'Пароль должен содержать хотя бы одну строчную букву')
        return False

    if not any(char in special for char in passwd):
        messagebox.showerror('Регистрация', 'Пароль должен содержать хотя бы один специальный символ ' + str(special))
        return False

    return True

# ф-я реализует окно логина
def login_form():
    # создаем элементы графического интерфейса
    text_enter_login = Label(text='Логин:')
    enter_login = Entry()

    text_enter_pass = Label(text='Пароль:')
    enter_password = Entry(show='*')

    button_login = Button(text='Войти', command=lambda: login(), width=15)

    button_reg = Button(text='Регистрация', command=lambda: registration_form(), width=15)

    # выравниваем элементы графического интерфейса по сетке
    text_enter_login.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    enter_login.grid(row=0, column=1, padx=10, pady=10)

    text_enter_pass.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    enter_password.grid(row=1, column=1, padx=10, pady=10)

    button_login.grid(row=2, column=0, padx=10, pady=10)
    button_reg.grid(row=2, column=1, padx=10, pady=10)

    # ф-я реализует окно регистрации нового пользователя
    def registration_form():
        # создаем новое модальное окно для регистрации
        root_admin = Toplevel()
        root_admin.grab_set()
        root_admin.title("Форма регистрации")
        root_admin.wm_geometry('300x500')
        root_admin.resizable(False, False)

        # создаем элементы графического интерфейса
        text_name = Label(root_admin, text='Имя:')
        registr_name = Entry(root_admin)

        text_middle_name = Label(root_admin, text='Отчество:')
        registr_middle_name = Entry(root_admin)

        text_last_name = Label(root_admin, text='Фамилия:')
        registr_last_name = Entry(root_admin)

        text_gender = Label(root_admin, text='Пол:')
        gender_cb = Combobox(root_admin, values=["муж", "жен"], state='readonly')
        gender_cb.current(0)

        text_email = Label(root_admin, text='email:')
        registr_email = Entry(root_admin)

        text_phone = Label(root_admin, text='Телефон:')
        registr_phone = Entry(root_admin)

        text_log = Label(root_admin, text='Логин:')
        registr_login = Entry(root_admin)

        text_password1 = Label(root_admin, text='Пароль:')
        registr_password1 = Entry(root_admin, show='*')

        text_password2 = Label(root_admin, text='Повторите пароль:')
        registr_password2 = Entry(root_admin, show='*')

        button_registr = Button(root_admin, text='Зарегистрироваться', command=lambda: validate_and_register(), width=30)

        check_btn = Checkbutton(root_admin, text="Согласие на обработку персональных данных")

        # выравниваем элементы графического интерфейса по сетке
        text_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        registr_name.grid(row=0, column=1, padx=10, pady=10)

        text_middle_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        registr_middle_name.grid(row=1, column=1, padx=10, pady=10)

        text_last_name.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        registr_last_name.grid(row=2, column=1, padx=10, pady=10)

        text_gender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        gender_cb.grid(row=3, column=1, padx=10, pady=10)

        text_email.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        registr_email.grid(row=4, column=1, padx=10, pady=10)

        text_phone.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        registr_phone.grid(row=5, column=1, padx=10, pady=10)

        text_log.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        registr_login.grid(row=6, column=1, padx=10, pady=10)

        text_password1.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        registr_password1.grid(row=7, column=1, padx=10, pady=10)

        text_password2.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        registr_password2.grid(row=8, column=1, padx=10, pady=10)

        check_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
        button_registr.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

        # ф-я для проверки и сохранения данных регистрации нового пользователя
        def validate_and_register():
            # проверяем введенные данные
            if 'selected' not in check_btn.state():
                messagebox.showerror('Регистрация', 'Для продолжение регистрации необходимо принять уловия обработки персональных данных')
                return

            name = registr_name.get()
            if not name:
                messagebox.showerror('Регистрация', 'Имя не заполнено')
                return

            last_name = registr_last_name.get()
            if not last_name:
                messagebox.showerror('Регистрация', 'Фамилия не заполнена')
                return

            middle_name = registr_middle_name.get()
            gender = gender_cb.get()
            phone = registr_phone.get()
            email = registr_email.get()
            if not email:
                messagebox.showerror('Регистрация', 'email не указан')
                return

            login = registr_login.get()
            if not login:
                messagebox.showerror('Регистрация', 'Логин не может быть пустым')
                return

            pass1 = registr_password1.get()
            if not check_pwd_complexity(pass1):
                return

            pass2 = registr_password2.get()
            if pass1 != pass2:
                messagebox.showerror('Регистрация', 'Пароли не совпадают')
                return

            # формируем словарь с данными полльзователя
            user_data = {}
            user_data['name'] = name
            user_data['middle_name'] = middle_name
            user_data['last_name'] = last_name
            user_data['gender'] = gender
            user_data['phone'] = phone
            user_data['email'] = email
            user_data['login'] = login
            user_data['pwd'] = pass1

            # вызываем ф-ю для добавление нового пользователя в список зарегистрированных
            if not add_user(user_data):
                messagebox.showerror('Регистрация', 'Пользователь с указанным логином уже зарегистирован в системе')
                return

            messagebox.showinfo('Регистрация', 'Пользователь успешно зарегистрирован')

            # закрываем окно регистрации
            root_admin.destroy()

    # ф-я для аутентификации пользователя по логину и паролю
    def login():
        # проверяем, что пользователь ввел логин
        user_login = enter_login.get()
        if not user_login:
            messagebox.showerror('Логин', 'Неверный логин или пароль')
            return

        if not auth(user_login, enter_password.get()):
            messagebox.showerror('Логин', 'Неверный логин или пароль')
            return

        messagebox.showinfo('Логин', 'Вход выполнен')

# загружаем данные пользователя из файла
load_settings()

# открываем начальную форму логина
login_form()

# запускаем основной цикл обработки событий графического интерфейса пользователя
root.mainloop()
