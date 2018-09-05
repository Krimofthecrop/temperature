def kelvin_to_celsius(temp):
	"""
	Covert a temperture from Kelvin to Celsius
	"""
	return temp - 273.15

def celsius_to_fahr(temp):
	"""
	Covert a temp. from Celsius to Fahrenheit
	"""
	return temp * (9/5) + 32

def kelvin_to_fahr(temp):
	"""
	Covert a temp. from Kelvin to Fahrenheit
	"""
	temp_c = kelvin_to_celsius(temp)
	result = celsius_to_fahr(temp_c)
	return result
