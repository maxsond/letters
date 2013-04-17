class ParserError(Exception):
	pass

import storyteller

class Character(object):

	def __init__(self, gender, name):
		self.gender = gender
		self.name = name
		self.relationship = {}
		self.health = {}
		self.wealth = {}
		self.career = {}

def populate(playbill):
	playbill = open(playbill, 'r')
	global actorname 

#Could refactor to remove 'details' list if necessary.
	global roster
	roster = {}
	for line in playbill:
#		print line.split()
		details = []
		details = line.split()
#		print details
		if details != []:
			gender = details.pop()
			actorname = details.pop()
#			print actorname
#			print gender
			roster[actorname] = Character(gender, actorname)
#			roster[str(actorname)]['name'] = actorname
#			roster[str(actorname)]['gender'] = gender
#	for member in roster:
#		print "%s's gender is %s" % (roster[member]['name'], roster[member]['gender'])

#	print'\n'	
#	print "***For debugging purposes only!***"
#	print Gertrude.gender
#	print Lewis.gender
#	storyteller.init_relations(females, males)
	playbill.close()

# Return all valid properties of an Actor object and their values
def attr(actor):
	return actor.name

populate('playbill.txt')
storyteller.init_relations(roster)

print attr(roster['Gertrude'])