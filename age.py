def person_is_old(age):
	if age>=60:
		return True
	else:
 		return False
def tell_what_to_do(age):
	if person_is_old(age):
		print("U deserved to have a long Vacation")
	else:
		print("Go To Work")

tell_what_to_do(23)
tell_what_to_do(70)
#person_is_old(66)
