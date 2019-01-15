import matplotlib.pyplot as plt


x_values = list(range(1, 5001))
y_values = [y**3 for y in x_values]

plt.scatter(x_values, y_values, c = y_values)

plt.show()