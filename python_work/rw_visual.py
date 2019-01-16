import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    rw = RandomWalk()
    rw.fill_walk()  
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s = 15, c = point_numbers, cmap = plt.cm.Blues,
                edgecolors='none')
    # Выделение первой и последней точек.
    plt.scatter(0, 0, c = 'green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
