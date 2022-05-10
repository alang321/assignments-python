import pygame as pg

pg.init()

scr_width = 800
scr_height = 800

reso = (scr_width, scr_height)
scr = pg.display.set_mode(reso)

paddle_pos = [scr_width / 2, scr_height - 20]
paddle_vel = 100

ball_pos = [scr_width/2 + 30, scr_width/2]
ball_vel = [600, 600]

grid_rows = 8
grid_cols = 14
grid_row_hitpoints = [1, 1, 1, 1, 1, 1, 1, 1]

grid = [[grid_row_hitpoints[i]] * grid_cols for i in range(grid_rows)]

grid[0][0] = 0
print(grid)
