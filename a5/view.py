import math

import pygame as pg
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

def openwindow(xmax, ymax):
    """ Init pygame, set up window, return scr (window Surface) """
    reso = (xmax, ymax)
    scr = pg.display.set_mode(reso)
    return scr

def processevents():
    """ Let PyGame process events, and detect keypresses. """
    keys = pg.key.get_pressed()
    up = keys[pg.K_UP]
    down = keys[pg.K_DOWN]
    w = keys[pg.K_w]
    s = keys[pg.K_s]
    left = keys[pg.K_LEFT]
    right = keys[pg.K_RIGHT]
    f = keys[pg.K_f]
    g = keys[pg.K_g]
    b = keys[pg.K_b]
    q = keys[pg.K_b]

    dalpha = 0  # -1 or 0 or 1
    if up:
        dalpha = 1
    if down:
        dalpha = -1

    dthrottle = 0 # -1 or 0 or 1
    if w:
        dthrottle = 1
    if s:
        dthrottle = -1

    dflaps = 0 # -1 or 0 or 1
    if left:
        dthrottle = 1
    if right:
        dthrottle = -1

    gearpressed = g # True or False
    brakepressed = b # True or False
    userquit = q # True or False

    return dalpha, dthrottle, dflaps, gearpressed, brakepressed, userquit


def clr(scr):
    """Clears surface, fill with black"""
    scr.fill(white)
    return


def flip():
    """Flip (update) display"""
    pg.display.flip()
    return


def closewindow():
    """Close window, quit pygame"""
    pg.quit()
    return


def elev2y(elev, ymax, minelev, maxelev):
    """Scale an elevation angle to y-pixels"""
    y = ymax - ymax * (elev - minelev) / (maxelev - minelev)
    return y


def azi2x(azi, xmax, minazi, maxazi):
    """Scale an azimuth angle to x-pixels"""
    x = xmax * (azi - minazi) / (maxazi - minazi)
    return x


def drawhor(scr, theta, xmax, ymax, minelev, maxelev):
    """Draw horizon for pitch angle theta[deg]"""
    theta *= -1
    theta = min(max(theta, minelev), maxelev)
    y = elev2y(theta, ymax, minelev, maxelev)

    pg.draw.line(scr, black, (0, y), (xmax, y))
    return

def drawrunway(scr, theta, x, y, xmax, ymax, minazi, maxazi, minelev, maxelev):
    w = 60
    l = 3000
    dist0 = (y**2 + x**2)**0.5
    dist1 = (y**2 + (abs(x) + l)**2)**0.5
    dazi0 = max(min(math.degrees(math.atan(1/2*w/dist0)), maxazi), minazi)
    dazi1 = max(min(math.degrees(math.atan(1/2*w/dist1)), maxazi), minazi)
    elev0 = -theta - math.atan(y/-x)
    elev1 = -theta - math.atan(y/(-x + l))
    xc = azi2x(0, xmax, minazi, maxazi)
    y0 = elev2y(elev0, ymax, minelev, maxelev)
    y1 = elev2y(elev1, ymax, minelev, maxelev)
    dx0 = xmax * dazi0/(maxazi-minazi)
    dx1 = xmax * dazi1/(maxazi-minazi)
    A = (xc - dx0, y0)
    B = (xc + dx0, y0)
    C = (xc + dx1, y1)
    D = (xc - dx1, y1)
    pg.draw.line(scr, black, A, B)
    pg.draw.line(scr, black, B, C)
    pg.draw.line(scr, black, C, D)
    pg.draw.line(scr, black, D, A)