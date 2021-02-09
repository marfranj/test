# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:45:22 2018

@author: Marc.Ciamaichelo
"""
import pyodbc 
import os
import pandas as pd
import time

# =============================================================================
# #testVar = input("Blah")
# this input function literally allows you to input something manually into the list during the execution of the program
# test = 'Blah'
# print(test)
# =============================================================================

con = pyodbc.connect(DRIVER='{SQL Server}',Server='BLMJGH2\SQLEXPRESS',database = 'TestDB',Trusted_Connection='yes')

cur = con.cursor()

main_table = "main_table"
temp_table = "temp_table"
table_list = [main_table, temp_table]
#print(table_list[0])
table_list2 = '[Customers], [bulk_prac]'

for i in range(0, len(table_list)):
    SQLCommand = ("""
           DELETE FROM """ + str(table_list[i]) + """
           WHERE [Residue Skin Left Temperature - TimeAverage2] IS NOT NULL
           """)
    cur.execute(SQLCommand)

con.commit()

con.close()

