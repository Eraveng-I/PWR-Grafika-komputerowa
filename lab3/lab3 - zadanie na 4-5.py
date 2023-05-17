#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import math

from random import*
import random

wartosc = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    axes()
    #obrot wszystkiego
    spin(0.25 * time * 180 / 3.1415)

    random.seed(wartosc)
    N=20
    tab = [[[0] * 3 for i in range(N)] for j in range(N)]
    tablica_u = [0 for i in range(N)]
    tablica_v = [0 for i in range(N)]

    for i in range(0,N):
        tablica_u[i] = (i)*(1.0/(N - 1.0))
        tablica_v[i] = (i)*(1.0/(N - 1.0))

    #obrotwszystkiego
    #spin(0.00025 * time * 180 / 3.1415)
    for i in range(0,N):
        for j in range(0,N):
            u = tablica_u[j]
            v = tablica_v[i]
            tab[i][j][0] = (-90* u ** 5 +225*u ** 4 -270*u ** 3 +180 *u ** 2 - 45*u)* math.cos(math.pi * v)
            tab[i][j][1] = 160*u**4 -320*u **3 +160 *u **2 -5
            tab[i][j][2] = (-90* u** 5 +225*u**4 -270*u **3 +180 *u **2 - 45*u)* math.sin(math.pi * v)
            
    #obrot wszystkiego
    #spin(0.25 * time * 180 / 3.1415)
    for i in range(0,N):
        for j in range(0,N):
            #obraca czesc z osiami
            #spin(0.00025 * time * 180 / 3.1415)
            glBegin(GL_LINES)
            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if(i+1 == N):
                i=-1
            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            if(i==-1):
                i=N-1

            #spin(0.00025 * time * 180 / 3.1415)
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if(j+1 == N):
                j=-1
            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            if(j==-1):
                j=N-1
            glEnd()

            '''glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glBegin(GL_TRIANGLES)
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if(i+1 == N):
                i=-1
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            if(i==-1):
                i=N-1

            if(j+1 == N):
                j=-1
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            if(j==-1):
                j=N-1
            glEnd()

            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glBegin(GL_TRIANGLES)
            
            if(i+1 == N):
                i=-1
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            if(i==-1):
                i=N-1

            if(j+1 == N):
                j=-1
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            if(j==-1):
                j=N-1
            
            if(i+1 == N):
                i=-1
            if(j+1 == N):
                j=-1
            glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2])
            if(i==-1):
                i=N-1
            if(j==-1):
                j=N-1

            glEnd()'''

    
    for i in range(0,N):
        glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(0,N):
            
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if(i+1 == N):
                i=-1
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            if(i==-1):
                i=N-1

        glEnd()

    #obrot osi
    #spin(time*180/3.1415)

    #axes()

    glFlush()


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

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
