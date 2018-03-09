import dbconfig
import pymysql

def _connect():
	conn = pymysql.connect(host = "localhost",
						   user = dbconfig.db_user,
						   passwd = dbconfig.db_password)
	return conn
   
def get_all_inputs():
	conn = _connect()
	try:
		with conn.cursor() as cursor:
			cursor.execute("SELECT id, description FROM crimemap.crimes")
			return cursor.fetchall()
	finally:
		conn.close()
		
def add_input(data):
	conn = _connect()
	try:
		with conn.cursor() as cursor:
			cursor.execute("INSERT INTO crimemap.crimes (description) VALUES ('%s');" % data)
			conn.commit()
	finally:
		conn.close()
		
def clear_all():
	conn = _connect()
	try:
		with conn.cursor() as cursor:
			cursor.execute("DELETE FROM crimemap.crimes")
			conn.commit()
	finally:
		conn.close()
		
def clear(id_):
	conn = _connect()
	try:
		with conn.cursor() as cursor:
			cursor.execute("DELETE FROM crimemap.crimes WHERE id = '%s'" % id_)
			conn.commit()
	finally:
		conn.close()
