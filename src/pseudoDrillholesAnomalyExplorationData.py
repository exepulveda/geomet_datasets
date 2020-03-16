import numpy as np


output_path = 'Muestras.prn'

x_min = -810.
x_max = -810. + 1710.
y_min = -630
y_max = -630 + 1300.

points = [25, 25]

X = np.linspace(x_min, x_max, num=points[0], endpoint=True)
Y = np.linspace(y_min, y_max, num=points[1], endpoint=True)
R = np.linspace(0., (y_max - y_min) * 0.4, num=5, endpoint=True)

f = open(output_path, 'w')
f.write('anomaly\n3\nmidx\nmidy\nvalue\n')

for x in X:
    for y in Y:
        r = np.sqrt(x * x + y * y)
        value = 5

        for i in range(len(R)):
            if r <= R[i]:
                value = i
                break

        string = str(x) + ' ' + str(y) + ' ' + str(value) + ' \n'
        f.write(string)

f.close()
