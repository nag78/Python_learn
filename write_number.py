import json

num = input("Ваше любимое число? ")
filename = 'f_number.json'
with open(filename, 'w') as f_obj:
    json.dump(num,f_obj)