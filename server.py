#this is a server client socket connection from person counter to a server from which the data will be further send to webapp and database
import pickle
import socket
import json

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database import Base,Iot_Counter
import random
import string
import time
import pymongo
import datetime

from pymongo import MongoClient
# IMPORTS FOR AUTHENTICATION


import json
from flask import make_response
import requests

#import for flask admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
admin=Admin(app)
#app = Flask(__name__)




# Connect to Database and create database session
engine = create_engine('sqlite:///Iot_Counter.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


admin.add_view(ModelView(Iot_Counter,session))

#admin.add_view(ModelView(StatementTable,session))
#admin.add_view(ModelView(StatementHistory,session))




client = MongoClient('mongodb://localhost:27017/')
db = client['messCapa']
collection = db['dataTable']

class foo(object):
    pass

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

i=0
a=0

#data_json={}

print "conn info: ", conn
while True:
    objrcv = pickle.loads ( conn.recv ( 1024 ) )
    print "conn recv: ", objrcv
    print "conn from: ", addr
    if objrcv.Y == 0:
        print 'down count'
        print objrcv.X
        global i
        i = 0
        i = str(objrcv.X)
        result = db.dataTable.insert_one({"downcount": i})

#yahaan se tujhe i ko database pe daalna hai
    elif objrcv.Y == -1:
        print "upcount"
        print  objrcv.X
        global a
        a = 0
        a = str(objrcv.X)

        result = db.dataTable.insert_one({"upCount": a})
        y = int(a) - int(i)
        result = db.dataTable.insert_one({"totalCountofpeople": y})


#    parsed = json.loads(data_json)
#    final = json.dumps(parsed)
#    with open("inOut.json","w") as f:
#      f.write(final)

        #yahaan se up jaaega
'''

@app.route("/", methods=["GET", "POST"])
def index():
    myUser= Iot_Counter.query.all().first()

    # print myUser.query.all()
    #print session.query(Iot_Counter).query.all()
    # print type(myUser)
    return render_template('index.html', myUser=myUser)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
    #app.run(host='127.0.0.1', port=5000)
'''
