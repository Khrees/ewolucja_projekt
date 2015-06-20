__author__ = 'illmoded'

from OpenGL.GL import *
from OpenGL.GLUT import *

import zwierza
import teren

dzien = 0
rozmiar = 100
poczatkowa_liczba_zwierzat = 50

ziemia = teren.generuj_teren(rozmiar)
listazwieraat = zwierza.generuj_zwierzeta(poczatkowa_liczba_zwierzat, rozmiar)


# rysowanie terenu
def rysuj_teren(w, h):
    for x in range(rozmiar):
        for y in range(rozmiar):
            if type(ziemia[x][y]) is teren.Pustynia:
                glColor3f(1, 1, 0)
                glBegin(GL_POLYGON)
                glVertex2f(x * w - 1, y * h - 1)
                glVertex2f(x * w + w - 1, y * h - 1)
                glVertex2f(x * w + w - 1, y * h + h - 1)
                glVertex2f(x * w - 1, y * h + h - 1)
                glVertex2f(x * w - 1, y * h - 1)
                glEnd()
            elif type(ziemia[x][y]) is teren.Dzunkla:
                glColor3f(0, 1, 0)
                glBegin(GL_POLYGON)
                glVertex2f(x * w - 1, y * h - 1)
                glVertex2f(x * w + w - 1, y * h - 1)
                glVertex2f(x * w + w - 1, y * h + h - 1)
                glVertex2f(x * w - 1, y * h + h - 1)
                glEnd()
            if ziemia[x][y].energia > 0:
                glColor3f(0, 0, 0)
                glBegin(GL_LINES)
                glVertex2f(x * w - 1, y * h - 1)
                glVertex2f(x * w + w - 1, y * h + h - 1)
                glEnd()
                glBegin(GL_LINES)
                glVertex2f(x * w + w - 1, y * h - 1)
                glVertex2f(x * w - 1, y * h + h - 1)
                glEnd()
    pass


def wyswietlanie():
    global dzien
    glutPostRedisplay()
    glClear(GL_COLOR_BUFFER_BIT)

    h = 2. / rozmiar
    w = 2. / rozmiar

    rysuj_teren(w, h)
    teren.tworzenie_lasow(rozmiar, ziemia)

    for krolik in listazwieraat:
        krolik.rusz_sie(rozmiar)

        glColor3f((krolik.energia % 100.) / 100., 0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(krolik.x * w - 1, krolik.y * h - 1)
        glVertex2f(krolik.x * w + w - 1, krolik.y * h - 1)
        glVertex2f(krolik.x * w + w - 1, krolik.y * h + h - 1)
        glVertex2f(krolik.x * w - 1, krolik.y * h + h - 1)
        glEnd()

    for krolik in listazwieraat:
        krolik.zycie_jest_nowela(rozmiar, listazwieraat, ziemia)

    print(len(listazwieraat))
    dzien += 1

    glFlush()

    if len(listazwieraat) == 0:
        sys.exit()

# OpenGL
glutInit()
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
glutCreateWindow("Window")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutDisplayFunc(wyswietlanie)
glClearColor(1.0, 1.0, 1.0, 0.0)
glutMainLoop()
