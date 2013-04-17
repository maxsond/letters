'''
This module handles movement around the game world.
It also handles representing the game world.
'''

'''
First, let's define a room.
'''

roomlist = {}

class Room(object):

	def __init__(self,name,desc):
		self.name = name
		self.desc = desc
		self.paths = {}
		self.inventory = {}
		
	def go(dest):
		return self.paths.get(dest,None)
	
	def look(self):
		return str(self.desc) + ' ' + str(' '.join([self.inventory[x].desc for x in self.inventory])) + ' '.join([self.paths[x] for x in self.paths])
'''
Note at the moment that Look() does not have a feature to sort.
It just spits out the items in random order.
Eventually we will want to add sorting, if only for doors and other exits.
'''

'''Test room'''
prison = Room('Prison',
'You find yourself in a dingy stone room.'
)

'''Next, let's define things to populate the rooms with.'''

class Thing(object):

	def __init__(self,ID,type,desc):
		self.ID = ID
		self.type = type
		self.desc = desc
		self.locations		 = []
		self.verb = {}

'''
Test child of thing.
This might be useful if we need things with special attributes or functions.
'''	
class Door(Thing):
	pass
	
gameinventory = {}	
oakdoor = Door(1,'door','A sturdy oak door is set in the north wall.')
chair = Thing(2,'chair','A cactus wood seat lies in the corner.')
gameinventory['door'] = oakdoor
prison.inventory['door'] = oakdoor
prison.inventory['chair'] = chair

'''with open('items.txt', 'r') as f:
	thinglist = f.readlines()
	for o in thinglist[::3]:
		i = thinglist.index(o)
		if o != '#':
			if o == '':
				break
			else:
			#need to find a way to pull the name of the indexed item rather than the index itself
				thinglist[i] = Thing(thinglist[i],thinglist[i+1],thinglist[i+2])
				prison.inventory['''

