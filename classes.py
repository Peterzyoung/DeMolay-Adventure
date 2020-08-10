import pygame

class Tile(object):
	def __init__(self):
			self.img = 0

class Map(object):
	def __init__(self, width, height):
		self.grid = [[0]*width]*height
		self.tilenames = []
	def load(self, name):
		file = open("maps.txt","r")
		data = ""
		for line in file:
				if line == name:
						data = file.readline()
						break
		if data == "":
			return
		section = 0
		chunk = ""
		for character in data:
				if character == "&":
					section += 1
				elif character == "$":
					if section == 1:
						self.tilenames.append(chunk)
						chunk = ""
				else:
					chunk += character
