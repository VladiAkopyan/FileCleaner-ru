import customtkinter as ctk
from customtkinter import CTkOptionMenu, CTkLabel, CTkEntry, CTkButton, CTkTextbox
from CTkMessagebox import CTkMessagebox
from types_files import types
from work_folder import replaceFile


class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('700x500')
        self.title("FileCleaner")
        self.resizable(False, False)

        # Заголовок FileCleaner
        CTkLabel(self, text='FileCleaner', font=("San Francisco", 30, 'bold')).grid(column=0, row=0, sticky="ew", pady=30)

        # Ввод путей к папкам
        self.folder_in = CTkEntry(self, placeholder_text="Путь исходной папки", width=270, font=("San Francisco", 14, 'bold'))
        self.folder_in.grid(column=0, row=1, padx=10)

        self.folder_out = CTkEntry(self, placeholder_text="Путь конечной папки", width=270, font=("San Francisco", 14, 'bold'))
        self.folder_out.grid(column=0, row=2)

        # Меню для выбора типа и расширения файлов
        self.types_menu = CTkOptionMenu(self, values=['Документы и текст', 'Видео', 'Изображения', 'Музыка'], command=self.choice, width=250, font=("San Francisco", 14, 'bold'))
        self.types_menu.grid(column=1, row=1, padx=25, pady=30)
        self.types_menu.set("Выберите тип файла")

        self.expansion = CTkOptionMenu(self, values=[],width=250, font=("San Francisco", 14, 'bold'))
        self.expansion.grid(column=1, row=2, padx=25)
        self.expansion.set('Выберите расширение файла')

        # Кнопка запуска выполнения функционала программы
        self.start_button = CTkButton(self, text='Запуск программы', command=self.startProgramm, font=("San Francisco", 14, 'bold'))
        self.start_button.grid(column=0, row=3, pady=30)

        # Окошко с выводом
        self.log_textbox = CTkTextbox(self, width=300, height=150, font=("San Francisco", 14, 'bold'))
        self.log_textbox.grid(column=0, row=4, pady=30, padx=30)

    def choice(self, _value):
        match _value:
            case "Документы и текст":
                self.expansion.configure(values=types['Документы и текст'])
            case "Видео":
                self.expansion.configure(values=types['Видео'])
            case "Изображения":
                self.expansion.configure(values=types['Изображения'])
            case "Музыка":
                self.expansion.configure(values=types['Музыка'])

    def startProgramm(self):
        if self.expansion.get() == 'Выберите расширение файла':
            self.messageWindow('Ошибка', 'Вы не выбрали расширение файла', 'warning')
        if not self.folder_in.get():
            self.messageWindow('Ошибка', 'Вы не указали исходную папку', 'warning')
        if not self.folder_out.get():
            self.messageWindow('Ошибка', 'Вы не указали конечную папку', 'warning')
        else:
            self.warningWindowForStartProgram()
            answer_user = self.warningWindowForStartProgram().get()
            if answer_user == 'Согласен':
                replaceFile(self.log_message, self.folder_in.get(), self.folder_out.get(), self.types_menu.get(), self.expansion.get())
            if answer_user == 'Нет':
                self.warningWindowForStartProgram().destroy()

    def warningWindowForStartProgram(self):
        return CTkMessagebox(title='Внимание', message='После того как вы согласитесь, все файлы с выбранным вами расширением будут удалены из начальной папки и будут перемещены в другую (выбранную вами). Вы соглашаетесь на это?', icon='warning', option_2='Согласен', option_1='Нет')

    def messageWindow(self, _title, _message, _icon):
        return CTkMessagebox(title=_title, message=_message, icon=_icon)

    def log_message(self, msg):
        self.log_textbox.insert('end', msg + "\n")
        self.log_textbox.see('end')
        self.update()