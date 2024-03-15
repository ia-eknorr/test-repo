## TODO: Document
# Import
from exchange.water.common.abstract.udt import AbstractUdt

class HOA(AbstractUdt):
	"""Hand Off Auto"""
	_udtType = 'Exchange/Water/HOA'
	def setAuto(self, value, immediate=False):
		""" """
		self.addWrites('Auto', value)
		if immediate: self.writeTags()
		return None
	
	def setFaulted(self, value, immediate=False):
		""" """
		self.addWrites('Faulted', value)
		if immediate: self.writeTags()
		return None
	
	def setHand(self, value, immediate=False):
		""" """
		self.addWrites('Hand', value)
		if immediate: self.writeTags()
		return None
			
	def setMode(self, value, immediate=False):
		""" """
		self.addWrites('Mode', value)
		if immediate: self.writeTags()
		return None
		
	@property
	def auto(self):
		""" """
		return self.get('Auto')
	
	@property
	def faulted(self):
		""" """
		return self.get('Faulted')
		
	@property
	def hand(self):
		""" """
		return self.get('Hand')
		
	@property
	def mode(self):
		""" """
		return self.get('Mode')
	
	@property
	def value(self):
		""" """
		return self.get('Value')
		
	@property
	def device(self):
		""" """
		return self.get('Device')