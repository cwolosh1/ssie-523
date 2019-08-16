from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def initialize(x0, y0, z0):
    global x, y, z, xresult, yresult, zresult
    x = x0
    y = y0
    z = z0
    xresult = [x]
    yresult = [y]
    zresult = [z]
    
def observe():
    global x, y, z, xresult, yresult, zresult
    xresult.append(x)
    yresult.append(y)
    zresult.append(z)
    
def update():
    global x, y, z, xresult, yresult, zresult
    nextx = x - y
    nexty = -x -3*y + z
    nextz = y + z
    x, y, z = nextx, nexty, nextz

def main():
    ax = gca(projection='3d')
    for x0 in arange(-2, 2, 1):
        for y0 in arange(-2, 2, 1):
            for z0 in arange(-2, 2, 1):
                initialize(x0, y0, z0)
                for t in range(30):
                    update()
                    observe()
                ax.plot(xresult, yresult, zresult, 'b')
    show()

main()