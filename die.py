#!/usr/bin/env python3

import random

class Die:	
	def __init__(self, value = 0):
		if value == 0 or not 1 <= value <= 6:
			self.value = random.randint(1, 6)
		else:
			self.value = value
		
	def __repr__(self):
		return str(self.value)
	
	def __eq__(self, other):
		if isinstance(other, Die):
			return self.value == other.value
		return False
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __lt__(self, other):
		if isinstance(other, Die):
			return self.value < other.value
	
	def __gt__(self, other):
		if isinstance(other, Die):
			return self.value > other.value
		
	def __hash__(self):
		return hash(self.value)