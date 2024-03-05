import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from platformer import flip, load_sprite_sheets, get_block, Object, Block, Fire

WIDTH, HEIGHT = 1000, 800

block_size = 96

fire1 = Fire(block_size * 3, HEIGHT - block_size - 64, 16, 32)
fire2 = Fire(block_size * 3.5, HEIGHT - block_size - 64, 16, 32)
fire3 = [Fire(j * block_size, HEIGHT - block_size - 64, 16, 32) for j in range (3, 6)]
flame = fire1, fire2

floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range (-WIDTH // block_size, WIDTH * 2 // block_size)]
block = [Block(0, HEIGHT - block_size, block_size)]

objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size), Block(block_size * 3, HEIGHT - block_size * 4, block_size), *flame, *fire3]