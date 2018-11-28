"""planets.py: Simulate the planets in solar system.

__author__ = "Haozhe Guo"
__pkuid__  = "1800011809"
__email__  = "guohz0528@pku.edu.cn"
"""


import math
import turtle


"""define a screen
"""
wn = turtle.Screen()
wn.bgcolor('black')
"""display the sun
"""
Phoebus = turtle.Turtle()
Phoebus.shape('circle')
Phoebus.color('yellow')
Phoebus.resizemode('user')
Phoebus.shapesize(2.00, 2.00, 1)
"""adjust the rate of display
"""
turtle.tracer(21, 0.05)


"""parameters
[turtle,color,radius of planet,a,c,b/a,phi]
 hypothetically ,T is in proportion to a
 most of data is fake
"""
Mercury = [0, 'blue', 0.52, 35, 11.0, 0, 0]
Venus = [0, 'orange', 0.70, 64, -8.0, 0, 0]
Earth = [0, 'green', 0.72, 90, 15.0, 0, 0]
Mars = [0, 'red', 0.58, 135, 0.0, 0, 0]
Jupiter = [0, 'purple', 1.40, 250, -50.0, 0, 0]
Saturn = [0, 'gray', 1.28, 350, 150.0, 0, 0]
Halley = [0, 'white', 0.2, 370, -350.0, 0, 0]

para = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Halley]


for i in range(7):
    """define the turtles
    """
    para[i][0] = turtle.Turtle()
    para[i][0].shape('circle')
    para[i][0].color(para[i][1])
    para[i][0].resizemode('user')
    para[i][0].shapesize(para[i][2], para[i][2], 1)
    """compute 'b/a'
    """
    para[i][5] = (para[i][3]**2-para[i][4]**2)**0.5/para[i][3]
    """move the turtles to the initial coordinates
    """
    para[i][0].pu()
    para[i][0].goto(para[i][3]+para[i][4], 0)
    para[i][0].pd()


def starrun(tur, a, c, b_a, phi):

    x = a*math.cos(phi)
    y = a*math.sin(phi)

    if x < -c:
        alpha = 3*math.pi/2-phi+math.atan(y/(x+c))
    elif x > -c:
        alpha = math.pi/2-phi+math.atan(y/(x+c))
    else:
        alpha = math.pi-phi

    sin = math.sin(alpha)
    cos = math.cos(alpha)
    dis = math.hypot(x+c, y)

    if cos < 0.000000001:
        del_phi = math.pi/3/dis/sin
    else:
        del_phi = (sin-(sin**2-math.pi*cos/1.5/dis)**0.5)/cos

    phi = phi+del_phi

    tur.goto(c+a*math.cos(phi), a*math.sin(phi)*b_a)
    return phi


def main():
    """main module
    """
    for k in range(30000):

        for i in range(7):

            tur = para[i][0]
            a = para[i][3]
            c = para[i][4]
            b_a = para[i][5]
            phi = para[i][6]

            para[i][6] = starrun(tur, a, c, b_a, phi)


if __name__ == '__main__':
    main()
