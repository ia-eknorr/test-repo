## TODO: Document
# Import
from exchange.water.common.abstract.udt import AbstractUdt

class HypoTransfer(AbstractUdt):
	""" """
	# HypoTransfer UDT Type
	_udtType = 'Exchange/Water/HypoTransfer'
	
	## Properties
	@property
	def autoRefillSetpoint(self):
		""" """
		return self.get('AutoRefillSetpoint')
		
	@property
	def flowRate(self):
		""" """
		return self.get('FlowRate')
		
	@property
	def timeout(self):
		""" """
		return self.get('Timeout')
		
	@property
	def selectedBulkTank(self):
		""" """
		return self.get('SelectedBulkTank')
		
	def setInProcess(self, value, immediate=False):
		""" """
		return self._setValue('InProcess', value, immediate=immediate)
		
	def setLastGallons(self, value, immediate=False):
		""" """
		return self._setValue('LastGallons', value, immediate=immediate)
		
	def setLastSource(self, value, immediate=False):
		""" """
		return self._setValue('LastSource', value, immediate=immediate)
		
	def setLastTransfer(self, value, immediate=False):
		""" """
		return self._setValue('LastTransfer', value, immediate=immediate)
	
	def setTransferStart(self, value, immediate=False):
		""" """
		return self._setValue('TransferStart', value, immediate=immediate)
		
	def setMessage(self, message, immediate=False):
		""" """
		return self._setValue('Message', message, immediate=immediate)
		
	def setSelectedBulkTankNumber(self, bulkTankNumber, immediate=False):
		""" """
		return self._setValue('SelectedBulkTank', bulkTankNumber, immediate=immediate)