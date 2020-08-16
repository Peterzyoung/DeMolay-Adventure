import pygame, os

def init():
	os.chdir(os.getcwd()+"\Assets")
	load_assets()

def load_assets():
	global tiles
	for n in os.listdir(os.getcwd()+"\tiles"):
		tiles[n[:-4]] = pygame.image.load(os.path.join(os.getcwd()+"\marks",str(n))).convert()

def load_menus():
	global buttons
	buttons["title"] = [
	Button("Play","c",80)]
	

class Tile(object):
	def __init__(self):
		self.img = None
		self.solid = False
		self.portal = None
		self.effects = []

class Map(object):
	def __init__(self,width,height):
		self.grid = [[Tile()]]
		self.lighting = 0
	def load(self,name):
		self.complete = []
		row = []
		set = []
		chunk = ""
		file = open("maps.txt","r")
		data = ""
		for line in file:
			if line[:-1] == name:
				data = file.readline()
				break
		file.close()
		if data == "":
			return "map not found"
		section = 0
		for character in data:
			if character == "#":
				if section == 0:
					self.complete.append(set[0])
				else:
					self.complete.append(set)
				section += 1
			elif character == "&"
				set.append(row)
				row = []
			elif character == "$":
				try:
					chunk = int(chunk)
				except:
					pass
				row.append(chunk)
				chunk = ""
			else:
				chunk += character
		self.prepare()
	def prepare(self):
		global tiles
		for y, row in enumerate(self.complete[1]):
			for x, item in enumerate(row):
				self.grid[y][x].img = tiles[self.complete[0][item]]
				self.grid[y][x].solid = bool(self.complete[2][y][x])


class Button(object):
	def __init__(self,name,x,y,font="gabriola",size=22,color=(254,254,254),highlight=(200,200,200),border=False):
		self.name = name
		self.font = pygame.font.SysFont(font,size)
		text = self.font.render(name, 0, (color))
		self.img = pygame.Surface((text.width+20,text,height+20))