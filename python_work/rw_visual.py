import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    rw = RandomWalk()
    rw.fill_walk()  
    plt.scatter(rw.x_values, rw.y_values, s = 15, c = rw.y_values)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
