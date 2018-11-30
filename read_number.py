import json

filename = 'f_number.json'
with open(filename) as f_obj:
    num = json.load(f_obj)
print("Ваше любимое число: " + num)