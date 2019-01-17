import pygal
from die import Die


# Создние 2-х кубиков D6.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                 '10', '11', '12', 'Result']
# hist.x_labels = "Result"
hist.y_labels = frequencies

hist.add('D6', frequencies)
hist.render_in_browser()
