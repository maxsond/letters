#This file is responsible for writing letters

import actors
import storyteller

class Letter(object):

	def __init__(self,author,target,motive):
		self.sal = {'tender': 'Dearest ', 'business': '', 'acquaintance': 'Dear '}
		self.close = {'tender': 'Love,', 'business': 'Regards,', 'acquaintance': 'Sincerely,'}
		self.author = author
		self.target = target
		self.motive = motive

	def salutation(self, author, target):
		if actors.roster[author].relationship[target] > 5:
                    salu = 'tender'
                else:
                    salu = 'acquaintance'
		return '\n' + self.sal[salu] + self.target + ',\n\n'

	def closing(self):
            if actors.roster[self.author].relationship[self.target] > 5:
                mood = 'tender'
            else:
                mood = 'business'

            return self.close[mood] + '\n' + self.author + '\n'

	def body(self):
		return self.motive + '\n\n'

        def lprint(self):
            print self.salutation(self.author, self.target) + self.body() + self.closing()
            return 0
