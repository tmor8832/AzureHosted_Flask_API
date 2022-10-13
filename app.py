from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import date
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import uuid
from flask_cors import CORS
import mysql.connector
from mysql.connector import errorcode
import json

app = Flask(__name__)
api = Api(app)

CORS(app) #enable routes from other parts of the network without blocking the requests

'''
Obtain connection string information from the portal after setting up the database. 

Set up the database using these instructions https://learn.microsoft.com/en-us/azure/mysql/single-server/quickstart-create-mysql-server-database-using-azure-portal

Access the database using this guide https://learn.microsoft.com/en-us/azure/mysql/single-server/connect-python?source=recommendations
'''

config = {
  'host':'jhub123aa.mysql.database.azure.com',
  'user':'azureuser',
  'password':'123456Aa',
  'database':'weather',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': '/etc/ssl/certs/DigiCertGlobalRootG2.crt.pem'
}

class Event(Resource):
    def put(self, location, temperature, wind):
        try:
            conn = mysql.connector.connect(**config)
            print("Connection established")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            ''' The first time the function is executed to create the table uncomment this and use it, once created no longer needed'''
            # Drop previous table of same name if one exists
        #     cursor.execute("DROP TABLE IF EXISTS weather;")
        #     print("Finished dropping table (if existed).")
        #    # Create table
        #     cursor.execute("CREATE TABLE weather (id serial PRIMARY KEY AUTO_INCREMENT, location VARCHAR(50) NOT NULL, wind VARCHAR(50) NOT NULL, temperature INTEGER NOT NULL);")
        #     print("Finished creating table.")
        #    #Insert some data into table
            cursor.execute("INSERT INTO weather (location, wind, temperature) VALUES (%s, %s, %s);", (location, wind, temperature))
            print("Inserted",cursor.rowcount,"row(s) of data.")
            conn.commit()
            cursor.close()
            conn.close()
        return "success"
   
    def patch(self, location, temperature, wind):
        conn = mysql.connector.connect(**config)
        results = []
        print("Connection established")
        cursor = conn.cursor()
        cursor.execute("""
                UPDATE weather
                set wind = %s, temperature =%s
                WHERE location = %s""", (wind, temperature, location,))
        for row in cursor:
            results.append(row)
        conn.commit()
        cursor.close()
        conn.close()
        resultsjson = json.dumps(results)
        return resultsjson

class allEvents(Resource):
    def get(self):
        results = []
        try:
            conn = mysql.connector.connect(**config)
            print("Connection established")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            cursor.execute("""
                    SELECT location, temperature, wind
                    FROM weather """)
            for row in cursor:
                results.append(row)
            conn.commit()
            cursor.close()
            conn.close()
            resultsjson = json.dumps(results)
            return resultsjson

class getWind(Resource):
    def get(self, location):
        results = []
        try:
            conn = mysql.connector.connect(**config)
            print("Connection established")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            cursor.execute("""
                    SELECT location, wind 
                    FROM weather
                    WHERE location = %s""", (location,))
            for row in cursor:
                results.append(row)
            # Cleanup
            conn.commit()
            cursor.close()
            conn.close()
            resultsjson = json.dumps(results)
            return resultsjson

class getTemp(Resource):
    def get(self, location):
        results = []
        try:
            conn = mysql.connector.connect(**config)
            print("Connection established")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            cursor.execute("""
                    SELECT location, temperature
                    FROM weather
                    WHERE location = %s""", (location,))
            for row in cursor:
                results.append(row)
            # Cleanup
            conn.commit()
            cursor.close()
            conn.close()
            resultsjson = json.dumps(results)
            return resultsjson

class deleteOne(Resource):
    def delete(self, location):
        try:
            conn = mysql.connector.connect(**config)
            print("Connection established")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            cursor.execute("""
                    DELETE FROM weather
                    WHERE location = %s""", (location,))
            # Cleanup
            conn.commit()
            cursor.close()
            conn.close()
            return ""

class deleteAll(Resource):
    def delete(self):
        try:
            conn = mysql.connector.connect(**config)
            print("Connection established")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            cursor.execute("""
                    DELETE FROM weather 
                    """)
            # Cleanup
            conn.commit()
            cursor.close()
            conn.close()
            return ""
api.add_resource(Event, "/event/<string:location>/<int:temperature>/<string:wind>")
api.add_resource(allEvents, "/getevents/")
api.add_resource(getWind, "/getWind/<string:location>/")
api.add_resource(getTemp, "/getTemp/<string:location>/")
api.add_resource(deleteOne, "/deleteOne/<string:location>")
api.add_resource(deleteAll, "/deleteAll/")

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(port=8000)
