from die import Die
import matplotlib.pyplot as plt


# Кубики D8 2шт
die_1 = Die(10)
die_2 = Die()


# Моделирование бросков
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

for value in range(2, die_1.num_sides+die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация
max_x = die_1.num_sides + die_2.num_sides + 1
x_values = [x for x in range(2, max_x)]
y_values = frequencies

# plt.plot(x_values, y_values)
plt.scatter(x_values, y_values)
plt.show()
