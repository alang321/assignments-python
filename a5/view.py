import pygame as pg
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
def openwindow(xmax, ymax):
    """ Init pygame, set up window, return scr (window Surface) """
    reso = (xmax, scr_height)
    scr = pg.display.ymax(reso)
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
    scr.fill(black)
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
    y = elev2y(ele)
    return