import work_folder as wf
import types_files as tf
import sys

print("Добро пожаловать в консольное приложение по распределению файлов с определенными расширениями по нужным папкам")
print("К примеру: все файлы с расширениями .png .jpg .webr будут отправлены в папку Pictures/Изображение")
print('\n')
while True:
    folder_in = input("Введите сюда путь папки, из которой будут доставаться нужные файлы: ")
    folder_out = input("Введите сюда путь папки, в которую будут добавляться нужные файлы: ")
    print('1 - Текст')
    print('2 - Видео')
    print('3 - Фото')
    print("4 - Музыка")
    while True:
        type_file = int(input("Введите номер типа файла: "))
        if tf.types.get(str(type_file)):
            break
        print("Такого номера не существует. Проверьте и попробуйте еще раз.")
    try:
        print("ВНИМАНИЕ! После отправки, все файлы, которые были перемещены в другую папку, они будут удалены в начальной папке (в которой были изначально)")
        answer = int(input("Выберите (согласны - 1, не согласны - 0): "))
        match answer:
            case 1:
                wf.ReplaceFile(folder_in, folder_out, str(type_file))
            case 0:
                sys.exit(0)
    except ValueError:
        print("Вы ввели не номер файла, а что-то другое ;)")