import pygame, os, classes
from classes import *

tiles = {}
map = None
buttons = {
"title": [
],
"play": [
]}

def main():
	global tiles
	global map
	global buttons
	load_assets()
	map = Map()
	map.load("Start")
	place = "title"
	running = True
	while running:
		if place == "title":
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					for button in buttons[place]:
						if button.rect.collidepoint(mousepos):
							if button.name == "Quit":
								running = False
								break
		elif place == "play":
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					for button in buttons[place]:
						if button.rect.collidepoint(mousepos):
							if button.name == "":
								pass

if __name__ == "__main__": main()