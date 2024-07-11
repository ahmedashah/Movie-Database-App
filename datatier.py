# datatier.py
#
# Executes SQL queries against the given database.
#

import sqlite3


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# the first row retrieved by the query (or the empty
# tuple () if no data was retrieved). The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: first row retrieved by the given query, or
#          () if no data was retrieved. If an error
#          occurs, a msg is output and None is returned.
#
# NOTE: error message format is 
#   print("select_one_row failed:", err)
# where err is the Exception object.
#
def select_one_row(dbConn, sql, parameters = None):
  if parameters == None: #if nothing passed through 
    parameters = [] #an empty array is made 
    
  dbCursor = dbConn.cursor() #gets a cursor for the database connection

  try: 
    dbCursor.execute(sql, parameters) #passes the parameters for our search in this quary and reads the quary
    resultRow = dbCursor.fetchone() # gets the result of our search into row
    if (resultRow == None): # if nothing was retrived 
      return () # returns an empty tuple
    else:       
      return resultRow #if quary successfully searched outputs the result
    
  except Exception as err: # if an error happens and we handle it with an exception
    print("select_one_row failed:", err) #prints the error
    return None #nothing gets returned

  finally:
    dbCursor.close()  # closes the connection
    
    

##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# a list of rows retrieved by the query. If the query
# retrieves no data, the empty list [] is returned.
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: a list of 0 or more rows retrieved by the 
#          given query; if an error occurs a msg is 
#          output and None is returned.
#
# NOTE: error message format is 
#   print("select_n_rows failed:", err)
# where err is the Exception object.
#
def select_n_rows(dbConn, sql, parameters = None):
  dbCursor = dbConn.cursor() #gets a cursor for the database connection
    
  try: 
    if parameters == None:
      dbCursor.execute(sql) #if no parameters are passed
    else:
      dbCursor.execute(sql, parameters) #passes the parameters for our search in this quary and reads the quary
    resultRows = dbCursor.fetchall() # gets the result of our search into rows
    return resultRows #if quary successfully searched outputs the result
    
  except Exception as err: # if an error happens and we handle it with an exception
    print("select_n_rows failed:", err) #prints the error
    return None #nothing gets returned

  finally:
    dbCursor.close()  # closes the connection
    


##################################################################
#
# perform_action: 
# 
# Given a database connection and a SQL action query,
# executes this query and returns the # of rows
# modified; a return value of 0 means no rows were
# updated. Action queries are typically "insert", 
# "update", "delete". The query can be parameterized,
# in which case pass the values as a list via 
# parameters; this parameter is optional.
#
# Returns: the # of rows modified by the query; if an 
#          error occurs a msg is output and -1 is 
#          returned. Note that a return value of 0 is
#          not considered an error --- it means the
#          query did not change the database (e.g. 
#          because the where condition was false?).
#
# NOTE: error message format is 
#   print("perform_action failed:", err)
# where err is the Exception object.
#
def perform_action(dbConn, sql, parameters = None):

   dbCursor = dbConn.cursor() # get the cursor to retrieve rows
  
   try:   
    if parameters == None :## if no parameters were given
      dbCursor.execute(sql) # search quary without parameters
    else:      
      dbCursor.execute(sql,parameters) # search quary with parameters

    return dbCursor.rowcount # retrieves the number of rows and returns the count
    
     
   except Exception as err: #if an error happens
     print("perform_action failed:", err)
     return -1 # returns the error
     
   finally:
     dbCursor.close()
     

   
  

  
     
  
