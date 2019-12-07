#!/usr/bin/env python3.4

print("Content-type: text/html\n\n")

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

import sqlite3
import pandas as pd
from matplotlib import pyplot as plt
import cgi
import os
from datetime import datetime

import cgitb
cgitb.enable()
#get the data from the form
form = cgi.FieldStorage()
p_id = form.getvalue('id','')
service = form.getvalue('service', '')
physician =  form.getvalue('physician','')

def get_waiting_number(physician_id, sevice_id):
    print("TEST")

f = open("/home/wbagais/waiting_room_files/header.html", 'r')
transcript = f.read()
print(transcript)
f.close()

import sys

#Check if all values exest
if (p_id == ''):
    print("<h1> Please Enter the patient number</h1>") 
    sys.exit(0)

elif(service == ''):
    print("<h1> Please Select a service</h1>")
    sys.exit(0)

elif (physician == ''):
    print("<h1> Please Select a physician</h1>")
    sys.exit(0)

#connect to the database
conn = sqlite3.connect('/home/wbagais/waiting_room_files/waiting_room_db.db')
cursor = conn.cursor()
#select the patient information
sql = "SELECT patient_id, fname, lname FROM patient WHERE patient_id = "
sql = sql + p_id + ";"

cursor.execute(sql)

patient_result = cursor.fetchall()
#select the physician id 
sql_physician = "SELECT physician_id, fname, lname FROM physician WHERE physician_id  = "
sql_physician = sql_physician + physician + ";"

cursor.execute(sql_physician)
physician_result = cursor.fetchall()


#select max order number
date = datetime.today().strftime('%Y-%m-%d')

sql_order = "SELECT MAX(order_num), COUNT(*) FROM check_in WHERE check_out=0 AND physician_id = "
sql_order = sql_order + physician + " AND date = '" + date +"'" 

if(service == '3'):
    sql_order = sql_order + "AND service_id = 3"

cursor.execute(sql_order)
order_result = cursor.fetchall()
max_order = 0
count_order = 0 
if (len(order_result) >  0 and order_result[0][0] is not None):
    max_order = order_result[0][0]
if (len(order_result) >  0 and order_result[0][1] is not None):
    count_order =  order_result[0][1]
#Select service id
sql_service = "SELECT service_id, name, severity_level FROM service WHERE service_id  = "
sql_service = sql_service + service + ";"

cursor.execute(sql_service)
service_result = cursor.fetchall()


#check if the patient id exist
if(len(patient_result) == 0):
    print('<h1 class="mb-10">')
    print('Patient ID does NOT exist')
    print("</h1>")
else: 
    #############################
    try:
        sql = ''' INSERT INTO check_in (patient_id, physician_id, service_id, date, order_num, check_out) VALUES(?,?,?,?,?,0)'''

        cursor.execute(sql, (p_id,physician,service,date, max_order+1))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique
        conn.close()


    ##############################

    #print patient, pysician, service info
    print('<h1 class="mb-10">')
    print("patient name")
    print(patient_result[0][1]," ",patient_result[0][2],"<br />")
    print("physician name")
    print(physician_result[0][1]," ",physician_result[0][2],"<br />")
    print("service ")
    print(service_result[0][1],"<br />")
    
    

    print("estimate Waiting time is ")
    waiting_time = 0
    #if (num_lines > 0):
    if ( count_order >0):
        #waiting_time = str((num_lines-1) * 15)
        waiting_time = str((count_order)*15)
    print(str(waiting_time), "min <br />")
print("</h1>")
#add the footer code
f = open("/home/wbagais/waiting_room_files/footer.html", 'r')
transcript = f.read()
print(transcript)
f.close()
