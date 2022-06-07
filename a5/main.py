import view # file with your otwv drawing functions
import pygame as pg
import math
import isa

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

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
alpha = 3 # deg
V = 113.178 # m/s
x = -3000 # m
y = 200 # m

# Model parameters
mzerofuel = 40000.0 #[kg] mass aircraft + payload excl fuel
mfuel = 5000.0 # [kg]
S = 102.0 #[m2]
Tmax = 200 * 1e3 #[N]
CT = 17.8 * 1e6 # [kg/Ns] kg/s per N thrustSpecific fuel consumption
rho = 1.225 # [kg/m3] air density (constant or use ISA)
g = 9.81 # [m/s2] gravitational constant
throttledot = 0.1 # [1/s] throttle speed (spool up/down speed)
alphadot = 1.0 # [deg/s] alpha change due to control
flapsdot = 0.2 # [1/s] flap deflection speed
alphamin = -10.0 # [deg]
alphamax = 20.0 # [deg]

dflaps = 0
dgear = 0
dbrake = 0
dthrottle = 0

displaytext = 0

clock = pg.time.Clock()
dt = 0
while running:
    # Clear screen scr
    view.clr(scr)
    # Get user inputs by processing events
    change_alpha, change_throttle, change_flaps, gearpressed, brakepressed, userquit = view.processevents()

    alpha = clamp(alpha + dt * alphadot * change_alpha, alphamin, alphamax)
    dflaps = clamp(dflaps + dt * flapsdot * change_flaps, 0, 1)
    dthrottle = clamp(dthrottle + dt * throttledot * change_throttle, 0, 1)

    cl, cd = view.CLCD(alpha, dflaps, dgear, dbrake)
    L = cl * 0.5 * rho * V**2 * S
    D = cd * 0.5 * rho * V**2 * S
    T = dthrottle * Tmax
    m_dot_fuel = -CT * T
    mfuel -= m_dot_fuel
    m = mzerofuel + mfuel
    W = m * g

    dvdt = (T*math.cos(math.radians(alpha)) - D - W * math.sin(math.radians(gamma)))/m
    dgdt = (T*math.sin(math.radians(alpha)) + L - W * math.cos(math.radians(gamma)))/m/V

    V = V + dvdt * dt
    gamma = gamma + dgdt * dt

    theta = alpha + gamma
    v_x = V * math.cos(math.radians(gamma))
    v_y = V * math.sin(math.radians(gamma))

    x += v_x * dt
    y += v_y * dt
    Temp, p, rho = isa.getIsa(y)

    if x >= 0 or y < 0:
        print("x:", x, "y:", y)
        break

    # Draw horizon on scr, using pitch angle theta, and screen dimensions
    view.drawhor(scr, theta, xmax, ymax, minelev, maxelev)
    view.drawrunway(scr, theta, x, y, xmax, ymax, minazi, maxazi, minelev, maxelev)
    # Update screen
    view.flip()

    displaytext += dt
    if displaytext > 0.5:
        displaytext = 0
        print(dthrottle, alpha, dflaps, x, y)
    pg.event.pump()
    if userquit:
        print("userquit")
        running = False

    dt = clock.tick(120) / 1000

# Close window
view.closewindow()
