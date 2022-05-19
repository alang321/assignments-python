import view # file with your otwv drawing functions
# Size of window
xmax = 1000 #[pixels] window width (= x-coordinate runs of right side right+1)
ymax = 700 #[pixels] window height(= y-coordinate of lower side of window+1)
# Size of viewport (angles in degrees)
minelev = -14.0 #[deg] elevation angle lower side
maxelev = 14.0 #[deg] elevation angle top side
minazi = -20.0 #[deg] azimuth angle left side
maxazi = 20.0 #[deg] azimuth angle right side
# Set pitch angle
theta = float(input("Enter pitch angle[deg]:")) # pitch angle [deg]
# Set up window, scr is surface of screen
scr = view.openwindow(xmax, ymax)
running = True
while running:
    # Clear screen scr
    view.clr(scr)
    # Get user inputs by processing events
    dalpha, dthrottle, dflaps, gearpressed, brakepressed, userquit = view.processevents()
    # Draw horizon on scr, using pitch angle theta, and screen dimensions
    view.drawhor(scr, theta, xmax, ymax, minelev, maxelev)
    # Update screen
    view.flip()
    if userquit:
        running = False

# Close window
view.closewindow()
