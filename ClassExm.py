class Car:
	
	def __init__(self,x=40):
		self.xyz=x
	def turn_left(self,x):
		self.xyz=x

var = Car(56)
print(var.xyz)
#xyz.turn_left(40)
