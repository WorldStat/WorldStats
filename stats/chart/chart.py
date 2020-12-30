import sqlite3
import pandas
import csv
import matplotlib.pyplot as plt
from collections import Counter


'''Connecting to DB'''
conn = sqlite3.connect('../../db.sqlite3')
cursor = conn.cursor()

'''Retrieving all data to DF from DB'''
df = pandas.read_sql_query('SELECT * FROM data', conn)
print(df.shape)


count = df['GROUP1'].value_counts().drop([98])
chart_df = pandas.DataFrame(count)
questions = ['Sometimes', 'Rarely', 'Never', 'Often']
chart_df['Question'] = questions
#print(df['FITIN'].describe())
print(chart_df)

'''Creating a PLOT'''
chart_df.plot(rot=0, x='Question', kind='bar', figsize=(5, 5), color='#86bf91', zorder=2, width=0.85)
#plt.bar(count)
#plt.title('Histogram plot')
#plt.show()
plt.xlabel('Number of students', fontsize=18, fontname="Comic Sans MS",  color='darkcyan')
plt.ylabel('Answer', fontsize=16, fontname="Comic Sans MS", color='darkcyan')
plt.savefig('../../media/charts/Teens&Tech.png')



""" Another way to count occurances 
def count_els(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

print(count)
print(count_els(df['FITIN']))
"""


"""Retrieving data for creating a chart
x = cursor.execute('''SELECT CAST(FITIN AS INT)
FROM data;''').fetchall()

y = cursor.execute('''SELECT
CAST(FRIEND1 AS INT)
FROM data;''').fetchall()
"""
