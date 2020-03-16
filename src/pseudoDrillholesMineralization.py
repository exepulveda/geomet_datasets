import numpy as np


def write_lastre(f, code, points, xmin, xmax, ymin, ymax, zmin, zmax):
    X = np.arange(xmin, xmax, (xmax - xmin) / (points[0]*2))
    Y = np.arange(ymin, ymax, (ymax - ymin) / (points[1]*2))
    Z = np.arange(zmin, zmax, (zmax - zmin) / points[2])

    for z in Z:
        for y in Y:
            for x in X:
                string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
                f.write(string)


def write_oxidos(f, code, points, xmin, xmax, ymin, ymax, zmin, zmax, r):
    X = np.arange(xmin, xmax, (xmax - xmin) / points[0])
    Y = np.arange(ymin, ymax, (ymax - ymin) / points[1])
    Z = np.arange(zmin, zmax, (zmax - zmin) / points[2])

    for z in Z:
        for y in Y:
            for x in X:
                R = np.sqrt(x * x + y * y)
                if R < r:
                    string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
                    f.write(string)


def write_mixto(f, code, points, xmin, xmax, ymin, ymax, zmin, zmax, r):
    X = np.arange(xmin, xmax, (xmax - xmin) / points[0])
    Y = np.arange(ymin, ymax, (ymax - ymin) / points[1])
    Z = np.arange(zmin, zmax, (zmax - zmin) / points[2])

    for z in Z:
        for y in Y:
            for x in X:
                R = np.sqrt(x * x + y * y)
                if R < r / 2:
                    string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
                    f.write(string)


def write_primario(f, code, points, xmin, xmax, ymin, ymax, zmin, zmax, r, pipa):
    X = np.arange(xmin, xmax, (xmax - xmin) / points[0])
    Y = np.arange(ymin, ymax, (ymax - ymin) / points[1])
    Z = np.arange(zmin, zmax, (zmax - zmin) / points[2])

    for z in Z:
        for y in Y:
            for x in X:
                R = np.sqrt(x * x + y * y)
                if True:
                    if R > (zmax - zmin + 200.) * pipa / (z - zmin + 200.):
                        if R < 350:
                            string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
                            f.write(string)
                    else:
                        string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(4.) + ' \n'
                        f.write(string)


def write_caja(f, code, xmin, xmax, ymin, ymax, zmin, zmax):
    X = np.arange(xmin, xmax, (xmax - xmin) / 20)
    Y = np.arange(ymin*1.5/1.0, ymax*1.5/1.0, (ymax - ymin) / 20*2./1.0)
    Z = np.arange(zmin, zmax, (zmax - zmin) / 20)

    for z in Z:
        for y in Y:
            x = X[0]
            string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
            f.write(string)
            x = X[len(X) - 1]
            string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
            f.write(string)
    for z in Z:
        for x in X:
            y = Y[0]
            string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
            f.write(string)
            y = Y[len(Y) - 1]
            string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
            f.write(string)
    for x in X:
        for y in Y:
            z = Z[0]
            string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
            f.write(string)
            z = Z[len(Z) - 1]
            string = str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(code) + ' \n'
            f.write(string)

output_path = 'minz_drillholes.prn'

xmin = -800/2.0
xmax = +800/2.0
ymin = -800/2.0
ymax = +800/2.0
zmin = 1500.0
zmax = 2500.0

ancho_caja = 100.
zlastre_max = zmax
zlastre_min = zlastre_max - 20.
zoxidos_max = zlastre_min - 50.
zoxidos_min = zoxidos_max - 20.
zmixto_max = zoxidos_min - 20.
zmixto_min = zmixto_max - 10.
zprimario_max = zmixto_min - 20.
zprimario_min = zprimario_max - 500.
suelo = zprimario_min - 50

points = [10, 10, 10]
rock_list = [5, 1, 2, 3] # 5 intrusivo plutonico

f = open(output_path, 'w')
string = 'Sondajes\n4\nmidx\nmidy\nmidz\nminz\n'
f.write(string)

r = 250
#write_lastre(f, rock_list[0], points, xmin, xmax, ymin, ymax, zlastre_min, zlastre_max)
write_oxidos(f, rock_list[1], points, xmin, xmax, ymin, ymax, zoxidos_min, zoxidos_max, r)
write_mixto(f, rock_list[2], points, xmin, xmax, ymin, ymax, zmixto_min, zmixto_max, r)
write_primario(f, rock_list[3], points, xmin, xmax, ymin, ymax, zprimario_min, zprimario_max, r, r * 3 / 4)
#write_lastre(f, rock_list[0], points, xmin, xmax, ymin, ymax, suelo, suelo - 10)

write_caja(f, rock_list[0], xmin - ancho_caja, xmax + ancho_caja,
           ymin - ancho_caja, ymax + ancho_caja, zlastre_max + ancho_caja, suelo - 10 - ancho_caja)

f.close()

values = np.loadtxt(output_path, skiprows=6, usecols=(0, 1, 2), dtype=np.float64)
size = [10., 10., 5.]
minimos = [np.min(values[:, 0]) - size[0], np.min(values[:, 1]) - size[1], np.min(values[:, 2]) - size[2]]
maximos = [np.max(values[:, 0]) + size[0], np.max(values[:, 1]) + size[1], np.max(values[:, 2]) + size[2]]
largos = [(maximos[0] - minimos[0]), (maximos[1] - minimos[1]), (maximos[2] - minimos[2])]
nodos = [(maximos[0] - minimos[0])/size[0], (maximos[1] - minimos[1])/size[1], (maximos[2] - minimos[2])/size[2]]

print 'min: ', minimos
print 'max: ', maximos
print 'siz: ', size
print 'lar: ', largos
print 'nod: ', nodos
