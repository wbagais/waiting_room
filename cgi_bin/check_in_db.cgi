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

import cgitb
cgitb.enable()
#get the data from the form
form = cgi.FieldStorage()
p_id = form.getvalue('id','')
service = form.getvalue('service', '')
physician =  form.getvalue('physician',' ')

def get_waiting_number(physician_id, sevice_id):
    print("TEST")

#print("<html>")

f = open("/home/wbagais/waiting_room_files/header.html", 'r')
transcript = f.read()
print(transcript)
f.close()

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

#Select service id
sql_service = "SELECT service_id, name, severity_level FROM service WHERE service_id  = "
sql_service = sql_service + service + ";"

cursor.execute(sql_service)
service_result = cursor.fetchall()

if (service == '3'):
    waiting_path = "/home/wbagais/waiting_room_files/waiting_list/"  
    waiting_path = waiting_path + str(physician_result[0][0])  
    waiting_path = waiting_path + "/emergency_waiting_list.txt"
else:
    waiting_path = "/home/wbagais/waiting_room_files/waiting_list/" + str(physician_result[0][0]) + "/regular_waiting_list.txt"

#check if the patient id exist
if(len(patient_result) == 0):
    print('not valid user id')
else:
    #print patient, pysician, service info
    print("patient name")
    print(patient_result[0][1]," ",patient_result[0][2],"<br />")
    print("physician name")
    print(physician_result[0][1]," ",physician_result[0][2],"<br />")
    print("service ")
    print(service_result[0][1],"<br />")
    
    # Add the patient to the waiting list
    f = open(waiting_path,'a')
    f.write(p_id)
    f.write(",")
    f.write(str(service_result[0][0]))
    f.write("\n")
    f.close()

    num_lines = file_len(waiting_path)
    #print(waiting_path) 
    if(service != '3'):
        emergency_path = "/home/wbagais/waiting_room_files/waiting_list/" 
        emergency_path = emergency_path + str(physician_result[0][0]) 
        emergency_path = emergency_path + "/emergency_waiting_list.txt"
        
        if(os.stat(emergency_path).st_size != 0):
            num_lines = num_lines + file_len(emergency_path)
        

    print("estimate Waiting time is ")
    waiting_time = 0
    if (num_lines > 0):
        waiting_time = str((num_lines-1) * 15)
    print(str(waiting_time), "min <br />")

    f = open("/home/wbagais/waiting_room_files/footer.html", 'r')
    transcript = f.read()
    print(transcript)
    f.close()
