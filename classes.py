import pygame

class Map(object):
	def __init__(width,height):
		self.grid = [[0]*width]*height