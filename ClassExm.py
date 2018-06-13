class Car:
	
	def __init__(self,x=40):
		self.xyz=x
		print("Constructor")	
	def turn_left(self,x):
		self.xyz=x
		print("2nd Method")

var = Car(56)
print(var.xyz)
print(var.turn_left(30))
print(var.xyz)
