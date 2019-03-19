#! python3
# bulletPointAdder.py - Добавляет маркеры Википедии в начало
# каждой строки текста, сохраненного в буфере обмена.

import pyperclip 
text = pyperclip.paste()

# Разделяет строки и добавляет звездочки.
lines = text.split('\n')
for i in range(len(lines)):         # Цикл по списку "lines"
    lines[i] = '* ' + lines[i]      # добавляет звездочку в каждую
                                    # строку в списке "lines"
text = '\n'.join(lines)

pyperclip.copy(text)