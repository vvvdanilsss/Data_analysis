import math
import numpy as np
import matplotlib.pyplot as plt

a11, a12, b1 = map(float, input().split())
a21, a22, b2 = map(float, input().split())

matrix_a = np.array([[a11, a12], [a21, a22]])
matrix_b = np.array([[b1], [b2]])

rang_matrix_a = np.linalg.matrix_rank(matrix_a)
rang_matrix_ab = np.linalg.matrix_rank(np.hstack([matrix_a, matrix_b]))


def plot_graph(n):
    x1, y1 = check_div_zero(a11, a12, b1)
    x2, y2 = check_div_zero(a21, a22, b2)
    plt.figure(figsize=(10, 10))

    if n == 1:
        if x1 is not None:
            plt.plot(x1, y1, label=f'Прямая {a11}x+{a12}y={b1}')

        if x2 is not None:
            plt.plot(x2, y2, label=f'Прямая {a21}x+{a22}y={b2}')

    if n == 2:
        if x1 is not None:
            plt.plot(x1, y1, label=f'Прямая {a11}x+{a12}y={b1}')

        elif x2 is not None:
            plt.plot(x2, y2, label=f'Прямая {a21}x+{a22}y={b2}')

    if n == 3:
        x, y = np.linalg.solve(matrix_a, matrix_b)
        plt.scatter(x, y, label=f'Точка ({round(*x, 3)},{round(*y, 3)})')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Иллюстрация решений системы уравнений')
    plt.legend()
    plt.grid(True)
    plt.show()


def check_div_zero(a1, a2, b):
    pool_x = pool_y = [0, 10]

    if not math.isclose(a1, 0):
        pool_x = [(b - a2 * y0) / a1 for y0 in pool_y]

    elif not math.isclose(a2, 0):
        pool_y = [(b - a1 * x0) / a2 for x0 in pool_x]

    else:
        return None, None

    return pool_x, pool_y


if rang_matrix_a != rang_matrix_ab:
    plot_graph(1)

elif rang_matrix_a < 2:
    plot_graph(2)

else:
    plot_graph(3)