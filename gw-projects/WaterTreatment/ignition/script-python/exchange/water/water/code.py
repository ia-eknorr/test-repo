## TODO: 
def setFilterHistory(filterNumber):
	system.perspective.sendMessage("setTagHistory", getFilterHistoryPayload(filterNumber), "page")
	
def getFilterHistoryPayload(filterNumber):
	payload = {}
	tags = []
	
	tagData = {}
	tagData['path'] = '[default]Exchange/Water/Filters/Filter%d/Flow' %filterNumber
	tagData['friendly'] = 'Flow'
	tagData['alias'] = '[default]Exchange/Water/Filters/Filter%d/Flow' %filterNumber
	tagData['enabled'] = True
	tags.append(tagData)
	
	#tagData = {}
	#tagData['path'] = '[default]Exchange/Water/Filters/Filter%d/Level' %filterNumber
	#tagData['friendly'] = 'Level'
	#tagData['alias'] = '[default]Exchange/Water/Filters/Filter%d/Level' %filterNumber
	#tagData['enabled'] = True
	#tags.append(tagData)
	
	
	payload['tags'] = tags
	return payload
