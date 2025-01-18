import matplotlib.pyplot as plt
import numpy as np
import random
import math
from itertools import combinations

# Set up the figure and 1D axis
fig, axs = plt.subplots(3, 1, figsize=(8, 3))
# Randomly choose left or right for axis direction arrow
axis_direction = 1
n = len(axs)

for isetup in range(100):

    def clear_canvas():
        axs[0].cla()
        axs[1].cla()
        for i, ax in enumerate(axs):
            if i == n-1:
                ax.set_ylim(-1, 1)  # Constrain vertical space
                ax.set_xlim(-10, 10)  # Set axis limits for clarity
                ax.axis('off')
                continue
            ax.axhline(0, color='black', linewidth=0.8)  # Draw the x-axis
            ax.set_ylim(-1, 1)  # Constrain vertical space
            ax.set_xlim(-10, 10)  # Set axis limits for clarity
            ax.axis('off')
        
            arrow_x = -9.5 if axis_direction == -1 else 9.5  # Position of the arrow start
            ax.arrow(arrow_x, 0, axis_direction * 0.1, 0, head_width=0.2, head_length=0.4, fc='black', ec='black', width=0)
            axs[0].annotate('Initial', (-10, 1.0), color='black', fontsize=12, ha='center')
            axs[1].annotate('Final', (-10, 1.0), color='black', fontsize=12, ha='center')

    clear_canvas()

    s = round(random.uniform(5, 20)) * 0.2

    # Generate a random x0 point and arrow for the first axis
    x0 = round(random.uniform(-2, 2))
    v0_length = round(random.uniform(0, 5))  # Random arrow length
    v0_direction = random.choice([-1, 1])  # Random direction (+ or -)
    v0 = v0_direction * v0_length

    a = random.choice([-1, 1]) * round(random.uniform(-4, 4))
    t = round(random.uniform(1, 16)) * 0.5
    x = x0 + v0 * t + 0.5 * a * t**2
    v = v0 + a * t
    print("x0", x0, "x", x, "v0", v0, "v", v, "a", a, "t", t)
    while abs(x) + abs(v) > 9.5:
        a = random.choice([-1, 1]) * round(random.uniform(-4, 4))
        t = round(random.uniform(1, 16))
        x = x0 + v0 * t + 0.5 * a * t**2
        v = v0 + a * t
        print("x0", x0, "x", x, "v0", v0, "v", v, "a", a, "t", t)

    v_length = abs(v)
    v_direction = np.sign(v)

    def draw_x0():
        axs[0].plot(x0, 0.2, 'ro', label='$x_0$')  # Mark x0
        axs[0].annotate('$x_0$', (x0, 0.4), color='red', fontsize=10, ha='center')

    def draw_v0():
        # Plot x0 and the arrow on the first axis
        v0_end = x0 + v0
        if abs(v0) != 0:
            axs[0].arrow(x0, 0.2, v0, 0, head_width=0.2, head_length=0.4, fc='red', ec='red')
            axs[0].text((x0 + v0_end) / 2, 0.8, '$v_0$', color='red', fontsize=10, ha='center')
        else:
            axs[0].text((x0 + v0_end) / 2, 0.8, '$v_0 = 0$', color='red', fontsize=10, ha='center')

    def draw_x():
        # Plot x and the arrow on the second axis
        axs[1].plot(x, 0.2, 'bo', label='$x$')  # Mark x
        axs[1].annotate('$x$', (x, 0.4), color='blue', fontsize=10, ha='center')

    def draw_v():
        v_end = x + v
        if abs(v) != 0:
            axs[1].arrow(x, 0.2, v, 0, head_width=0.2, head_length=0.4, fc='blue', ec='blue')
            axs[1].text((x + v_end) / 2, 0.8, '$v$', color='blue', fontsize=10, ha='center')
        else:
            axs[1].text((x + v_end) / 2, 0.8, '$v=0$', color='blue', fontsize=10, ha='center')

    def draw_a():
        a_end = 3 + np.sign(a)
        if abs(a) != 0:
            axs[0].arrow(3, -0.4, a, 0, head_width=0.2, head_length=0.4, fc='green', ec='green')
            axs[0].text((3 + a_end) / 2, -0.8, '$a$', color='green', fontsize=10, ha='center')
        else:
            axs[0].text((3 + a_end) / 2, -0.8, '$a=0$', color='green', fontsize=10, ha='center')

    def draw_t():
        axs[0].text(8, -0.8, f'$t={t:.1f}$', color='black', fontsize=10, ha='center')

    texts = {
            "x0": f'$x_0$ = {x0*s:.2f} m'    , # 0
            "v0": f'$v_0$ = {v0*s:.2f} m/s'  , # 1
            "x": f'$x$ = {x*s:.2f} m'       , # 2
            "v": f'$v$ = {v*s:.2f} m/s'     , # 3
            "a": f'$a$ = {a*s:.2f} m/s$^2$' , # 4
            "t": f'$t$ = {t:.2f} s'       , # 5
            "d?": f'$x$ - $x_0$ = ?'       , # 6
            "x0?": f'$x_0$ = ?'             , # 7
            "v0?": f'$v_0$ = ?'             , # 8
            "x?": f'$x$ = ?'               , # 9
            "v?": f'$v$ = ?'               , # 10
            "a?": f'$a$ = ?'               , # 11
            "t?": f'$t$ = ?'               , # 12
    }

    values = {
        "x0": x0*s,
        "v0": v0*s,
        "x": x*s,
        "v": v*s,
        "a": a*s,
        "t": t,
    }

    # Define your list
    items = ['x0', 'v0', 'x', 'v', 'a', 't']

    # Generate all combinations of 4 items
    groups_of_4 = list(combinations(items, 4))

    # Split into groups of 4 and 2
    split_combinations = []
    for group_of_4 in groups_of_4:
        group_of_2 = tuple(item for item in items if item not in group_of_4)
        split_combinations.append((group_of_4, group_of_2))

    # Create Probsets
    probsets = []
    for group_4, group_2 in split_combinations:
        if group_4[0] == "v0" and group_4[1] == "v" and group_4[2] == "a" and group_4[3] == "t":
            continue
        variables1 = []
        variables2 = []
        for var in group_4:
            variables1.append(var)
            variables2.append(var)
        variables1.append(group_2[0] + "?")
        variables2.append(group_2[1] + "?")
        probsets.append([variables1, values[group_2[0]]])
        probsets.append([variables2, values[group_2[1]]])

    for iprob, probset in enumerate(probsets):
        clear_canvas()
        axs[2].cla()
        axs[2].set_ylim(-1, 1)  # Constrain vertical space
        axs[2].set_xlim(-10, 10)  # Set axis limits for clarity
        axs[2].axis('off')
        for i, itext in enumerate(probset[0]):
            if itext == "x0": draw_x0()
            if itext == "x": draw_x()
            if itext == "v0": draw_v0()
            if itext == "v": draw_v()
            if itext == "a": draw_a()
            if itext == "t": draw_t()
            axs[2].annotate(texts[itext], (-5, 1.0 - i*0.45), color='black', fontsize=10, ha='left')
        plt.savefig(f"plots/setup{isetup}_prob{iprob}_ans{probset[1]:.2f}.png")

