import sqlite3
import pandas
import csv
import matplotlib.pyplot as plt
from collections import Counter

'''Connecting to DB'''
conn = sqlite3.connect('../../db.sqlite3')
cursor = conn.cursor()

'''Creating a Database for storing research values from .csv'''
data = pandas.read_csv('../../worldstats/TeensandTech.csv')

'''Creating a table using data from .csv file'''
#cursor.execute('''CREATE TABLE TeensTech (CASEID, FITIN, FRIEND1)''')
data.to_sql('data', conn, if_exists = 'append', index = False)


