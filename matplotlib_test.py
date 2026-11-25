"""
Author: Dietrich Geisler
Last Modified: 10/25/2025

A script to check that matplotlib was installed correctly
"""

import matplotlib.pyplot as plt
import math

def main():
    """
    A simple demonstration of using matplotlib to display a graph
    """

    # Modified from https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html
    x_values = []
    y_values = []
    for x in range(0, 200):
        x_values.append(x / 100)
        y_values.append(1 + math.sin(2 * math.pi * (x / 100)))
        
    fig, ax = plt.subplots()
    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Matplotlib Demo')

    ax.plot(x_values, y_values)
    plt.show()
    
if __name__ == "__main__":
    main()