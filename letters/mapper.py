import map
'''
Add rooms to the map from a text file.
First line: RoomID (e.g. 'prison')
Second line: Room description text
Third-nth line: RoomID of connected room, followed by a space, followed by the exit's description
'''

def build_rooms(roomfile):
#default roomfile should be 'rooms.txt'
	buildroom = { 0 : 'RoomID',
		1 : 'desc',
		2 : 'exitnum'
		}
	temproom = []
	f = open(roomfile, 'r')
	g = f.readlines()
	for line in g:
		if line[0] != '\n':
			temproom.append(line)
			print temproom			# testing purposes only
		else:
			map.roomlist[temproom[0]] = map.Room(temproom[0][:-1:],temproom[1][:-1:]) #splicing to remove the newline
			for item in temproom[2::]:
				print ('Item: %s' % item)
				temppaths = item.split(',')
				if len(temppaths) < 3:
					break
					print('Warning! Room %s is missing exit or description data!' % temproom[0])
				else:
					map.roomlist[temproom[0]].paths[temppaths[0]] = temppaths[1], temppaths[2]
			print temproom
			temproom = []
			print temproom
	f.close()
	
build_rooms('rooms.txt')
for item in map.roomlist:
	print map.roomlist[item].name
	print map.roomlist[item].look()
