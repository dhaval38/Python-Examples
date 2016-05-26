def fahrenhiet(T):
	return((float(9)/5)*T + 32)

def celsius(T):
	return (float(5)/9)*(T-32)

tempratures = (36.5, 37, 37.5, 38, 39)
if __name__ == "__main__":
	temp_in_fahrenhiet = list(map(lambda x:(float(9)/5)*x+32, tempratures))
	temp_in_celsius = list(map(lambda y:(float(5)/9)*(y-32), temp_in_fahrenhiet))
	print "Fahrenhiet : %s" %temp_in_fahrenhiet
	print "Celsius : %s" %temp_in_celsius
