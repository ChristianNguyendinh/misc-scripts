import sqlite3
import sys
from bs4 import BeautifulSoup

# ==================================================================
# Very simple sqlite practice. Reads in data from an html
# table, then inputes the data into a sqlite databse
# Requries BeautifulSoup4 and sqlite3
# ==================================================================

data_file = open("test.html", "r") # open data file for reading

soup = BeautifulSoup(data_file, 'html.parser') # scrape

data_file.close()

results = soup.find_all("tr", class_="user") # get data for each desired row

db_conn = sqlite3.connect('test.db') # connect to DB. Create if doesn't exist


with db_conn:
	db_conn.execute("DROP TABLE IF EXISTS Students") # start fresh
	db_conn.commit()

	try:
		# Create table for our data
		db_conn.execute("CREATE TABLE Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FirstName TEXT NOT NULL, LastName TEXT NOT NULL, Class TEXT NOT NULL, Section TEXT NOT NULL, Role TEXT NOT NULL);")	
		db_conn.commit()
		print("Table Created")

	except:
		print("Table couldn't be Created")


	print("Inserting into Table...")

	for i in results:
		# Gather Data from html page

		curr = i.find("a", class_="name")
		#print(curr.contents[0])
		name_list = curr.contents[0].split(" ", 1) # Split into first and last names
		first_name = name_list[0]
		last_name = name_list[1]

		
		class_info = curr.parent.next_sibling.next_sibling.find("div", class_="section") # extra nextsibling because technically the newline is the next sibling
		info_list = class_info.contents[0].split("-", 1) 
		#print(info_list[0])
		#print(info_list[1])
		class_name = info_list[0]
		section_name = info_list[1]
		
		status = class_info.parent.next_sibling.next_sibling.find("div")
		#print(status.contents[0])
		status_name = status.contents[0]

		# Load info for this student into the DB
		db_conn.execute("INSERT INTO Students (FirstName, LastName, Class, Section, Role)"
						"VALUES ('" + first_name + "', '" + last_name + "', '" + class_name + "', '" + section_name + "', '" + status_name + "')")
		db_conn.commit()

# Close the DB connection
db_conn.close()
print("db closed")

