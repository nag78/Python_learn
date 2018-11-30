import json

file = 'f_number.json'
prompt = "Enter your favorite number. "
num = input(prompt)
with open(file, 'w') as f_obj:
    print(num)
    json.dump(num,file)