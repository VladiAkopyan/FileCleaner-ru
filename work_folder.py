from pathlib import Path
import shutil
import types_files as tf

def FindFileFromFolder(_folder_in, _folder_type):
    for file in Path(_folder_in).rglob(_folder_type):
        print(file)

def ReplaceFile(_folder_in, _folder_out, _type_file):
    folder_in = Path(_folder_in)
    folder_out = Path(_folder_out)

    folder_out.mkdir(parents=True, exist_ok=True)

    for expansion in tf.types[_type_file]:
        for file in folder_in.rglob(expansion):
            try:
                shutil.move(str(file), str(folder_out / file.name))
                print(f"✅ Перемещён: {file.name}")
            except PermissionError:
                print("⚠️ Не перемещено (занят другим процессом)")
            except OSError as e:
                print(f"⚠️ Системная ошибка: {e}")