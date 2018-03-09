import dbconfig
import pymysql

def _connect():
	conn = pymysql.connect(host = "localhost",
						   user = dbconfig.db_user,
						   passwd = dbconfig.db_password)
	return conn
   
def get_all():
	conn = _connect()
	try:
		with conn.cursor() as cursor:
			cursor.execute("SELECT latitude, longitude, date, category, description FROM crimemap.crimes")
			
			keys = ("latitude", "longitude", "date", "category", "description")			
			crimes = []
			for crime in cursor.fetchall():
				crime_dict = dict(zip(keys, crime))
				crime_dict["date"] = crime_dict["date"].strftime("%F")
				crimes.append(crime_dict)

			return crimes
	finally:
		conn.close()
		
def add_crime(data):
	conn = _connect()
	try:
		with conn.cursor() as cursor:
			cursor.execute("""INSERT INTO crimemap.crimes (latitude, longitude, date, category, description)
							  VALUES (%(latitude)s, %(longitude)s, %(date)s, %(category)s, %(description)s);""", data)
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
			cursor.execute("DELETE FROM crimemap.crimes WHERE id = %s", id_)
			conn.commit()
	finally:
		conn.close()
