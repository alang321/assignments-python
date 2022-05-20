import view # file with your otwv drawing functions
import pygame as pg
import math
# Size of window
xmax = 1000 #[pixels] window width (= x-coordinate runs of right side right+1)
ymax = 700 #[pixels] window height(= y-coordinate of lower side of window+1)
# Size of viewport (angles in degrees)
minelev = -14.0 #[deg] elevation angle lower side
maxelev = 14.0 #[deg] elevation angle top side
minazi = -20.0 #[deg] azimuth angle left side
maxazi = 20.0 #[deg] azimuth angle right side
# Set pitch angle
#theta = float(input("Enter pitch angle[deg]:")) # pitch angle [deg]
# Set up window, scr is surface of screen
scr = view.openwindow(xmax, ymax)
running = True

gamma = -3 # deg
alpha = -5 # deg
V = 113.178 # m/s
x = -3000 # m
y = 2000 # m


clock = pg.time.Clock()
dt = 0
while running:
    # Clear screen scr
    view.clr(scr)
    # Get user inputs by processing events
    dalpha, dthrottle, dflaps, gearpressed, brakepressed, userquit = view.processevents()

    theta = alpha + gamma
    v_x = V * math.cos(math.radians(gamma))
    v_y = V * math.sin(math.radians(gamma))

    x += v_x * dt
    y += v_y * dt

    if x >= 0:
        break

    # Draw horizon on scr, using pitch angle theta, and screen dimensions
    view.drawhor(scr, theta, xmax, ymax, minelev, maxelev)
    view.drawrunway(scr, theta, x, y, xmax, ymax, minazi, maxazi, minelev, maxelev)
    # Update screen
    view.flip()
    pg.event.pump()
    if userquit:
        running = False

    dt = min(clock.tick(60) / 1000, 0.1)

# Close window
view.closewindow()
