import pygame

from const import *


class Dragger:

	def __init__(self):
		self.mouseX = 0
		self.mouseY = 0
		self.initial_row = 0
		self.initial_col = 0
		self.piece = 0
		self.dragging = False

	# blit method

	def update_blit(self, surface, images):
		img_center = self.mouseX, self.mouseY
		look_1 = images.get(self.piece).convert_alpha()
		look_1 = pygame.transform.smoothscale(look_1, (80, 80))
		texture_rect = look_1.get_rect(center=img_center)
		surface.blit(look_1, texture_rect)

	# other methods

	def update_mouse(self, pos):
		self.mouseX, self.mouseY = pos

	def save_initial(self, pos):
		self.initial_row = pos[1] // SQSIZE
		self.initial_col = pos[0] // SQSIZE

	def drag_piece(self, piece):
		self.piece = piece
		self.dragging = True

	def undrag_piece(self):
		self.piece = 0
		self.dragging = False