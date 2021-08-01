from hello import *

class Team:
	name = ''
	members = []
	def __init__(self, name):
		self.name = name
	
	def add_member(self, new_member):
		self.members.append(new_member)

	def printAll(self):
		print("team name "+self.name)
		for member in self.members:
			print(member+" ")

hello2()
print(__name__)
t1 = Team('AmazingGuys')
t1.add_member('Jake')
t1.add_member('Kyle')
t1.printAll();