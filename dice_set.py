#!/usr/bin/env python3

from die import Die

class DiceSet:
	def __init__(self):
		self.d1 = Die()
		self.d2 = Die()
		self.d3 = Die()
		self.d4 = Die()
		self.d5 = Die()
		self.d6 = Die()
		
	def __repr__(self):
		return f'{self.d1} {self.d2} {self.d3} {self.d4} {self.d5} {self.d6}'
	