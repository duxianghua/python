import MySQLdb

host='localhost'
user='root'
passwd='123123'


def mysql(SQL):
	SQL_commend=SQL
	try:
		db=MySQLdb.connect(host,user,passwd)
		sql=db.cursor()
		sql.execute(SQL_commend)
		data=sql.fetchall()
		return data
		db.close()
	except Exception, e:
		print e

show global status like ‘Max_used_connections’;

for i in data:
		print i[0],'\t\t\t',i[1]

import netsnmp

def snmp(iod):
	var=netsnmp.Varbind(iod)
	print var
	result = netsnmp.snmpwalk(var,Version = 2,DestHost="localhost",Community="public")
	return result
