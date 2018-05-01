# Andrea Leon, Eliana Marostica, and Parul Kohl
# CS304 Final Project: Wellesley Project Database
# updateDB.py
# created 4/29/2018
#!/usr/local/bin/python2.7


import sys
import MySQLdb
import dbconn2

# ================================================================
# The functions that do most of the work.  

#TO DO: Insert Functions Below

def checkUser(conn, email):
	'''Finds if user exists in user table based on email
		By: Eliana Marostica'''
	curs = conn.cursor(MySQLdb.cursors.DictCursor)
	curs.execute('SELECT email FROM user WHERE email = %s', [email])
	return curs.fetchone()

# def addProject(conn, projCreator, projName, projDur, projComp, projRoles, projReq, projDesc)
#	'''Adds project to project table
#		by: Andrea Leon'''
# 	curs = conn.cursor(MySQLdb.cursors.DictCursor) # results as Dictionaries
#     curs.execute('insert into project (creator, name, compensation, rolesOpen, \
#     	description, duration) values (%s, %s, %s, %s, %s, %s)', [projCreator, \
#     	projName, projDur, projComp, projRoles, projReq, projDesc])
#     return "Project created"

def addUser(conn, email, name, role, hashed):
	'''Adds a user to the user table
		By: Eliana Marostica'''
	curs = conn.cursor(MySQLdb.cursors.DictCursor)
	curs.execute('INSERT into user(email,name,role,hashed) VALUES(%s,%s,%s,%s)', [email, name, role, hashed])

def fetchHashed(conn, email):
	'''Retrieves the password hash for a user based on email
		By: Eliana Marostica'''
	curs = conn.cursor(MySQLdb.cursors.DictCursor)
	curs.execute('SELECT hashed FROM user WHERE email = %s', [email])
	return curs.fetchone()

def getUID(conn, email):
	'''Returns user's uid from user table based on provided email
		By: Eliana Marostica'''
	curs = conn.cursor(MySQLdb.cursors.DictCursor)
	curs.execute('SELECT uid FROM user WHERE email = %s', [email])
	row = curs.fetchone()
	return row['uid']

def getName(conn, email):
	'''Returns user's name from user table based on their email
		By: Eliana Marostica'''
	curs = conn.cursor(MySQLdb.cursors.DictCursor)
	curs.execute('SELECT name FROM user WHERE email = %s', [email])
	row = curs.fetchone()
	return row['name']

>>>>>>> 752342286e9998ca746e8a6a7e02675267d6b9e9


# ================================================================
# This starts the ball rolling, *if* the script is run as a script,
# rather than just being imported.    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: {name} nm".format(name=sys.argv[0])
    else:
        DSN = dbconn2.read_cnf()
        DSN['db'] = 'wprojdb_db'     # the database we want to connect to
        dbconn2.connect(DSN)
        print lookupByNM(sys.argv[1])