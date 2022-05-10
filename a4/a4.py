import pygame as pg

pg.init()

SCR_COLOR = (0, 0, 0)
GRID_COLOR = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 000)]
BALL_COLOR = (255, 255, 255)
PADDLE_COLOR = (255, 255, 255)

scr_width = 500
scr_height = 800

reso = (scr_width, scr_height)
scr = pg.display.set_mode(reso)

paddle_pos = [scr_width / 2, scr_height - 20]
paddle_vel = 150 # pixels per sec
paddle_lim = [50, scr_width - 50]
paddle_rect = pg.Rect(0, 0, 50, 6)

ball_pos = [scr_width/2 + 30, scr_height/2]
ball_vel = [300, 300]
ball_rad = 4
ball_surface = pg.Surface((ball_rad * 2, ball_rad * 2))
pg.draw.circle(ball_surface, BALL_COLOR, (ball_rad, ball_rad), ball_rad)
ball_rect = ball_surface.get_rect()

grid_rows = 8
grid_cols = 14
grid_row_hitpoints = [4, 4, 3, 3, 2, 2, 1, 1]

grid_margin_t = 50
#dimension of grid elements, width is determined by math from cols
grid_elem_h = 10
grid_elem_w = scr_width / grid_rows
grid_hitpoints = [[grid_row_hitpoints[i]] * grid_cols for i in range(grid_rows)]

grid_rects = [[[]] * grid_cols for i in range(grid_rows)]
for row_idx in range(len(grid_rects)):
    for col_idx in range(len(grid_rects[row_idx])):
        pos_y = grid_margin_t + row_idx * grid_elem_h
        pos_x = col_idx * (grid_elem_w)
        grid_rects[row_idx][col_idx] = pg.Rect(pos_x, pos_y, grid_elem_w, grid_elem_h)

tick_0 = 0.001 * pg.time.get_ticks()
escape = False

clock = pg.time.Clock()
dt = 0
while not escape:
    # Check for key or quit event:
    keys = pg.key.get_pressed()
    escape = keys[pg.K_ESCAPE]
    left = keys[pg.K_LEFT]
    right = keys[pg.K_RIGHT]

    # And check if the window close button is clicked
    pg.event.pump()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            escape = True

    # update paddle pos
    if left and not right:
        paddle_pos[0] = max(paddle_lim[0], paddle_pos[0] - paddle_vel * dt)
    elif right and not left:
        paddle_pos[0] = min(paddle_lim[1], paddle_pos[0] + paddle_vel * dt)

    # update ball pos
    for i in range(2):
        ball_pos[i] += ball_vel[i] * dt
    # wall collision ball
    # sides
    if ball_pos[0] + ball_rad >= scr_width:
        intrusion_depth = scr_width - ball_pos[0] - ball_rad
        ball_vel[0] = - ball_vel[0]
        ball_pos[0] = scr_width - intrusion_depth - ball_rad - 1
    if ball_pos[0] - ball_rad <= 0:
        intrusion_depth = ball_pos[0] - ball_rad
        ball_vel[0] = - ball_vel[0]
        ball_pos[0] = intrusion_depth + ball_rad + 1
    #top bottom
    if ball_pos[1] + ball_rad >= scr_height:
        intrusion_depth = scr_height - ball_pos[1] - ball_rad
        ball_vel[1] = -ball_vel[1]
        ball_pos[1] = scr_height - intrusion_depth - ball_rad - 1
    if ball_pos[1] - ball_rad <= 0:
        intrusion_depth = ball_pos[1] - ball_rad
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] = intrusion_depth + ball_rad + 1
    #grid



    # draw
    paddle_rect.centerx = paddle_pos[0]
    paddle_rect.centery = paddle_pos[1]
    ball_rect.centerx = ball_pos[0]
    ball_rect.centery = ball_pos[1]
    scr.fill(SCR_COLOR)
    scr.blit(ball_surface)
    pg.draw.rect(scr, PADDLE_COLOR, paddle_rect)

    # draw grid
    for row_idx, row_hitpoints in enumerate(grid_hitpoints):
        for col_idx, hitpoints in enumerate(row_hitpoints):
            if hitpoints != 0:
                color_idx = min(hitpoints, len(GRID_COLOR)) - 1
                pg.draw.rect(scr, GRID_COLOR[color_idx], grid_rects[row_idx][col_idx])
                pg.draw.rect(scr, (0,0,0), grid_rects[row_idx][col_idx],1)

    pg.display.flip()

    #time keeping, max framerate of 60, otherwise game is slowed down
    dt = min(clock.tick(60)/1000, 0.1)
