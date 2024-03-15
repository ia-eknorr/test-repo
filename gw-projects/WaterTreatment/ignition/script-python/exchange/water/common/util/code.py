## TODO: 
def getFillColors(colors=['rgba(180,180,180,1)'], index=0):
	"""
	Args:
		colors:
		index: 
	Returns:
		rgb color string
	"""
	try:
		# last value in array is the fallback - [-1] will return last value in array
		index = -1 if index < -1 else index
		
		return colors[index].value if len(colors) > index else colors[-1].value
	except:
		try:
			return colors[index] if len(colors) > index else colors[-1]
		except:
			return 'rgba(150,150,150,1)'