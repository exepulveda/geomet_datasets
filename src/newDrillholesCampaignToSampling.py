import mayavi.mlab as ml
import numpy as np


def doblado(x1, y1, z1, degree, size, azm):
    print azm
    x2 = x1 + np.sin(np.pi / 2. - degree) * np.cos(np.pi / 2. - azm) * size
    y2 = y1 + np.sin(np.pi / 2. - degree) * np.sin(np.pi / 2. - azm) * size
    z2 = z1 - np.sin(np.pi / 2. - degree) * size
    grad2deg = 180.0 / np.pi
    az = azm
    dp = (np.pi / 2. - degree) * grad2deg
    return x2, y2, z2, az, dp


def sampling_drillhole(x_collar, y_collar, z_collar, azm_original, dip_original, len1, length_composite):
    deg2grad = 3.1416 / 180.0
    azm = (90.0 - azm_original + np.random.standard_normal() * 2.) * deg2grad
    dip = (90.0 + dip_original + np.random.standard_normal() * 2.) * deg2grad
    length = len1 + np.random.standard_normal() * len1 / 3.

    orientation = 0
    doblao = False
    if len1 > 80.:
        if np.random.random() > 0.5:
            doblao = True
            if np.random.random() > 0.5:
                orientation = 1.
            else:
                orientation = -1.

    x, y, z, az, dp = np.zeros(100), np.zeros(100), np.zeros(100), np.zeros(100), np.zeros(100)

    degree_final = np.random.random() * 10.
    degree = dip
    for i in range(100):
        if i * length_composite < length:
            if False:
                factor = degree_final / 25.
                degree += factor * np.pi / 180. * orientation
                if i > 0:
                    x[i], y[i], z[i], az[i], dp[i] = doblado(x[i - 1], y[i - 1], z[i - 1], degree, length_composite, azm)
                else:
                    x[i] = x_collar + np.sin(azm) * np.sin(dip) * length_composite * (i + 1)
                    y[i] = y_collar + np.cos(azm) * np.sin(dip) * length_composite * (i + 1)
                    z[i] = z_collar - np.cos(dip) * length_composite * (i + 1)
                    az[i] = (np.pi / 2. - degree) * 180.0 / np.pi
                    dp[i] = (np.pi / 2. - degree) * 180.0 / np.pi
            else:
                x[i] = x_collar + np.cos(azm) * np.sin(dip) * length_composite * (i + 1)
                y[i] = y_collar + np.sin(azm) * np.sin(dip) * length_composite * (i + 1)
                z[i] = z_collar - np.cos(dip) * length_composite * (i + 1)
                az[i] = - azm / deg2grad + 90.0
                dp[i] = dip / deg2grad - 90.0
        else:
            x[i] = -999
    return x, y, z, az, dp


input_path = '..//13-topofinal//topo.out'
topografia = np.loadtxt(input_path, skiprows=6, usecols=(0, 1, 2, 3), dtype=np.float64)
final_anomaly = 1

nx, minx, xsize = 161, -820., 10.
ny, miny, ysize = 120, -630., 10.

space_anomaly1, len1 = 50., 250.
space_anomaly2, len2 = 100., 350.
numbe_anomaly3, len3 = 100, 400.
numbe_relleno, len4 = 100, 200.

x_collar = []
y_collar = []
z_collar = []
flag_anomaly = []
anomaly = []
n_drillholes = 0
length_composite = 5.0
error_sampling = 15.

x = topografia[:, 0]
y = topografia[:, 1]
z = topografia[:, 2]
a = topografia[:, 3]

nx_jump_1 = int(space_anomaly1 / xsize)
ny_jump_1 = int(space_anomaly1 / ysize)
nx_jump_2 = int(space_anomaly2 / xsize)
ny_jump_2 = int(space_anomaly2 / ysize)

for j in range(ny):
    nn = j * nx
    for i in range(nx):
        n = nn + i
        if a[n] < 2:
            if (i % nx_jump_1 == 0) and (j % ny_jump_1 == 0):
                x_collar.append(x[n] + np.random.random() * error_sampling)
                y_collar.append(y[n] + np.random.random() * error_sampling)
                z_collar.append(z[n])
                flag_anomaly.append(1)
                anomaly.append(a[n])
                n_drillholes += 1
for j in range(ny):
    nn = (j + int(ny_jump_2 / 2)) * nx
    for i in range(nx):
        n = nn + i + int(nx_jump_2 / 2)
        if n < len(a) - 1:
            if a[n] < 3:
                if (i % nx_jump_2 == 0) and (j % ny_jump_2 == 0):
                    x_collar.append(x[n] + np.random.random() * error_sampling)
                    y_collar.append(y[n] + np.random.random() * error_sampling)
                    z_collar.append(z[n])
                    flag_anomaly.append(2)
                    anomaly.append(a[n])
                    n_drillholes += 1

kk = 0
r = 30.
while True:
    ix = np.random.randint(nx)
    iy = np.random.randint(ny)
    n = iy * nx + ix
    if n < len(a) - 1:
        if a[n] < 4:
            entry = True
            for k in range(len(x_collar)):
                if (np.abs(x_collar[k] - x[n]) < r) and (np.abs(y_collar[k] - y[n]) < r):
                    entry = False
                    break
            if entry:
                x_collar.append(x[n] + np.random.random() * error_sampling)
                y_collar.append(y[n] + np.random.random() * error_sampling)
                z_collar.append(z[n])
                flag_anomaly.append(3)
                anomaly.append(a[n])
                n_drillholes += 1
    if kk == numbe_anomaly3:
        break
    kk += 1

kk = 0
parts_y = int(ny / numbe_relleno)
r = 50.
while True:
    ix = np.random.randint(nx)
    iy = np.random.randint(ny)
    n = iy * nx + ix
    if n < len(a) - 1:
        if a[n] < 3:
            entry = True
            for k in range(len(x_collar)):
                if (np.abs(x_collar[k] - x[n]) < r) and (np.abs(y_collar[k] - y[n]) < r):
                    entry = False
                    break
            if entry:
                x_collar.append(x[n] + np.random.random() * error_sampling)
                y_collar.append(y[n] + np.random.random() * error_sampling)
                z_collar.append(z[n])
                flag_anomaly.append(4)
                anomaly.append(a[n])
                n_drillholes += 1
    if kk == 1000:
        break
    kk += 1

kk = 0
parts_y = int(ny / numbe_relleno)
r = 20.
while True:
    ix = np.random.randint(nx)
    iy = np.random.randint(ny)
    n = iy * nx + ix
    if n < len(a) - 1:
        if a[n] < 2:
            entry = True
            for k in range(len(x_collar)):
                if (np.abs(x_collar[k] - x[n]) < r) and (np.abs(y_collar[k] - y[n]) < r):
                    entry = False
                    break
            if entry:
                x_collar.append(x[n])
                y_collar.append(y[n])
                z_collar.append(z[n])
                flag_anomaly.append(5)
                anomaly.append(a[n])
                n_drillholes += 1
    if kk == 1000:
        break
    kk += 1

print 'drillholes: ', n_drillholes
x_composite = np.zeros((100, n_drillholes))
y_composite = np.zeros((100, n_drillholes))
z_composite = np.zeros((100, n_drillholes))
az_composite = np.zeros((100, n_drillholes))
dp_composite = np.zeros((100, n_drillholes))
an_composite = np.zeros((100, n_drillholes))

dip_original = -90.0
azm_original = 0.0
for k in range(n_drillholes):
    azm = azm_original
    dip = dip_original
    if flag_anomaly[k] == 1:
        azm = -90
        dip = -75
        xx, yy, zz, az, dp = sampling_drillhole(x_collar[k], y_collar[k], z_collar[k], azm, dip, len1, length_composite)
        for i in range(len(xx)):
            x_composite[i, k] = xx[i]
            y_composite[i, k] = yy[i]
            z_composite[i, k] = zz[i]
            az_composite[i, k] = az[i]
            dp_composite[i, k] = dp[i]
            an_composite[i, k] = 1
    elif flag_anomaly[k] == 2:
        azm = 90
        dip = -75
        xx, yy, zz, az, dp = sampling_drillhole(x_collar[k], y_collar[k], z_collar[k], azm, dip, len2 / anomaly[k], length_composite)
        for i in range(len(xx)):
            x_composite[i, k] = xx[i]
            y_composite[i, k] = yy[i]
            z_composite[i, k] = zz[i]
            az_composite[i, k] = az[i]
            dp_composite[i, k] = dp[i]
            an_composite[i, k] = 2
    elif flag_anomaly[k] == 3:
        azm = -45.
        dip = -75.
        xx, yy, zz, az, dp = sampling_drillhole(x_collar[k], y_collar[k], z_collar[k], azm, dip, len3 / anomaly[k], length_composite)
        for i in range(len(xx)):
            x_composite[i, k] = xx[i]
            y_composite[i, k] = yy[i]
            z_composite[i, k] = zz[i]
            az_composite[i, k] = az[i]
            dp_composite[i, k] = dp[i]
            an_composite[i, k] = 3
    elif flag_anomaly[k] == 4:
        azm = float(np.random.randint(-180, high=180))
        dip = float(np.random.randint(-90-30, high=-90+30))
        xx, yy, zz, az, dp = sampling_drillhole(x_collar[k], y_collar[k], z_collar[k], azm, dip, len4, length_composite)
        for i in range(len(xx)):
            x_composite[i, k] = xx[i]
            y_composite[i, k] = yy[i]
            z_composite[i, k] = zz[i]
            az_composite[i, k] = az[i]
            dp_composite[i, k] = dp[i]
            an_composite[i, k] = 4
    elif flag_anomaly[k] == 5:
        azm = float(np.random.randint(0, high=360))
        dip = float(np.random.randint(-90-5, high=-90+5))
        xx, yy, zz, az, dp = sampling_drillhole(x_collar[k], y_collar[k], z_collar[k], azm, dip, len4, length_composite)
        for i in range(len(xx)):
            x_composite[i, k] = xx[i]
            y_composite[i, k] = yy[i]
            z_composite[i, k] = zz[i]
            az_composite[i, k] = az[i]
            dp_composite[i, k] = dp[i]
            an_composite[i, k] = 5

f = open('Drillholes.out', 'w')
string = 'Sondajes\n9\nDHID\nmidx\nmidy\nmidz\nfrom\nto\nazimut\ndip\nanomalia\n'
f.write(string)

for i in range(len(topografia[:, 3])):
    if topografia[i, 3] <= final_anomaly:
        topografia[i, 3] = final_anomaly

pts = ml.points3d(topografia[:, 0], topografia[:, 1], topografia[:, 2], topografia[:, 3],
                  vmin=1, vmax=5, scale_mode='none', scale_factor=0.2, transparent=True, opacity=0.9)
mesh = ml.pipeline.delaunay2d(pts)
surf = ml.pipeline.surface(mesh, transparent=True, opacity=0.9)
surf.scene.background = (1, 1, 1)
surf.scene.parallel_projection = False
surf.actor.property.point_size = 3

desp = 50
xmin = [min(topografia[:, 0]) - desp, max(topografia[:, 0]) + desp]
ymin = [min(topografia[:, 1]) - desp, max(topografia[:, 1]) + desp]
zmin = [min(topografia[:, 2]) - desp, max(topografia[:, 2]) + desp]

#point = ml.points3d(xmin, ymin, zmin, zmin, name='caja_topo', mode='point', scale_mode='none')
#ax = ml.axes(color=(0.0, 0.0, 0.0), nb_labels=10, xlabel='Easting', ylabel='Norting', zlabel='Elevation',
#             x_axis_visibility=True, y_axis_visibility=True, z_axis_visibility=True,
#             ranges=[min(xmin), max(xmin), min(ymin), max(ymin), min(zmin), max(zmin)])
#ax.axes.font_factor = 1
#ax.axes.label_format = '%.0f'

xx, yy, zz, aa = [], [], [], []
for k in range(n_drillholes):
    #if flag_anomaly[k] == final_anomaly:
    if k < 9:
        dhide = 'DDH-00' + str(k + 1)
    elif k < 99:
        dhide = 'DDH-0' + str(k + 1)
    else:
        dhide = 'DDH-' + str(k + 1)
    label = ml.text(x_collar[k], y_collar[k], dhide, z=z_collar[k], width=0.2, name=dhide)
    label.property.shadow = True
    point = ml.points3d(x_collar[k], y_collar[k], z_collar[k], 2., name=dhide,
                        mode='axes', vmin=0., vmax=1., scale_mode='none')
    point.glyph.glyph_source.glyph_source.scale_factor = 20.
    point.glyph.glyph.scaling = 0

    for i in range(len(x_composite[:, k])):
        if x_composite[i, k] != -999:
            xx.append(x_composite[i, k])
            yy.append(y_composite[i, k])
            zz.append(z_composite[i, k])
            aa.append(flag_anomaly[k])
            string = str(k+1) + ' ' + str(x_composite[i, k]) + ' ' + str(y_composite[i, k]) + ' ' + str(z_composite[i, k]) \
                     + ' ' + str(i * length_composite) + ' ' + str((i + 1) * length_composite) \
                     + ' ' + str(az_composite[i, k]) + ' ' + str(dp_composite[i, k]) + ' ' + str(an_composite[i, k]) + ' \n'
            f.write(string)

point = ml.points3d(xx, yy, zz, aa, mode='point', scale_mode='none', vmin=1, vmax=5)
point.scene.background = (1, 1, 1)
point.scene.parallel_projection = True
point.actor.property.point_size = 6
point.glyph.glyph.scaling = 0
ml.view(0, 0)
f.close()
ml.show()
