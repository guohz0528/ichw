"""tile.py: Try to tile a wall.
__author__ = "Haozhe Guo"
__pkuid__  = "1800011809"
__email__  = "guohz0528@pku.edu.cn"
"""


def dtm(x, wall, a, b, m, n):
    """determine if a tile can be put
    """
    if m-x % m >= a and n-x//m >= b:
        dtm = True

        for i in range(1, a):
            dtm = dtm and wall[x+i]

    else:
        dtm = False

    return dtm


def onize(x, m, a, b, wall, way):
    """put a tile on the wall
    """
    wy = [k for k in way]
    wl = [k for k in wall]

    tup = []

    for i in range(a):
        for j in range(b):
            x_ = x+i+j*m

            wl[x_] = False
            tup.append(x_)

    wy.append(tuple(tup))

    return (wy, wl)


def put(s, wall, a, b, m, n, mn, way):
    """tile the wall
    """
    for x in range(s, mn):
        if wall[x]:

            if dtm(x, wall, a, b, m, n):
                wy, wl = onize(x, m, a, b, wall, way)
                put(x+a, wl, a, b, m, n, mn, wy)

            if dtm(x, wall, b, a, m, n):
                wy, wl = onize(x, m, b, a, wall, way)
                put(x+b, wl, a, b, m, n, mn, wy)

            return

    global tile
    tile.append(way)


def put_(s, wall, a, m, n, mn, way):
    """tile the wall
    """
    for x in range(s, mn):
        if wall[x]:

            if dtm(x, wall, a, a, m, n):
                wy, wl = onize(x, m, a, a, wall, way)
                put_(x+a, wl, a, m, n, mn, wy)

            return

    global tile
    tile.append(way)


def tat(m, t, i0, i_1):
    """draw a tile
    """
    t.pu()
    t.goto(i0 % m*20, i0//m*20)

    t.pd()
    t.goto(i_1 % m*20+20, i0//m*20)
    t.goto(i_1 % m*20+20, i_1//m*20+20)
    t.goto(i0 % m*20, i_1//m*20+20)
    t.goto(i0 % m*20, i0//m*20)


def tur(m, p, mn):
    """let a turtle draw the tiled wall
    """
    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    global tile
    for i in tile[p]:
        tat(m, t, i[0], i[-1])

    turtle.done()


def tryit(m, n, a, b):
    """try it
    """
    mn = m*n

    if (mn) % (a*b) == 0 and max(m, n) >= max(a, b) and min(m, n) >= min(a, b):

        wall = []
        for y in range(mn):
            wall.append(True)

        if a != b:
            put(0, wall, a, b, m, n, mn, [])
        else:
            put_(0, wall, a, m, n, mn, [])


def output(m, n, a, b):
    """output
    """
    mn = int(m*n/a/b)

    global tile
    long = len(tile)

    if long == 0:
        print('Sorry, but the tiles cannot pave the wall exactly.')

    elif long == 1:
        print('There is only one way to tile the wall:')
        print(tile[0])

        tur(m, 0, mn)

    else:
        print('There are', long, 'ways to tile the wall:')
        for p in range(long):
            print(p, ' : ', tile[p])

        p = int(input('You can input the number of the tiling way you want to display.'))
        tur(m, p, mn)


def main():
    """main module
    """
    m, n = map(int, input('Please input the height and the width of the wall, separate them by a blank.').split())
    a, b = map(int, input('Please input the length and the width of the tiles, separate them by a blank.').split())

    tryit(m, n, a, b)

    output(m, n, a, b)


if __name__ == '__main__':
    tile = []
    main()
