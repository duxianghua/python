import netsnmp

class SNMP(object):
	"""SNMP default parameters
	Version = 2
	DestHost = localhost
	Community = public
	"""
	def __init__(self,Version=2,DestHost='localhost',Community='public'):
		self.Version = Version
		self.DestHost = DestHost
		self.Community = Community
	def snmp_walk(self,iod):
		var=netsnmp.Varbind(iod)
		result = netsnmp.snmpwalk(var,
			Version = self.Version,
			DestHost = self.DestHost,
			Community = self.Community)
		return result
	def snmp_get(self,iod):
		var=netsnmp.Varbind(iod)
		result = netsnmp.snmpget(var,
			Version = self.Version,
			DestHost = self.DestHost,
			Community = self.Community)
		return result