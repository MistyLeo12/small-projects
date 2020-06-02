import matplotlib.pyplot as plt 
import numpy as np
import random
from matplotlib import animation


"""
Uses matplotlib to plot a random walk. This project was to help me practice matplotlib and refreshing myself markov chains

Information and reason for the project was used here:
https://en.wikipedia.org/wiki/Random_walk#:~:text=A%20random%20walk%20is%20a,space%20such%20as%20the%20integers.

Stay tuned, I will be trying to implement more complex Markov models in my next project!

"""

def randomWalk(steps, num_walks):
    x = np.zeros(steps)
    y = np.zeros(steps)

    for i in range(1, steps):
        random_val = random.randint(0, 7) #8 degrees of freedom in 2d graph
        if random_val is 0:
            x[i] = x[i-1] + 1 
            y[i] = y[i-1]
        elif random_val is 1:
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        elif random_val is 2:
            x[i] = x[i-1]
            y[i] = y[i-1] + 1
        elif random_val is 3:
            x[i] = x[i-1]
            y[i] = y[i-1] - 1
        elif random_val is 4:
            x[i] = x[i-1] + 1
            y[i] = y[i-1] + 1
        elif random_val is 5:
            x[i] = x[i-1] + 1
            y[i] = y[i-1] - 1
        elif random_val is 6:
            x[i] = x[i-1] - 1
            y[i] = y[i-1] + 1
        else:
            x[i] = x[i-1] - 1
            y[i] = y[i-1] - 1
    print(x)
    print(y)
    return x, y


plt.tight_layout(pad=0)


def visualize(steps, num_walks):
    color = ['blue', 'red', 'green', 'black', 'purple']
    for j in range(0, num_walks):
        x, y = randomWalk(steps, num_walks)
        plt.plot(x, y,'+', label= "Random walk", color=color[j])
    plt.axis([-10,10,-10,10])
    plt.title("2D Random Walk")
    plt.show()

visualize(10, 5)




