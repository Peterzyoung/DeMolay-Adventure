import pygame, os

tiles = {}
def init():
	os.chdir(os.getcwd()+"\Assets")

def load_assets():
	global tiles
	for n in os.listdir(os.getcwd()):
		pass

class Tile(object):
	def __init__(self):
		self.img = None
		self.solid = False
		self.portal = None
		self.effects = []

class Map(object):
	def __init__(self, width, height):
		self.grid = [[Tile()]]
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

def Main():

if __name__ =="" __main__": main()
