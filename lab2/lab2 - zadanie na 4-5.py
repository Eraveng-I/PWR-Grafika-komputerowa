#!/usr/bin/env python3
import sys
from random import*
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

wartosc = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass



def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    x =-90
    y=60
    a=120
    b=180
    d=0
    e=0
    f=0

    random.seed(wartosc)

    #losujemy kolor
    d= random.randint(0,255)
    e= random.randint(0,255)
    f= random.randint(0,255)
    glColor3ub(d, e, f)

    rysuj_prostokat(x,y,a,b)
    
    #losujemy kolor
    d= random.randint(0,255)
    e= random.randint(0,255)
    f= random.randint(0,255)
    glColor3ub(d, e, f)

    rysuj_dywan(x,y,a,b,4)

    glFlush()

def rysuj_prostokat(x,y,a,b):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x, y-a)
    glVertex2f(x+b, y)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(x+b, y)
    glVertex2f(x, y-a)
    glVertex2f(x+b, y-a)
    glEnd()


def rysuj_dywan(x,y,a,b,poziom):

    if(poziom>0):
        nowy_a = a/3
        nowy_b = b/3
        rysuj_prostokat(x+nowy_b,y-nowy_a,nowy_a,nowy_b)    #wycinamy srodek
        poziom=poziom-1
        for i in range(3):
            for j in range(3):
                if (i!=1 or j!=1):
                    nowy_x = x + i*nowy_b
                    nowy_y = y - j*nowy_a
                    rysuj_dywan(nowy_x, nowy_y, nowy_a, nowy_b, poziom)


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
