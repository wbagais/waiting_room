#!/usr/bin/env python3.4

print("Content-type: text/html\n\n")

def print_from_file(path):
    f = open(path, 'r')
    for line in f:
        print("<tr>")
        txt = line.split(',')
        for i in txt:
            print("<td>")
            print(i)
            print("</td>")
    
        print('<td><a href="">View</a></td>')
        print("</tr>")
    f.close()

import sqlite3
import pandas as pd
from matplotlib import pyplot as plt
import cgi
import os

import cgitb
cgitb.enable()

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

#get physician id
link = cgi.FieldStorage()
physician_id = link["physician_id"].value

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
print("</h1>")
#emergency list path
emergency_path = "/home/wbagais/waiting_room_files/waiting_list/" 
emergency_path = emergency_path + str(physician_id) 
emergency_path = emergency_path + "/emergency_waiting_list.txt"
#other patients list path
other_path = "/home/wbagais/waiting_room_files/waiting_list/"
other_path = other_path + str(physician_id)
other_path = other_path + "/regular_waiting_list.txt"

#create the table
print('<table width="100%" border="1">')
print("<tr>")
print("<th>Patient ID</th>")
print("<th>Patient Name</th>")
print("<th>Service</th>")
print("<th>&nbsp;</th>")
print("</tr>")


#read emergency list
print_from_file(emergency_path)
print_from_file(other_path)

print("</table>")
#print the footer

f = open("/home/wbagais/waiting_room_files/footer.html", 'r')
transcript = f.read()
print(transcript)
f.close()
