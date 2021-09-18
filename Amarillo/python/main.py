'''
pip install flask
set FLASK_APP=main.py
pip install flask-mysql
flask run
'''
import os
import pymysql
from app import app
from db_config import mysqla
from flask import jsonify
from flask import flash, request

@app.route('/users')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM usuario")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route("/")
def hello_world():
	name = os.environ.get("NAME", "World")
	return "Hello {}!".format(name)



if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
