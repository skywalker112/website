'''
Created on Dec 9, 2018

@author: bpr
'''
#-*- coding: utf-8 -*-

from url_info import *
import mysql.connector
from datetime import datetime


def createConnection():
    connection = mysql.connector.connect(host='localhost',
                             database='wiadomosci',
                             user='root',
                             password='')
    return connection
    
    
def addToDatabase(wydanie):
    
    try:
        connection = createConnection()
       
        records_to_insert = [wydanie.get()]
    
        sql_insert_query = """ INSERT INTO wydania (title, url, description, date) 
                              VALUES (%s,%s,%s,%s)"""
        
        cursor = connection.cursor(prepared=True)
        #used executemany to insert 3 rows
        result  = cursor.executemany(sql_insert_query, records_to_insert)
        connection.commit()
        print (cursor.rowcount, "Record inserted successfully into python_users table")
        
    except mysql.connector.Error as error :
        print("Failed inserting record into python_users table {}".format(error))
        
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("connection is closed")

        

def sendSqlCommand(sql_querry):
    
    result = []
    try:
        connection = createConnection()
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql_querry)
        res = cursor.fetchone() 
        for r in res:
            result.append(r)
        
    except mysql.connector.Error as error :
        print("Failed inserting record into python_users table {}".format(error))
        
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
        
    return result

def checkIfExist(value):
    querry = "SELECT COUNT(1) FROM wydania WHERE key = '" + value + "';'"
    
    sql = "SELECT COUNT(1) FROM wydania WHERE url='http://wiadomosci.tvp.pl/39971070/polska-gospodarka-to-pedzaca-lokomotywa'"
    
    
    print(querry)
    getIfExist = sendSqlCommand( sql )
    print(getIfExist)

#getAll = sendSqlCommand("SELECT * FROM wydania")
#checkIfExist(getOne().get()[1])



wydania = getAll()
print(len(wydania))

for wydanie in wydania:
    print("daje nowe")
    addToDatabase(wydanie)




   
   