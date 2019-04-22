# Исходная таблица.
tableData = [
             ['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
            ]


def printTable(table):
    cols = len(table)                                # Количество столбцов
    rows = len(table[0])                             # Количество строк

    # Вычисление максимальной ширины столбца по самой длинной строке
    col_width = []
    for col in table:
        col_width.append(len(sorted(col, key=len)[-1]))

    # Заполнение результирующего списка и вывод результата со смещением вправо
    for row in range(rows):
        result = []
        for col in range(cols):
            result.append(table[col][row].rjust(col_width[col]))
        print('\t'.join(result))


printTable(tableData)
