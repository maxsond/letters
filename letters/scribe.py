import actors
import storyteller

class Letter(object):

	def __init__(self,author,target,motive):
		self.sal = {'tender': 'Dearest ', 'business': '', 'acquaintance': 'Dear'}
		self.close = {'tender': 'Love,', 'business': 'Regards,', 'acquaintance': 'Sincerely,'}
		self.author = author
		self.target = target
		self.motive = motive
	
	def salutation(self):
		if roster[author]['relationship'][target] > 5:
			salu = 'tender'
		return self.sal[salu] + self.target
	def closing(self):
		return "Love, " + self.author
	def body(self):
		return self.motive