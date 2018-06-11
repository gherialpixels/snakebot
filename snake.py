import time, random, os, sys

import pygame
from pygame.locals import *

WIDTH = 400
HEIGHT = 400

class Snake(object):
	def __init__(self, n):
		self.snake_length = n
		self.tail = [[random.randint(0, 19), random.randint(0, 19)]]
		self.score = 0

		for i in range(self.snake_length - 1):
			self.tail.append([self.tail[0][0], self.tail[0][1] - (i + 1)])


	def _move(self):
		for i in range(self.snake_length - 1, 0, -1):
			self.tail[i][0] = self.tail[i - 1][0]
			self.tail[i][1] = self.tail[i - 1][1]
			"""
			tail[4] = tail[3]
			tail[5] = tail[4]
			"""

	def _move_head(self, direction):
		self.tail[0][0] += direction[0]
		self.tail[0][1] += direction[1]

	def _update(self, direction):
		self._move_head(direction)
		self._move()
		if self.tail[0][0] < 0:
			self.tail[0][0] = 19
		elif self.tail[0][0] > 19:
			self.tail[0][0] = 0
		elif self.tail[0][1] < 0:
			self.tail[0][1] = 19
		elif self.tail[0][1] > 19:
			self.tail[0][1] = 0

	def _munch(self, food):
		if food[0] == self.tail[0][0] and food[1] == self.tail[0][1]:
			self.snake_length += 1
			self.tail.append([(self.tail[-1][0] - self.tail[-2][0]) + self.tail[-1][0], \
			(self.tail[-1][1] - self.tail[-2][1]) + self.tail[-1][1]])
			self.score += 1
			return True

	def _collide(self):
		if self.tail[0] in self.tail[2:]:
			return True

def planting(orm):
	spot = [random.randint(0, 19), random.randint(0, 19)]
	while spot in orm.tail:
		spot = [random.randint(0, 19), random.randint(0, 19)]

	return spot

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 100, 100))
clock = pygame.time.Clock()

gs = 20
direction = [1, 0]

s = Snake(5)

default_size = (gs - 3, gs - 3)
snake_img = pygame.Surface(default_size)
food_img = pygame.Surface(default_size)

snake_img.fill((255, 255, 255))
food_img.fill((255, 200, 50))

food_pos = planting(s)

while 1:
	clock.tick(20)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()
		elif event.type == KEYDOWN:
			if event.key == K_DOWN:
				if direction == [0, -1]:
					break
				direction = [0, 1]
			elif event.key == K_UP:
				if direction == [0, 1]:
					break
				direction = [0, -1]
			elif event.key == K_RIGHT:
				if direction == [-1, 0]:
					break
				direction = [1, 0]
			elif event.key == K_LEFT:
				if direction == [1, 0]:
					break
				direction = [-1, 0]

	s._update(direction)
	if s._munch(food_pos):
		food_pos = planting(s)
	if s._collide():
		print "You have failed! Score: " + str(s.score)
		pygame.quit()
		quit()
	background.fill((100, 100, 100))
	for i in range(len(s.tail)):
		background.blit(snake_img, (s.tail[i][0] * gs, \
 										s.tail[i][1] * gs))


	background.blit(food_img, (food_pos[0] * gs, food_pos[1] * gs))

	screen.blit(background, (0, 0))
	pygame.display.update()
