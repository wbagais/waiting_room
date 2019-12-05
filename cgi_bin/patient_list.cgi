#!/usr/bin/env python3.4

print("Content-type: text/html\n\n")

import sqlite3
import pandas as pd
from matplotlib import pyplot as plt
import cgi
import os
from datetime import datetime

import cgitb
cgitb.enable()

#get physician id
link = cgi.FieldStorage()
physician_id = link["physician_id"].value
#start_time = link["start_time"].value
comment = link.getvalue("comment", "")
start_time = link.getvalue("start_time", "")
patient_id = link.getvalue("patient_id", "")
service_id = link.getvalue("service_id", "")
duration = 0 
sql = ""
if(patient_id != "" and start_time != ""):
    end_time = datetime.now().strftime("%H:%M:%S")
    
    FMT = '%H:%M:%S'
    duration = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    
    date = datetime.today().strftime('%Y-%m-%d')
    
    #connect to the database
    conn = sqlite3.connect('/home/wbagais/waiting_room_files/waiting_room_db.db')
    cursor = conn.cursor()
    
   # sql = ''' INSERT INTO visit (patient_id, physician_id, service_id, data,start_time, end_time,comment) VALUES(?,?,?,?,?)''', (patient_id,physician_id,service_id,date,start_time,end_time,comment) 
    #sql = sql + "VALUES ("
    #sql = sql + patient_id + ","
    #sql = sql + physician_id + ","
    #sql = sql + service_id + ","
    #sql = sql + "'" + date + "',"
    #sql = sql + "'" + start_time + "',"
    #sql = sql + "'" + end_time + "',"
    #sql = sql + "'" + comment + "'"
    #sql = sql + ")"

    try:
        #cursor.execute("SELECT * FROM visit")
        sql = ''' INSERT INTO visit (patient_id, physician_id, service_id, date,start_time, end_time,comment) VALUES(?,?,?,?,?,?,?)'''
        
        cursor.execute(sql, (patient_id,physician_id,service_id,date,start_time,end_time,comment))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique
        conn.commit()
    #patient_result = cursor.fetchone()

    try:
        #cursor.execute("SELECT * FROM visit")
        checkin_sql = "UPDATE check_in SET check_out=1  WHERE patient_id='"
        checkin_sql = checkin_sql + str(patient_id) + "' AND date='" + str(date) + "'"

        cursor.execute(checkin_sql)
        conn.commit()
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0]) # column name is not unique
        conn.commit()

##########################FUNCTIONS######################################
def print_patients(patients_list):
    for patient in patients_list:
        print("<tr>")
        print("<td>")
        print(patient[0])
        print("</td>")

        name_sql = "SELECT fname, lname FROM patient WHERE patient_id = " + str(patient[0])
        cursor.execute(name_sql)
        first_result = cursor.fetchone()
        print("<td>")
        print(first_result[0] , " ", first_result[1])
        print("</td>")

        name_sql = "SELECT name FROM service WHERE service_id = " + str(patient[1])
        cursor.execute(name_sql)
        first_result = cursor.fetchone()
        print("<td>")
        print(first_result[0])
        print("</td>")

        url = "http://students.hi.gmu.edu/cgi-bin/wbagais/patient_details.cgi?physician_id=" 
        url = url + physician_id 
        url = url + "&patient_id=" 
        url = url + str(patient[0]) 
        url = url + "&service_id=" 
        url = url + str(patient[1])
        print('<td><a href=' +url + '>View</a></td>')
        print("</tr>")

def print_from_file(path):
    f = open(path, 'r')
    for line in f:
        print("<tr>")
        txt = line.split(',')
        for i in txt:
            print("<td>")
            print(i)
            print("</td>")

        url = "http://students.hi.gmu.edu/cgi-bin/wbagais/patient_details.cgi?physician_id=" + physician_id + "&patient_id=" + txt[0] + "&service=" + txt[2]
        print('<td><a href=' +url + '>View</a></td>')
        print("</tr>")
    f.close()

##########################END FUNCTIONS######################################

#print the header
f = open("/home/wbagais/waiting_room_files/header_1.html", 'r')
transcript = f.read()
print(transcript)
f.close()
#print page name
print("Patient List")
#print the rest of the header
f = open("/home/wbagais/waiting_room_files/header_2.html", 'r')
transcript = f.read()
print(transcript)
f.close()

print('<section class="team-area section-gap">')
print('<div class="container">')
print('<div class="row d-flex justify-content-center">')
print('<div class="menu-content pb-70 col-lg-7">')
print('<div class="title text-center">')

#connect to the database
conn = sqlite3.connect('/home/wbagais/waiting_room_files/waiting_room_db.db')
cursor = conn.cursor()

#select the physician name
sql_physician = "SELECT  fname, lname FROM physician WHERE physician_id  = "
sql_physician = sql_physician + physician_id + ";"

cursor.execute(sql_physician)
physician_result = cursor.fetchall()

#print physician name
print('<h1 class="mb-10">')
print(physician_result[0][0]," ",physician_result[0][1])
#print(sql)
print("</h1>")
#######################################
sql_first = "SELECT patient_id,service_id FROM check_in WHERE physician_id = " + physician_id
sql_first = sql_first + " AND check_out =0 AND service_id = 3"
cursor.execute(sql_first)
first_result = cursor.fetchall()

sql_second = "SELECT patient_id,service_id FROM check_in WHERE physician_id = " + physician_id
sql_second = sql_second + " AND check_out =0 AND service_id != 3" 
cursor.execute(sql_second)
second_result = cursor.fetchall()



print('<table width="100%" border="1">')
print("<tr>")
print("<th>Patient ID</th>")
print("<th>Patient Name</th>")
print("<th>Service</th>")
print("<th>&nbsp;</th>")
print("</tr>")

print_patients(first_result)
print_patients(second_result)

print("</table>")
#########################################


#emergency list path
#emergency_path = "/home/wbagais/waiting_room_files/waiting_list/" 
#emergency_path = emergency_path + str(physician_id) 
#emergency_path = emergency_path + "/emergency_waiting_list.txt"
#other patients list path
#other_path = "/home/wbagais/waiting_room_files/waiting_list/"
#other_path = other_path + str(physician_id)
#other_path = other_path + "/regular_waiting_list.txt"

#create the table
#print('<table width="100%" border="1">')
#print("<tr>")
#print("<th>Patient ID</th>")
#print("<th>Patient Name</th>")
#print("<th>Service</th>")
#print("<th>&nbsp;</th>")
#print("</tr>")


#read emergency list
#print_from_file(emergency_path)
#print_from_file(other_path)

#print("</table>")

#print the footer
f = open("/home/wbagais/waiting_room_files/footer.html", 'r')
transcript = f.read()
print(transcript)
f.close()
