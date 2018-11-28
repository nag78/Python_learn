guest_name = ''
filename = 'guests_book.txt'
prompt = "Введите свое имя, Гость: "
prompt += "\nВведите q чтобы выйти"
with open(filename, 'a') as file_object:
    while True:
        guest_name = input(prompt)
        if guest_name == 'q':
            break
        file_object.write(guest_name.title() + "\n")

