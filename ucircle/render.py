import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Leitura da entrada
print('Insira um valor em graus (0-360):')
degrees_input = float(input())
radians = degrees_input * math.pi / 180

def render():
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor('#ffffff')

    circle = Circle((0, 0), 1, facecolor=('k', 0), edgecolor='k',
                    linestyle='solid', linewidth=0.5)

    xmin, xmax, ymin, ymax = -3, 3, -3, 3
    ticks_frequency = 1

    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
    ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)

    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)

    ax.set_xticks(x_ticks[x_ticks[x_ticks != 0]])
    ax.set_yticks(y_ticks[y_ticks[y_ticks != 0]])
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    ax.add_patch(circle)

    sin_x = np.arange(-3, 3*np.pi, 0.1)
    sin_y = np.sin(sin_x)
    plt.plot(sin_x, sin_y, color=('green', 0.5), linewidth=1)

    cos_x = np.arange(-3, 3*np.pi, 0.1)
    cos_y = np.cos(cos_x)
    plt.plot(cos_x, cos_y, color=('purple', 0.5))

    ax1, ay1 = [-2, 2], [2, -2]
    ax2, ay2 = [2, -2], [2, -2]
    plt.plot(ax1, ay1, ax2, ay2, linestyle='dotted', color=('k', 0.35))

    plt.text(2, 2, r"$45°$", fontsize=10, color=('k', 0.35))
    plt.text(2, -2, r"$315°$", fontsize=10, color=('k', 0.35))
    plt.text(-2, -2, r"$225°$", fontsize=10, color=('k', 0.35),
             horizontalalignment='right')
    plt.text(-2, 2, r"$135°$", fontsize=10, color=('k', 0.35),
             horizontalalignment='right')

    plt.text(0, 3, r"$90°$", fontsize=10, color=('k', 0.35))
    plt.text(0, -4, r"$270°$", fontsize=10, color=('k', 0.35))
    plt.text(-4, 0, r"$180°$", fontsize=10, color=('k', 0.35),
             horizontalalignment='center')
    plt.text(3, 0, r"$360°$", fontsize=10, color=('k', 0.35),
             horizontalalignment='center')

    def get_circle_coordinates(radians):
        x = math.cos(radians)
        y = math.sin(radians)
        return (x, y)

    px, py = get_circle_coordinates(radians)
    plt.plot(px, py, 'ro')
    plt.text(px+0.3, py, "P", fontsize=10, color=('r', 0.75), horizontalalignment='center')

    plt.plot(0, math.sin(radians), 'o', color='green')
    plt.plot(math.cos(radians), 0, 'o', color='purple')

    tp1 = [px,py]
    tp2 = [math.cos(radians),0]

    tp3 = [px,py]
    tp4 = [0,math.sin(radians)]

    tp5 = [px,py]
    tp6 = [0,0]

    x_values = [tp1[0], tp3[0],tp2[0], tp4[0], tp5[0], tp6[0]]
    y_values = [tp1[1], tp3[1],tp2[1], tp4[1], tp5[1], tp6[1]]

    plt.plot(x_values, y_values, '--', color=('k', 0.5), linewidth=0.5)

    plt.text(-3, -3, "Entrada: {} ({} rad)"
             .format(degrees_input, round(radians, 2)),
             fontsize=10, color=('k', 1), horizontalalignment='left')
    plt.text(-3, -3.5, "P = ({}, {})".format(round(px, 2), round(py, 2)),
             fontsize=10, color=('r', 1), horizontalalignment='left')
    plt.text(-3, -4, "sen = {}".format(round(math.sin(radians), 2)),
             fontsize=10, color=('green', 1), horizontalalignment='left')
    plt.text(-3, -4.5, "cos(x) = {}".format(round(math.cos(radians), 2)),
             fontsize=10, color=('purple', 1), horizontalalignment='left')

    plt.show()
