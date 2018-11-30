import json

filename = 'f_number.json'

def get_stored_number():
    """Возвращает сохраненное число"""
    try:
        with open(filename) as f_obj:
            num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return num

def get_new_number():
    """Запрашивает новое число"""
    num = input("Введите любимое число: ")
    with open(filename, 'w') as f_obj:
        json.dump(num,f_obj)
    return num

def greet_number():
    num = get_stored_number()
    if num:
        print("Ваше любимое число: " + num + "!")
    else:
        num = get_new_number()
        print("Мы запомнили! Ваше любимое число: " + num + "!")

greet_number()