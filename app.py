from flask import Flask
import os
import sys
from flask_cors import CORS
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'loginflask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql@localhost:3306/loginflask'
app.config['SECRET_KEY'] = 'dkmy-project'

app.secret_key = os.urandom(24)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

import views

if __name__ == "__main__":
    app.run(debug=True)

# os.system("clear-cache.sh")