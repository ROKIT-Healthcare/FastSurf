import numpy as np
import torch

def get_scene_bounds(scene_name, voxel_size, sc_factor=1, interp=False):

    if scene_name == 'scene0000':
        x_min, x_max = -4.8, 4.8
        y_min, y_max = -0.4, 4.4
        z_min, z_max = -4.8, 4.8

    elif scene_name == 'scene0002':
        x_min, x_max = -2.4, 2.4
        y_min, y_max = -0.2, 3.0
        z_min, z_max = -2.4, 2.4

    elif scene_name == 'scene0005':
        x_min, x_max = -2.76, 2.84
        y_min, y_max = -0.2, 1.8
        z_min, z_max = -2.44, 3.16

    elif scene_name == 'scene0012':
        x_min, x_max = -3, 3
        y_min, y_max = -0.25, 2.75
        z_min, z_max = -3, 3

    elif scene_name == 'scene0050':
        x_min, x_max = -2.0, 2.0
        y_min, y_max = 0.0, 3.2
        z_min, z_max = -2.0, 2.0

    elif scene_name == 'scene0054':
        x_min, x_max = -2.8, 2.8
        y_min, y_max = -0.6, 2.8
        z_min, z_max = -2.8, 2.8

    elif scene_name == 'whiteroom':
        x_min, x_max = -4.8, 4.0
        y_min, y_max = -5.2, 3.6
        z_min, z_max = -3.2, 3.2

    elif scene_name == 'kitchen':
        x_min, x_max = -4.0, 5.2
        y_min, y_max = -5.2, 4.0
        z_min, z_max = -3.2, 4.0

    elif scene_name == 'breakfast_room':
        x_min, x_max = -2.5, 2.5
        y_min, y_max = -2.25, 2.25
        z_min, z_max = -2.5, 2.75

    elif scene_name == 'staircase':
        x_min, x_max = -4.8, 4.4
        y_min, y_max = -4.4, 4.8
        z_min, z_max = -3.2, 4.8

    elif scene_name == 'icl_living_room':
        x_min, x_max = -2.75, 2.75
        y_min, y_max = -2.75, 2.75
        z_min, z_max = -3.2, 2.0

    elif scene_name == 'complete_kitchen':
        x_min, x_max = -6, 6
        y_min, y_max = -4.5, 4.5
        z_min, z_max = -3, 3

    elif scene_name == 'green_room':
        x_min, x_max = -3.4, 3.4
        y_min, y_max = -4.4, 4.4
        z_min, z_max = -3.2, 2.4

    elif scene_name == 'grey_white_room':
        x_min, x_max = -2.48, 2.48
        y_min, y_max = -3.32, 3.32
        z_min, z_max = -2.24, 3.2

    elif scene_name == 'morning_apartment':
        x_min, x_max = -1.72, 1.72
        y_min, y_max = -2.0, 1.88
        z_min, z_max = -1.5, 1.5

    elif scene_name == 'thin_geometry':
        x_min, x_max = -4.2, 1.2
        y_min, y_max = -2.4, 0.75
        z_min, z_max = -1.0, 3.8

    else:
        x_min, x_max = -1.0, 1.0
        y_min, y_max = -1.0, 1.0
        z_min, z_max = -1.0, 1.0


    if interp:
        x_min = x_min - 0.5 * voxel_size
        y_min = y_min - 0.5 * voxel_size
        z_min = z_min - 0.5 * voxel_size

        x_max = x_max + 0.5 * voxel_size
        y_max = y_max + 0.5 * voxel_size
        z_max = z_max + 0.5 * voxel_size

    x_min = sc_factor * x_min
    x_max = sc_factor * x_max
    y_min = sc_factor * y_min
    y_max = sc_factor * y_max
    z_min = sc_factor * z_min
    z_max = sc_factor * z_max
    
    Nx = round((x_max - x_min) / voxel_size + 0.0005)
    Ny = round((y_max - y_min) / voxel_size + 0.0005)
    Nz = round((z_max - z_min) / voxel_size + 0.0005)

    tx = torch.linspace(x_min, x_max, Nx + 1)
    ty = torch.linspace(y_min, y_max, Ny + 1)
    tz = torch.linspace(z_min, z_max, Nz + 1)

    return tx, ty, tz
