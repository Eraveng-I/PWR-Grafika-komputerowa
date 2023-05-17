#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import math

from random import*
import random

wartosc = random.random()

viewer = [0.0, 0.0, 10.0]

phi=0.0
theta = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
mouse_x_pos_old = 0
mouse_y_pos_old = 0
delta_x = 0
delta_y = 0
R = 5.0

#1 zrodlo swiata
mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001


#2 zrodlo swiata
mat_ambient1 = [1.0, 1.0, 1.0, 1.0]
mat_diffuse1 = [1.0, 1.0, 1.0, 1.0]
mat_specular1 = [1.0, 1.0, 1.0, 1.0]
mat_shininess1 = 20.0

light_ambient1 = [0.1, 0.1, 0.0, 1.0]
light_diffuse1 = [0.8, 0.4, 0.6, 1.0]
light_specular1 = [1.0, 1.0, 1.0, 1.0]
light_position1 = [0.0, 10.0, 0.0, 1.0]

att_constant1 = 1.0
att_linear1 = 0.05
att_quadratic1 = 0.001

duza_tablica = [light_ambient1,light_diffuse1,light_specular1]
wyznacznik1 =0
wyznacznik2 =0

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient1)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse1)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular1)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess1)

    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)

    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant1)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear1)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic1)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT1)


def shutdown():
    pass


def render(time):
    global theta
    global phi

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle
        theta = theta%360

    glRotatef(theta, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        phi += delta_y * pix2angle
        phi = phi%360

    glRotatef(phi, 1.0, 0.0, 0.0)

    '''
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)

    xs = R * math.cos(theta*math.pi/180) * math.cos(phi*math.pi/180)
    ys = R * math.sin(phi*math.pi/180)
    zs = R * math.sin(theta*math.pi/180) * math.cos(phi*math.pi/180)
    glTranslate(xs, ys, zs)

    quadric2 = gluNewQuadric()
    gluQuadricDrawStyle(quadric2, GLU_LINE)
    gluSphere(quadric2, 0.5, 6, 5)
    gluDeleteQuadric(quadric2)

    light_position1[0] = xs
    light_position1[1] = ys
    light_position1[2] = zs
    #glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    '''

    random.seed(wartosc)
    N=20
    tab = [[[0] * 3 for i in range(N)] for j in range(N)]
    tablica_u = [0 for i in range(N)]
    tablica_v = [0 for i in range(N)]
    vektory = [[[0] * 3 for i in range(N)] for j in range(N)]

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

            xu = ( -450*u ** 4 +900*u ** 3 -810 *u ** 2 +360*u -45)* math.cos(math.pi * v)
            xv = math.pi*(90* u ** 5 -225*u ** 4 +270*u ** 3 -180 *u ** 2 + 45*u)* math.sin(math.pi * v)
            yu = (640*u ** 3 -960 *u ** 2 +320*u)
            yv = 0
            zu = ( -450*u ** 4 +900*u ** 3 -810 *u ** 2 +360*u -45)* math.sin(math.pi * v)
            zv = -math.pi*(90* u ** 5 -225*u ** 4 +270*u ** 3 -180 *u ** 2 + 45*u)* math.cos(math.pi * v)

            vektory[i][j][0] = yu*zv-zu*yv
            vektory[i][j][1] = zu*xv-xu*zv
            vektory[i][j][2] = xu*yv-yu*xv

            #normalizacja wektorow
            dlugosc = vektory[i][j][0]**2 + vektory[i][j][1]**2 + vektory[i][j][2]**2
            dlugosc = dlugosc**(1/2)

            if(dlugosc==0.0):
                dlugosc=1.0

            vektory[i][j][0] = vektory[i][j][0] / dlugosc
            vektory[i][j][1] = vektory[i][j][1] / dlugosc
            vektory[i][j][2] = vektory[i][j][2] / dlugosc

            

            
    #obrot wszystkiego
    #spin(0.25 * time * 180 / 3.1415)
    for i in range(0,N):
        for j in range(0,N):
            #obraca czesc z osiami
            #spin(0.00025 * time * 180 / 3.1415)
            glBegin(GL_LINES)
            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glNormal(vektory[i][j][0],vektory[i][j][1],vektory[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if(i+1 == N):
                i=-1
            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glNormal(vektory[i+1][j][0],vektory[i+1][j][1],vektory[i+1][j][2])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            if(i==-1):
                i=N-1

            #spin(0.00025 * time * 180 / 3.1415)
            glNormal(vektory[i][j][0],vektory[i][j][1],vektory[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if(j+1 == N):
                j=-1
            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glNormal(vektory[i][j+1][0],vektory[i][j+1][1],vektory[i][j+1][2])
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            if(j==-1):
                j=N-1
            glEnd()

            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glBegin(GL_TRIANGLES)
            glNormal(vektory[i][j][0],vektory[i][j][1],vektory[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if(i+1 == N):
                i=-1
            glNormal(vektory[i+1][j][0],vektory[i+1][j][1],vektory[i+1][j][2])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            if(i==-1):
                i=N-1

            if(j+1 == N):
                j=-1
            glNormal(vektory[i][j+1][0],vektory[i][j+1][1],vektory[i][j+1][2])
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            if(j==-1):
                j=N-1
            glEnd()

            glColor3ub(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            glBegin(GL_TRIANGLES)
            
            if(i+1 == N):
                i=-1
            glNormal(vektory[i+1][j][0],vektory[i+1][j][1],vektory[i+1][j][2])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            if(i==-1):
                i=N-1

            if(j+1 == N):
                j=-1
            glNormal(vektory[i][j+1][0],vektory[i][j+1][1],vektory[i][j+1][2])
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            if(j==-1):
                j=N-1
            
            if(i+1 == N):
                i=-1
            if(j+1 == N):
                j=-1
            glNormal(vektory[i+1][j+1][0],vektory[i+1][j+1][1],vektory[i+1][j+1][2])
            glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2])
            if(i==-1):
                i=N-1
            if(j==-1):
                j=N-1

            glEnd()


    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global wyznacznik1
    global wyznacznik2

    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    if key == GLFW_KEY_P and action == GLFW_PRESS:
        wyznacznik1=wyznacznik1+1
        if(wyznacznik1==4):
            wyznacznik1=0
            wyznacznik2=wyznacznik2+1
            if(wyznacznik2==3):
                wyznacznik2=0
        print("jest ustawiony parametr: ",wyznacznik2+1,wyznacznik1+1)

    if key == GLFW_KEY_O and action == GLFW_PRESS:
        duza_tablica[wyznacznik2][wyznacznik1] = duza_tablica[wyznacznik2][wyznacznik1] + 0.1

        if(duza_tablica[wyznacznik2][wyznacznik1]>=1.0):
            duza_tablica[wyznacznik2][wyznacznik1] = 1.0
        print(wyznacznik2+1,wyznacznik1+1, "parametr jest ustawiony na: ",duza_tablica[wyznacznik2][wyznacznik1])


    if key == GLFW_KEY_I and action == GLFW_PRESS:
        duza_tablica[wyznacznik2][wyznacznik1] = duza_tablica[wyznacznik2][wyznacznik1] - 0.1

        if(duza_tablica[wyznacznik2][wyznacznik1]<=0.0):
            duza_tablica[wyznacznik2][wyznacznik1] = 0.0
        print(wyznacznik2+1,wyznacznik1+1, "parametr jest ustawiony na: ",duza_tablica[wyznacznik2][wyznacznik1])

        

def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos

    global delta_y
    global mouse_y_pos_old

    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
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
