## TODO: 
def net(units='gallons', time='minute'):
	# Return the net flows for effluent, high service, and filters
	
	# Read tags
	tags = ["[default]Exchange/Water/Flows/CombinedFilterFlow",
			"[default]Exchange/Water/Flows/Finished",
			"[default]Exchange/Water/Flows/HighService",
			"[default]Exchange/Water/Tanks/Clearwell",
			"[default]Exchange/Water/Tanks/Finished1",
			"[default]Exchange/Water/Tanks/Finished2"
			]
	vals = system.tag.readBlocking(tags)
	
	filters = vals[0].value
	finished = vals[1].value
	highService = vals[2].value
	
	if time == 'second':
		# Convert flows from gpm to gallons per second
		filters = filters / 60
		finished = finished / 60
		highService = highService / 60
	
	# Calculate net change to clearwell (convert gallons to feet)
	if units == 'feet':
		# Clearwell: 1 foot = 135239.37888 gallons
		deltas = {'Clearwell':(filters - highService) / 135239.37888}
	else:
		deltas = {'Clearwell':(filters - highService)}
	
	# Calculate net change to finished water tanks
	# Tank 1 is 2.21 times the size of Tank 2
	gals = (highService - finished) / 3.21
	
	if units == 'feet':
		# Tank 1: 1 foot = 171938.0685 gallons
		deltas['Finished1'] = ((gals * 2.21) / 171938.0685)
	
		# Tank 2: 1 foot = 77589.4693 gallons
		deltas['Finished2'] = (gals / 77589.4693)
	else:
		deltas['Finished1'] = (gals * 2.21)
		deltas['Finished2'] = gals
	
	return deltas