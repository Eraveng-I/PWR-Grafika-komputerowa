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
    spin(0.1 * time * 180 / 3.1415)

    random.seed(wartosc)
    rozmiar=5
    wierzcholki = [[0] * 3 for i in range(5)]
    bok = 5.0
    wysokosc = 0.7*bok

    #ustalenie wspolrzednych
    wierzcholki[1][0]=bok
    wierzcholki[2][0]=bok
    wierzcholki[2][2]=bok
    wierzcholki[3][2]=bok
    wierzcholki[4][0]=bok/2
    wierzcholki[4][2]=bok/2
    wierzcholki[4][1]=wysokosc

    x=wierzcholki[4][0]
    y=wierzcholki[4][1]
    z=wierzcholki[4][2]
 
    #bok=bok/rozmiar
    #wysokosc=wysokosc/rozmiar
    #mechanizm(wierzcholki[4][0],wierzcholki[4][1],wierzcholki[4][2],bok,wysokosc,rozmiar,0,0)
    mechanizm2(wierzcholki[4][0],wierzcholki[4][1],wierzcholki[4][2],bok,wysokosc,rozmiar)
    glFlush()

def mechanizm2(x,y,z,bok,wysokosc,rozmiar):
    if(rozmiar>0):
        rozmiar=rozmiar-1
        bok=bok/2
        wysokosc=wysokosc/2

        mechanizm2(x,y,z,bok,wysokosc,rozmiar)
        mechanizm2(x-bok/2,y-wysokosc,z-bok/2,bok,wysokosc,rozmiar)
        mechanizm2(x+bok/2,y-wysokosc,z-bok/2,bok,wysokosc,rozmiar)
        mechanizm2(x+bok/2,y-wysokosc,z+bok/2,bok,wysokosc,rozmiar)
        mechanizm2(x-bok/2,y-wysokosc,z+bok/2,bok,wysokosc,rozmiar)
    else:
        rysuj_ostroslup(x,y,z,bok,wysokosc)

def mechanizm(x,y,z,bok,wysokosc,rozmiar,kierunek,kontrola):
    if(rozmiar>0):
        rysuj_ostroslup(x,y,z,bok,wysokosc)
        rozmiar=rozmiar-1
        if(kierunek==0):
           mechanizm(x-bok/2,y-wysokosc,z-bok/2,bok,wysokosc,rozmiar,1,kontrola)
           mechanizm(x+bok/2,y-wysokosc,z-bok/2,bok,wysokosc,rozmiar,2,kontrola)
           mechanizm(x+bok/2,y-wysokosc,z+bok/2,bok,wysokosc,rozmiar,3,kontrola)
           mechanizm(x-bok/2,y-wysokosc,z+bok/2,bok,wysokosc,rozmiar,4,kontrola)
        if(kierunek==1):
            if(kontrola==1 or kontrola==0 or rozmiar==2):
                mechanizm(x-bok/2,y-wysokosc,z-bok/2,bok,wysokosc,rozmiar,0,kierunek)
        if(kierunek==2):
            if(kontrola==2 or kontrola==0 or rozmiar==2):
                mechanizm(x+bok/2,y-wysokosc,z-bok/2,bok,wysokosc,rozmiar,0,kierunek)
        if(kierunek==3):
            if(kontrola==3 or kontrola==0 or rozmiar==2):
                mechanizm(x+bok/2,y-wysokosc,z+bok/2,bok,wysokosc,rozmiar,0,kierunek)
        if(kierunek==4):
            if(kontrola==4 or kontrola==0 or rozmiar==2):
                mechanizm(x-bok/2,y-wysokosc,z+bok/2,bok,wysokosc,rozmiar,0,kierunek)

def rysuj_ostroslup(x,y,z,bok,wysokosc):
    glColor3ub(255,0,0)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(x-bok/2,y-wysokosc,z-bok/2)
    glVertex3f(x+bok/2,y-wysokosc,z-bok/2)
    glColor3ub(0,0,255)
    glVertex3f(x-bok/2,y-wysokosc,z+bok/2)
    
    glVertex3f(x+bok/2,y-wysokosc,z+bok/2)
    glEnd()

    glColor3ub(0,255,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(x,y,z)

    glVertex3f(x-bok/2,y-wysokosc,z-bok/2)
    glVertex3f(x+bok/2,y-wysokosc,z-bok/2)
    glVertex3f(x+bok/2,y-wysokosc,z+bok/2)
    glVertex3f(x-bok/2,y-wysokosc,z+bok/2)
    glVertex3f(x-bok/2,y-wysokosc,z-bok/2)
    glEnd()
    

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
