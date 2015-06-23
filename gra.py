__author__ = 'illmoded'

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math as m

import zwierza
import teren

f = open('plik.txt', 'w')
dzien = 0
rozmiar = 100
poczatkowa_liczba_zwierzat = 20

rot_x = 0.
rot_y = 0.
rot_z = 0.
eyesz = 2.
zoom = 65.
maxzoom = 1.
minzoom = 10.
action = ""
xStart = yStart = 0.
xTrans = 0.
yTrans = 0.

ziemia = teren.generuj_teren(rozmiar)
lista_zwierzat = zwierza.generuj_zwierzeta(poczatkowa_liczba_zwierzat, rozmiar)

def init():
    glEnable(GL_NORMALIZE)
    light_ambient =  [1.0, 1.0, 1.0, 0.0]
    light_position =  [1.0, 1.0, 1.0, 0.0]

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, light_ambient)
    # glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)

def szecian(x, y, z, h):
    glTranslate(x * h - 1, y * h - 1, z)
    glutSolidCube(h)
    glTranslate(-(x * h - 1), -(y * h - 1), -z)

def sfera(x, y, z, h):
    glTranslate(x * h - 1, y * h - 1, z)
    glutSolidSphere(h/2., 10, 10)
    glTranslate(0, 0, h/4.)
    glutSolidCone(h/3., h/4., 10, 10)
    glTranslate(0, 0, h/4.)
    glutSolidCone(h/3., h/4., 10, 10)
    glTranslate(0, 0, -h/2.)
    glTranslate(-(x * h - 1), -(y * h - 1), -z)

def drzewko(x, y, z , h):
    glTranslate(x * h - 1, y * h - 1, z)
    glutSolidCylinder(h/4., h/4., 10, 10)
    glTranslate(-(x * h - 1), -(y * h - 1), -z)

def klawiatura(*args):
    if args[0] == '\033' or args[0] == 'q':
        sys.exit()

def mysz(button, state, x, y):
    global action, xStart, yStart
    if (button==GLUT_LEFT_BUTTON):
        if (glutGetModifiers() == GLUT_ACTIVE_SHIFT):
            action = "MOVE_EYE_2"
        else:
            action = "MOVE_EYE"
    elif (button==GLUT_MIDDLE_BUTTON):
        action = "TRANS"
    elif (button==GLUT_RIGHT_BUTTON):
        action = "ZOOM"
    xStart = x
    yStart = y

def ruch(x, y):
    global zoom, xStart, yStart, rot_x, rot_y, rot_z, xTrans, yTrans
    if (action=="MOVE_EYE"):
        rot_x += y - yStart
        rot_y -= x - xStart
    elif (action=="MOVE_EYE_2"):
        rot_z += y - yStart
    elif (action=="TRANS"):
        xTrans += y - yStart
        yTrans += x - xStart
    elif (action=="ZOOM"):
        zoom -= y - yStart
        if zoom > 150.:
            zoom = 150.
        elif zoom < 1.1:
            zoom = 1.1
    else:
        print("unknown action\n", action)
    xStart = x
    yStart = y 
    glutPostRedisplay()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.2, 1.2, -1.2, 1.2, -1.2, 1.2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# rysowanie terenu
def rysuj_teren(w, h):
    for x in range(rozmiar):
        for y in range(rozmiar):
            if type(ziemia[x][y]) is teren.Pustynia:
                glColor3f(1, 1, 0)
                szecian(x, y, 0, h)
            elif type(ziemia[x][y]) is teren.Dzunkla:
                glColor3f(0, 1, 0)
                szecian(x, y, 0, h)
            if ziemia[x][y].energia > 0:
                glColor3f(0, 0.5, 0)
                drzewko(x, y, h, h)

def polar():
    glTranslatef( yTrans/100., 0.0, 0.0 )
    glTranslatef(  0.0, -xTrans/100., 0.0)
    glRotatef( -rot_z, 0.0, 0.0, 1.0)
    glRotatef( -rot_x, 1.0, 0.0, 0.0)
    glRotatef( -rot_y, .0, 1.0, 0.0)

def wyswietlanie():
    global zoom, maxzoom, minzoom, rot_x, rot_y, rot_z

    glutPostRedisplay()
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt (0, 0, eyesz, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(zoom, 1, maxzoom, minzoom)
    glMatrixMode(GL_MODELVIEW)
    polar()
    rysuj()

def rysuj():
    global dzien
    h = 2. / rozmiar
    w = 2. / rozmiar

    glPushMatrix()
    rysuj_teren(w, h)
    teren.tworzenie_lasow(ziemia)

    for krolik in lista_zwierzat:
        krolik.rusz_sie(rozmiar)

        glColor3f((krolik.energia % 100.) / 100., 0, 0)
        szecian(krolik.x, krolik.y, h, h)

    for krolik in lista_zwierzat:
        krolik.zycie_jest_nowela(lista_zwierzat, ziemia)

    f.write(repr(len(lista_zwierzat)))
    f.write('\n')
    dzien += 1

    glPopMatrix()
    glFlush()

    if len(lista_zwierzat) == 0:
        f.close()
        sys.exit()

# OpenGL
glutInit()
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
glutCreateWindow("Window")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
init()
glutDisplayFunc(wyswietlanie)
glutKeyboardFunc(klawiatura)
glutMouseFunc(mysz)
glutMotionFunc(ruch)
glutReshapeFunc(reshape)
glClearColor(1.0, 1.0, 1.0, 0.0)
glutMainLoop()
