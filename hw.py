'''
Fellow("Pascal", "DRC")
Fellow("Francis", "USA")
Fellow("Kerry", "Ghana/America")
Fellow("Andrew", "Ghana")
	Exception: We cannot afford to hire Andrew
Fellow("Simphiwe, "South Africa")
	Exceptin: We cannot afford to hire Simphiwe
'''
class Mest:
	count_fellow = 0
	
	def __init__(self, name, country):
		self.name = name
		self. country = country

		Mest.count_fellow +=1

	def add_fellow(self):
		if Mest.count_fellow < 5:
			print ("Less than five")

		else:
			Exception ("We cannot afford to hire {} from {}".format(self.name, self.country))
			#print ("We cannot afford to hire {} from {}".format(self.name, self.country))


new_mest = Mest("Pascal", "DRC")
f_mest = Mest("Francis", "Ghana")
ew_mest = Mest("Kerry", "USA")
nsew_mest = Mest("Edem", "Ghana")
neffw_mest = Mest("Stephanie", "Nigeria")

new_mest.add_fellow()


