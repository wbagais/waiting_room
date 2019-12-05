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

start_time = datetime.now()

#print the header
f = open("/home/wbagais/waiting_room_files/header_1.html", 'r')
transcript = f.read()
print(transcript)
f.close()
#print page name
print("Patient Page")
#print the rest of the header
f = open("/home/wbagais/waiting_room_files/header_2.html", 'r')
transcript = f.read()
print(transcript)
f.close()

#read the data from cgi.FieldStorage
link = cgi.FieldStorage()
physician_id = link["physician_id"].value
patient_id =  link["patient_id"].value
service_id = link["service_id"].value

#connect to the database
conn = sqlite3.connect('/home/wbagais/waiting_room_files/waiting_room_db.db')
cursor = conn.cursor()

#select the patient information
sql = "SELECT fname, lname, six, dob "
sql = sql + "FROM patient WHERE patient_id  = "
sql = sql + patient_id + ";"

cursor.execute(sql)
patient_result = cursor.fetchone()

#select the patient visit history
sql = "SELECT patient_id, physician_id, service_id, date, comment "
sql = sql + "FROM visit WHERE patient_id  = "
sql = sql + patient_id + ";"

cursor.execute(sql)
visit_result = cursor.fetchall()

#select service id
sql = "SELECT name from service WHERE service_id = '"
sql = sql + service_id + "'"

cursor.execute(sql)
service_result = cursor.fetchone()
service = service_result[0]


#print the html for the begining of the main section
print('<section class="offered-service-area dep-offred-service">')
print('<div class="container">')
print('<div class="row offred-wrap section-gap">')
print('<div class="col-lg-8 offered-left">')

#check if the patient has visits history
if(len(visit_result) <= 0):
    print('<h1>this is the Patient First Visit</h1>')
else:
    # print patient records
    print('<h1>Patient visits history</h1>')
    print('<table width="100%" border="1">')
    print('<tr>')
    print('<th>Visit Date</th>')
    print('<th>Pysician</th>')
    print('<th>Service</th>')
    print('<th>Comment</th>')
    print('</tr>')

    visit_sql = "SELECT date, physician_id, service_id, comment FROM visit WHERE patient_id='" 
    visit_sql = visit_sql + patient_id+"'" 

    cursor.execute(visit_sql)
    visit_result = cursor.fetchall()
    for visit in visit_result:
        #TODO read the history of the patient
        print('<tr>')
        print('<td>')
        print(visit[0])
        print('</td>')

        physician_sql = "SELECT fname, lname FROM physician WHERE physician_id = '" + str(visit[1]) +"'"
        cursor.execute(physician_sql)
        physician = cursor.fetchone()
        print("<td>")
        print(physician[0] , " ", physician[1])
        print("</td>")

        service_sql = "SELECT name FROM service WHERE service_id = " + str(visit[2])
        cursor.execute(service_sql)
        service_result = cursor.fetchone()
        print("<td>")
        print(service_result[0])
        print("</td>")

        print('<td>')
        print(visit[3])
        print('</td>')
        print('</tr>')

print('</table>')

#current visit details
print('<h1 class="pt-120">Current Visit</h1>')
print('<br/>')
print('<table width=35%>')
print('<tr><th><h4><b>Survice:</b></h4></th>')
print('<th>')
print(service)
print('</th></tr></table>')

print('<br/>')
print('<h4><b>Comment:</b></h4>')

action_url = "http://students.hi.gmu.edu/cgi-bin/wbagais/patient_list.cgi?physician_id=" + physician_id 

##form
print('<form class="form-wrap" id="comment_form" action="', action_url,'"  method="POST">')
#TODO add form atributes
print('<textarea rows="5" cols="70" name="comment" form = "comment_form"> Enter text here...</textarea>')
print('<br/>')
print(' <input type="hidden" id="start_time" name="start_time" value="' + start_time.strftime("%H:%M:%S")  + '">')
print(' <input type="hidden" id="patient_id" name="patient_id" value="' + patient_id  + '">')
print(' <input type="hidden" id="service_id" name="service_id" value="' + str(service_id)  + '">')

#service_id
print('<button class="primary-btn text-uppercase">Confirm</button>')
print('</form>')

#layout format
print('</div>')
print('<div class="col-lg-4">')

############################################################
print('<div class=" appointment-left sidebar-service-hr ">')
print('<h3 class="pb-20">Patient Information</h3>')

#print patient info
print('<ul class="time-list">')

print('<li class="d-flex justify-content-between">')
print("<span><b>Patient Name</b></span>")
print("<span>")
print(patient_result[0] ," ", patient_result[1])
print("</span></li>")

print('<li class="d-flex justify-content-between">')
print("<span><b>Sex</b></span>")
print("<span>")
if (patient_result[2] == 'F'):
    print("Female")
elif(patient_result[2] == 'M'):
    print("Male")
print("</span></li>")

print('<li class="d-flex justify-content-between">')
print("<span><b>Date of birth</b></span>")
print("<span>")
print(patient_result[3])
print("</span></li>")
print("</li></ul></div></div></div></div></section>")

#print the footer
f = open("/home/wbagais/waiting_room_files/footer.html", 'r')
transcript = f.read()
print(transcript)
f.close()
