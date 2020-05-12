#SQLite Intro
#creating DataBase Table
import sqlite3
import sys

#specify connection to the databse -
conn = sqlite3.connect("tutorial.db")
#specify the cursor - where to, what to do, what to grab ...
c = conn.cursor()

#create a table
def checkTable(tableName):
    try:
        c.execute("SELECT  * FROM " + tableName)
        return True
    except:
        return False

def createTable(tablename, col1, col2, col3):
    if not checkTable(tablename):
        c.execute("CREATE TABLE {} ({} VARCHAR, {} REAL, {} TEXT )".format(tablename, col1, col2, col3)) #floats = REAL
        #Language, Version and Skill are columns
    else:
        return ("Table not created. Table exists.")

def deleteTable(tablename):
    c.execute("DROP TABLE " + tablename)

def EnterData(tableName, var1, var2, var3):
    c.execute("INSERT INTO {}  VALUES('{}', {}, '{}')".format(tableName, var1, var2, var3))

def EnterDynamicData(tableName):
    lang = input("What language? ")
    version = float(input("Which version? "))
    skill = input("Skill level? ")

    c.execute("INSERT INTO {} (Language, Version, Skill) VALUES (?, ?, ?)".format(tableName), (lang, version, skill))

def read_from_db(tablename):
    column = input("What column do you want to search? ")
    value = input("What level of the column ? ")
    language = input("What language? ")
    sql = "SELECT * from {} where {} == ? AND Language == ?".format(tablename, column)
    for row in c.execute(sql, [(value), (language)]): #vprašaj je samo za stvari, ki morajo biti v '' - strings!
        print(row)
        print(row[0])

def selectAll(tablename):
    sql = "SELECT * FROM {} LIMIT 3".format(tablename)
    for row in c.execute(sql):
        print (row)

def update_columns(tablename, column):
    sql = "UPDATE {0} SET {1} == 'Noob' where {1} == 'Beginner'".format(tablename, column)
    c.execute(sql)
    selectAll(tablename)

def delete_from_table(tablename, column, value):
    sql = "DELETE FROM {} where {} == ?".format(tablename, column)
    c.execute(sql, [(value)])
    selectAll(tablename)

createTable("example", "Language", "Version", "Skill")
EnterData("example", "Python", 2.7, "Beginner")
EnterData("example", "Python", 3.3, "Intermediate")
EnterData("example", "Python", 3.5, "Expert")
EnterDynamicData("example")

selectAll("example")
delete_from_table("example", "Skill", "Expert")

# read_from_db("example", "Skill", "Beginner")
read_from_db("example")

update_columns("example", "Skill")

conn.commit() #save without closing the connection
#conn.close()


#URLIB Module
import urllib.request

req = urllib.request.urlopen('https://www.google.com')
print(req.read())


#XML
#RSS FEED
#PARSE --> you can store it as a string and split it
#or use BeautifulSoup

from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen("http://rss.slashdot.org/Slashdot/slashdotMain")
xml = BeautifulSoup(req, 'lxml')


for item in xml.findAll('link')[3:]:
    #print(item.text) #you add .text if you want the text without TAGS
    url = item.text
    news = urllib.request.urlopen(url).read()
    print(news)
    print(20*"#")