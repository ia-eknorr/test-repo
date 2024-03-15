## TODO: 
def getAlarms(self, value, app=None):
	states = []
	for i in range(len(self.custom.states)):
		states.append(self.custom.states[i])
	alarms = system.alarm.queryStatus(state=states, provider='default', all_properties=[('App', '=', app)])
	data = []
	for alarm in alarms:
		displayPath = alarm.getDisplayPath()
		priority = alarm.getPriority()
		priorityOrdinal = alarm.getPriority().ordinal()
		state = alarm.getState().ordinal() #0=ClearUnacked, 1=ClearAcked, 2=ActiveUnacked, 3=ActiveAcked
		stateOrder = [1,0,3,2].index(state)
		id = alarm.getId()
		name = alarm.getName()
		
		timestamp = None
		timestampMS = None
		eventValue = None
		
		active = {}
		if alarm.getActiveData() != None:
			for prop in alarm.getActiveData().getValues():
				active[prop.getProperty().getName()] = prop.getValue()
			
		clear = {}
		if alarm.getClearedData() != None:
			for prop in alarm.getClearedData().getValues():
				clear[prop.getProperty().getName()] = prop.getValue()
		
		stateDict = active if state in [2,3] else clear
		if "eventTime" in stateDict:
			timestamp = system.date.format(stateDict["eventTime"], "M/d/yy hh:mm:ss a")
			timestampMS = stateDict["eventTime"]
		
		if "eventValue" in stateDict:
			eventValue = str(stateDict["eventValue"])
		
		ack = {"isAcked":False, "id":id}
		if state in [1,3]:
			ack["isAcked"] = True
			for prop in alarm.getAckData().getValues():
				propValue = str(prop.getValue())
				if prop.getProperty().getName() == "eventTime":
					propValue = system.date.format(prop.getValue(), "M/d/yy hh:mm:ss a")
				ack[prop.getProperty().getName()] = propValue
		ack = system.util.jsonEncode(ack)
		
		data.append({"id":id, "displayPath":displayPath, "name":name, "priority":priority, "priorityOrdinal":priorityOrdinal, "state":state, "stateOrder":stateOrder, "timestamp":timestamp, "timestampMS":timestampMS, "value":eventValue, "ack":ack})
	
	data.sort(key=lambda x: (x["stateOrder"], x["priorityOrdinal"], x["timestampMS"]), reverse=True)
	return data
	
	
def getAlarmJournal(self, value, states, app=None):
	import re

	startDate=system.date.addMinutes(system.date.now(),-10)
	endDate=(system.date.now())
	
	alarms = system.alarm.queryJournal( startDate=startDate, endDate=endDate, journalName='Journal', state = states)
	ds = system.dataset.toPyDataSet(alarms.getDataset())

	data = []
	for row in range(ds.rowCount):
		path = ds.getValueAt(row, 'Source')
		name = re.split(r'[/:]', path)[-1]
		displayPath = ds.getValueAt(row, 'DisplayPath')
		
		eventTime = system.date.format(ds.getValueAt(row, 'EventTime'), "M/d/yy hh:mm:ss a")
		
#		eventValueLevels = ['ClearAcked', 'ClearUnacked', 'ActiveAcked', 'ActiveUnacked']
		eventValue = ds.getValueAt(row, 'EventState')
		eventType = eventValue
#		eventValue = eventValueLevels[eventValue]
			
		priorityLevels = ['Diagnostic', 'Low', 'Medium', 'High', 'Critical']
		priority = ds.getValueAt(row, 'Priority')
		priority = priorityLevels[priority]
		
		
		data.append({'name':name, 'displayPath':displayPath, 'eventTime':eventTime, 'eventValue':eventValue, 'eventType':eventType, 'priority':priority})
	data.sort(key=lambda x: (x['eventTime']), reverse=True)
	return data
