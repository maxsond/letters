# Here's where we calculate motivations and events 
# based on the situations of the characters

import random

def __init__(self):
	pass

"""
Initializes relationships between characters.

Right now starting relationships have the following characteristics:
Max Value: 8
Min Value: 0
Distribution: 2d5 - 2
"""

def init_relations(roster):
	for person in roster:
		for target in roster:
			if target != person:
				relation = random.randint(1,5) + random.randint(1,5) - 2
				roster[person]['relations'][target] = relation
'''			
				print "%s's relation towards %s is %s" % (
				roster[person]['name'],
				roster[target]['name'],
				roster[person]['relations'][target])
'''
				
class Calendar(object):
	
	def __init__(self):
		self.year = {}
		self.month = {}
		self.week = {}
		self.day = {}

cal = Calendar()
	