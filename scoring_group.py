#!/usr/bin/env python3

from die import Die
from collections import Counter

class ScoringGroup:
	def __init__(self, dice = []):
		self.dice = dice
		self.group_score = None
		self.all_dice_consumed = False
		self.child_groups = []
		
	def __repr__(self):
		return str(self.dice)
	
	def num_dice(self):
		return len(self.dice)
	
	def remove_dice(self, to_remove):
		print(self.dice)
		for i in range(to_remove[1]):
			try:
				self.dice.remove(to_remove[0])
			except :
				print(f'Error! Cannot remove die {to_remove[0]} because it is not there')
			
	def score(self):
		counts = list(Counter(self.dice).items())
		print(counts)
		
		# We'll always take a combination made from 6
		if self.num_dice() == 6:
			# Check for 6 of a kind
			if len(counts) == 1:
				print('6 of a kind')
				self.group_score = 3000
				
			# Check for 2 triplets
			elif all(value[1] == 3 for value in counts):
				print('2 triplets')
				self.group_score = 2500
			
			# Check for 3 pairs
			elif all(value[1] == 2 for value in counts):
				print('3 pairs')
				self.group_score = 1500

			# Check for 1-6 run
			elif all(value[1] == 1 for value in counts):
				print('1-6 run')
				self.group_score = 1500
			
			# Check for 4 of a kind with pair
			elif counts[0][1] == 4 and counts[1][1] == 2:
				print('4 of a kind and a pair')
				self.group_score = 1500
			
			self.all_dice_consumed = True
			return
				
		
		# Check for 5 of a kind
		if self.num_dice() >= 5:
			if counts[0][1] == 5:
				print('5 of a kind')
				self.group_score = 2000
				# TODO
		
		# Check for 4 of a kind
		if self.num_dice() >= 4:
			if counts[0][1] == 4:
				print('4 of a kind')
				self.group_score = 1000
				# TODO
		
		# Check for 3 of a kind
		if self.num_dice() >= 3:
			if counts[0][1] == 3:
				print('3 of a kind')
				if counts[0][0] == 1:
					self.group_score = 300
				else:
					self.group_score = 100 * counts[0][0].value
				# TODO
		
		# Check for 1s
		ones = self.dice.count(Die(1))
		if ones > 0:
			print(f'{ones} 1s')
			self.group_score = 100 * ones
			# TODO
			
		# Check for 5s
		fives = self.dice.count(Die(5))
		if fives > 0:
			print(f'{fives} 5s')
			self.group_score = 50 * fives
			# TODO
		
		print('done scoring')