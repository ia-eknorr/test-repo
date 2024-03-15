# Import
from exchange.water.common.abstract.sfc_chart import AbstractSFC

# Chart Definition Classes
class Backwash(AbstractSFC):
	"""Backwash SFC Chart"""
	_item = 'Backwash'
	_parameters = {'filterNumber': 1}
	
class HypoTransfer(AbstractSFC):
	"""HypoTransfer SFC Chart"""
	_item = 'HypoTransfer'
	_parameters = {'bulkTankNumber': 1}