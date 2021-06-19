from typing import List, Dict
from flask import Flask
import json
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects.mysql import DATETIME
import logging



app = Flask(__name__)

load_dotenv()
db_user = os.getenv('user')
db_pwd = os.getenv('password')
db_host = os.getenv('host')
db_port = os.getenv('port')
db_name = os.getenv('database')


connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = create_engine(connection_str)
connection = engine.connect()
logging.info(' - - - ✅ MySQL Docker Container Python connection ok - - - \n')


@app.route('/')
def index() -> str:
    return ' - - - ✅ MySQL Database `flask_mysql` connection ok - - - '


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)