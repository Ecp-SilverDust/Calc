def soma(a,b=None):
	if b==None:
                b=a
	
	if is_number(a) and is_number(b)==True:
		return float(a)+float(b)
	else:
		return False
	
def is_number(c):
	try:
		float(c)
		return True
	except ValueError:
		return False
	

