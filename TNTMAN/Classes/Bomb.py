import sys
import os
import pygame
import TNTMan


class Bomb():
    def __init__(self):
        self.bomb_pos = TNTMan.TNTMan.get_position()
        self.cant_bombs = 3