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

    x =-50
    y=50
    a=50
    b=100
    d=0.0

    random.seed(wartosc)
    d= random.randint(0,255)
    glColor3ub(d, d, 0)

    d=random.randint(-20,20)

    a=a+d
    b=b+d

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

    glFlush()


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
