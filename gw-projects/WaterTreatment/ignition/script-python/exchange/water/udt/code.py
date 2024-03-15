# Import
from exchange.water.common.udt import filter, hoa, hypotransfer

# Functions
def getFilter(referenceValue):
	"""Get the filter UDT instance reference class
	
	Args:
		referenceValue: value to get the filter reference by,
			can be an int (filterNumber) or a string (path)
	Returns:
		class instance of the filter udt
	"""
	if isinstance(referenceValue, int) or isinstance(referenceValue, float):
		cls = filter.Filter.getByNumber(referenceValue)
	elif isinstance(referenceValue, str) or isinstance(referenceValue, unicode):
		cls = filter.Filter(referenceValue)
	else:
		raise Exception
	return cls

def getHoa(devicePath):
	"""Get the HOA udt instance reference class
	
	Args:
		devicePath: tag path to the HOA udt instance
	Returns:
		class instance of the HOA UDT
	"""
	return hoa.HOA(devicePath)
	
def getHypoTransfer(path='[default]Exchange/Water/Hypo/HypoTransfer'):
	"""Get the HyperTransfer udt instance reference class
	
	Args:
		path: tag path to the HypoTrasnfer udt instance
	Returns:
		class instance of the HypoTrasnfer UDT
	"""
	return hypotransfer.HypoTransfer(path)

