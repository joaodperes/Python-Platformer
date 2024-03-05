import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from platformer import flip, load_sprite_sheets, Object, Block, Fire, Checkpoint

WIDTH, HEIGHT = 1000, 800

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

block_size = 96

fire1 = Fire(block_size * 3, HEIGHT - block_size - 64, 16, 32)
fire2 = Fire(block_size * 3.5, HEIGHT - block_size - 64, 16, 32)
#fire3 = [Fire(j * block_size, HEIGHT - block_size - 64, 16, 32) for j in range (1, 9)]
flame = fire1, fire2

checkpoint = Checkpoint(((2 * WIDTH // block_size) * block_size) - 3 * block_size, HEIGHT - (2 * block_size) - 32, 64, 64)

rwall = [Block(((2 * WIDTH // block_size) * block_size) - block_size, (h * block_size) +  (HEIGHT % block_size), block_size) for h in range (-block_size, (HEIGHT - block_size)//block_size)]
lwall = [Block((-WIDTH // block_size) * block_size, (k * block_size) +  (HEIGHT % block_size), block_size) for k in range (-block_size, (HEIGHT - block_size)//block_size)]
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range (-WIDTH // block_size, WIDTH * 2 // block_size)]
block = Block(0, HEIGHT - block_size, block_size)

objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size), Block(block_size * 3, HEIGHT - block_size * 4, block_size), *flame, *rwall, *lwall, checkpoint]
