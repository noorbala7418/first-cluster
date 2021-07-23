from flask import Flask, request, Response
import datetime
import mysql.connector

app = Flask(__name__)
app.config["DEBUG"] = True

def insert_to_db():
    """ Insert Tweet To Database"""

    mydb = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="cluster",
    )
    myc = mydb.cursor()
    val = datetime.datetime.now()
    sql = f"INSERT INTO reqs (req_id) VALUES ('{val}')"
    myc.execute(sql)

    mydb.commit()
    mydb.close()
    myc.close()

@app.route('/', methods=['GET'])
def home():
    insert_to_db()
    return 'Im Alive!'

@app.route('/healthy', methods=['GET'])
def healthy():
    return 'its ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
