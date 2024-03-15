## TODO: Document
# Import
from exchange.water.common.abstract.udt import AbstractUdt

class Filter(AbstractUdt):
	""" """
	# Filter UDT Type
	_udtType = 'Exchange/Water/Filter'
	
	# Filter Static Values
	drainSetpoint = 15.0		# Level setpoint when draining the filter (inches)
	drainRate = 13.0			# Drain filter at this rate (inches per second)
	blowerSetpoint = 25			# Pressure setpoint before opening air scour valve
	blowerRate = 3.1			# Blower pressure builds at this rate (psi per second)
	scourTimeSetpoint = 10		# Duration of air scour process (seconds)
	turbSetpoint = 11			# Minimum backwash turbidity setpoint (ntu)
	turbRate = 0.052			# Turbidity changes at this rate (ntu per second) 
	rinseTurbSetpoint = 0.1		# Maximum turbidity to return filter to service (ntu)
	fillSetpoint = 90.0			# Minimum filter level prior to opening effluent valve (inches)
	fillRate = 8.0				# Fill filter at this rate (inches per second)
	restTimeSetpoint = 10		# Filter rest time setpoint (seconds)
	flowRate = 171				# Flow rate change (gallons per second)
	backwashFlowSetpoint = 5230	# Backwash flow rate setpoint (gallons per minute)
	rinseFlowSetpoint = 1100	# Rinse flow rate setpoint (gallons per minute)
	def getBehaviorConfigs(self):
		""" """
		return {
			'drainSetpoint': self.drainSetpoint, 'drainRate': self.drainRate, 'blowerRate': self.blowerRate, 'blowerSetpoint': self.blowerSetpoint
			, 'scourTimeSetpoint': self.scourTimeSetpoint, 'turbSetpoint': self.turbSetpoint, 'turbRate': self.turbRate
			, 'rinseTurbSetpoint': self.rinseTurbSetpoint, 'fillSetpoint': self.fillSetpoint, 'fillRate': self.fillRate
			, 'restTimeSetpoint': self.restTimeSetpoint, 'flowRate': self.flowRate
			, 'backwashFlowSetpoint': self.backwashFlowSetpoint, 'rinseFlowSetpoint': self.rinseFlowSetpoint
		}
	
	def __valve(self, path, state, immediate):
		""" """
		value = 1 if state.lower() == 'open' else 0
		self.addWrites(path, value)
		if immediate: self.writeTags()
		return None
		
	def setBackwashStep(self, step, immediate=False):
		""" """
		self.addWrites('Backwash/Step', step)
		if immediate: self.writeTags()
		return None
	
	## Influent Valve
	def influentValve(self, state, immediate=False):
		""" """
		self.__valve('Valves/Influent/Auto', state, immediate)
		return None
	
	## Effluent Valve
	def effluentValve(self, state, immediate=False):
		""" """
		self.__valve('Valves/Effluent/Auto', state, immediate)
		return False
	
	## Drain Valve
	def drainValve(self, state, immediate=False):
		""" """
		self.__valve('Valves/Drain/Auto', state, immediate)
		return False
		
	## AirScour Valve
	def airScourValve(self, state, immediate=False):
		""" """
		self.__valve('Valves/AirScour/Auto', state, immediate)
		return False
		
	## Backwash Valve
	def backwashValve(self, state, immediate=False):
		""" """
		self.__valve('Valves/Backwash/Auto', state, immediate)
		return False
		
	## Rinse Valve
	def rinseValve(self, state, immediate=False):
		""" """
		self.__valve('Valves/Rinse/Auto', state, immediate)
		return False
			
	## Waste Valve
	def wasteValve(self, state, immediate=False):
		""" """
		self.__valve('Valves/Waste/Auto', state, immediate)
		return False
		
	@staticmethod
	def getByNumber(filterNumber):
		""" """
		return Filter('[default]Exchange/Water/Filters/Filter{0}'.format(filterNumber))