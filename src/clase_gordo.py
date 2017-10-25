import CargaImagen
import pygame

class gordo(object):
    animation_number = 0
    gordo_list = CargaImagen.gordo_list
    counter = 0
    current = CargaImagen.gordo_list[animation_number]
    x = 0
    y = 0

    def player_init(self):
        self.animation()
        self.movement()
    def __init__(self, x, y):
        self.x = x
        self.y = y

