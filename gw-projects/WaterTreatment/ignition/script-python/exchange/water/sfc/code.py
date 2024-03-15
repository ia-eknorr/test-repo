# Import
from exchange.water.common.abstract.delegate import AbstractDelegate
from exchange.water.common.sfc import charts

class SFC(object):
	"""SFC enum like class to get SFC container class
	
	SFCs Delegated:
		Backwash
			- filterNumber: number of the filter to perform backwash on (1-9)
		HypoTransfer
			- bulkTankNumber: number of the bulk tank to do hypo transfer on (1-3)
	"""
	__metaclass__ = AbstractDelegate
	_package = charts