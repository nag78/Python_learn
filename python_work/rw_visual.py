import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s = 15, c = rw.y_values)
plt.show()