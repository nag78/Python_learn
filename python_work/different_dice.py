from die import Die
import pygal


# Создание кубиков D6 и D10
die_1 = Die()
die_2 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(50000):
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

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = [x for x in range(2, max_result + 1)]
# hist.x_labels = "Result"
hist.y_labels = frequencies

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_visual.svg')
hist.render_in_browser()
