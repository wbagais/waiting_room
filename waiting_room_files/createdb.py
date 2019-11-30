#!/bin/python3

import sqlite3
import pandas as pd
from matplotlib import pyplot as plt

print('create a empty database ')
conn = sqlite3.connect('/home/wbagais/waiting_room_files/waiting_room_db.db')
print('/home/wbagais/waiting_room_db.db is created')
print('read from csv and then add it to new_db.db')
#create patient table
patient_df = pd.read_csv('/home/wbagais/waiting_room_files/patient.csv')
patient_df.to_sql(name = "patient", con = conn, index = True, index_label = 'id')
print('table patient is added to/home/wbagais/waiting_room_files/waiting_room_db.db')
#create physician table
physician_df = pd.read_csv('/home/wbagais/waiting_room_files/physician.csv')
physician_df.to_sql(name = "physician", con = conn, index = True, index_label = 'id')
print('table physician is added to /home/wbagais/waiting_room_files/waiting_room_db.db')
#create service table
service_df = pd.read_csv('/home/wbagais/waiting_room_files/service.csv')
service_df.to_sql(name = "service", con = conn, index = True, index_label = 'id')
print('table service is added to //home/wbagais/waiting_room_files/waiting_room_db.db')
# create visit table
visit_df = pd.read_csv('/home/wbagais/waiting_room_files/visit.csv')
visit_df.to_sql(name = "visit", con = conn, index = True, index_label = 'id')
print('table visit is added to /home/wbagais/waiting_room_files/waiting_room_db.db')


print('read the first row of patient:')
cursor = conn.cursor()
cursor.execute("SELECT * FROM patient LIMIT 1;")
print(cursor.fetchall())

print('read the first row of physician:')
cursor = conn.cursor()
cursor.execute("SELECT * FROM physician LIMIT 1;")
print(cursor.fetchall())

print('read the first row of service:')
cursor = conn.cursor()
cursor.execute("SELECT * FROM service LIMIT 1;")
print(cursor.fetchall())


print('read the first row of visit:')
cursor = conn.cursor()
cursor.execute("SELECT * FROM visit LIMIT 1;")
print(cursor.fetchall())
