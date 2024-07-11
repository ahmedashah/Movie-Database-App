# Ahmed Shah - CS 341 Project 2 Part 2
# File: objecttier.py
#
# objecttier
#
# Builds Movie-related objects from data retrieved through
# the data tier.
#
# Original author:
#   Prof. Joe Hummel
#   U. of Illinois, Chicago
#   CS 341, Spring 2022
#   Project #02
#
import datatier


##################################################################
#
# Movie:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#
class Movie:
  #pass
  # setting up a parametrized constructor to set up the Movie Object being made
  def __init__(self, movieID, title, releaseYear):
    self._Movie_ID = movieID  #assigning the movie object an ID
    self._Title = title  #assigning the movie object a title
    self._Release_Year = releaseYear  #assigning the movue object a release Year

  @property
  def Movie_ID(self):  #getter for the movie Id
    return self._Movie_ID

  @property
  def Title(self):  #getter for the title of the movie
    return self._Title

  @property
  def Release_Year(self):  #getter for Release Date for the film
    return self._Release_Year


##################################################################
#
# MovieRating:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Year: string
#   Num_Reviews: int
#   Avg_Rating: float
#
class MovieRating:
  #pass
  #setting a parametrized constructor for a MovieRating object being made
  def __init__(self, movieID, title, releaseYear, numReviews, avgRating):
    self._Movie_ID = movieID
    self._Title = title
    self._Release_Year = releaseYear
    self._Num_Reviews = numReviews
    self._Avg_Rating = avgRating

  @property
  def Movie_ID(self):  # getter function for Movie ID
    return self._Movie_ID

  @property
  def Title(self):  # getter function for Title
    return self._Title

  @property
  def Release_Year(self):  # getter function for Release Year
    return self._Release_Year

  @property
  def Num_Reviews(self):  # getter function for Number of Reviews
    return self._Num_Reviews

  @property
  def Avg_Rating(self):  # getter function for Average Rating
    return self._Avg_Rating


##################################################################
#
# MovieDetails:
#
# Constructor(...)
# Properties:
#   Movie_ID: int
#   Title: string
#   Release_Date: string, date only (no time)
#   Runtime: int (minutes)
#   Original_Language: string
#   Budget: int (USD)
#   Revenue: int (USD)
#   Num_Reviews: int
#   Avg_Rating: float
#   Tagline: string
#   Genres: list of string
#   Production_Companies: list of string
#
class MovieDetails:
  #pass
  def __init__(self, movieID, title, releaseDate, runtime, origLanguage,
               budget, revenue, numReviews, avgRating, tagline, genres,
               prodComp):
    self._Movie_ID = movieID
    self._Title = title
    self._Release_Date = releaseDate
    self._Runtime = runtime
    self._Original_Language = origLanguage
    self._Budget = budget
    self._Revenue = revenue
    self._Num_Reviews = numReviews
    self._Avg_Rating = avgRating
    self._Tagline = tagline
    self._Genres = genres
    self._Production_Companies = prodComp

  @property
  def Movie_ID(self):  # getter for Movie ID
    return self._Movie_ID

  @property
  def Title(self):  # getter for Title
    return self._Title

  @property
  def Release_Date(self):  # getter for Release Date
    return self._Release_Date

  @property
  def Runtime(self):  # getter for Runtime
    return self._Runtime

  @property
  def Original_Language(self):  # getter for Original_Language
    return self._Original_Language

  @property
  def Budget(self):  # getter for Budget
    return self._Budget

  @property
  def Revenue(self):  # getter for Revenue
    return self._Revenue

  @property
  def Num_Reviews(self):  # getter for Num_Reviews
    return self._Num_Reviews

  @property
  def Avg_Rating(self):  # getter for Avg_Rating
    return self._Avg_Rating

  @property
  def Tagline(self):  # getter for Tagline
    return self._Tagline

  @property
  def Genres(self):  # getter for Genres
    return self._Genres

  @property
  def Production_Companies(self):  # getter for Production_Companies
    return self._Production_Companies


##################################################################
#
# num_movies:
#
# Returns: # of movies in the database; if an error returns -1
#
def num_movies(dbConn):
  #pass
  sqlQuary = """SELECT COUNT(Movie_ID) FROM Movies"""  # Quary to retriev count of all
  try:  #try block to ensure if something goes wrong, it gets handled
    count = ((datatier.select_one_row(dbConn, sqlQuary))[0])
      # calls the select_one_row to retrieve data. Indexed at [0] to properly retrieve the count number from a row
    return count  # returns the count
  except Exception:
    #print("num_movies failed:", err) #prints the error
    return -1


##################################################################
#
# num_reviews:
#
# Returns: # of reviews in the database; if an error returns -1
#
def num_reviews(dbConn):
  #pass
  sqlQuary = """SELECT COUNT(Movie_ID) FROM Ratings"""  # Quary to retrieve count of all
  try:  #try block to ensure if something goes wrong, it gets handled
    count = (
      (datatier.select_one_row(dbConn, sqlQuary))[0]
    )  # calls the select_one_row to retrieve data. Indexed at [0] to properly retrieve the count number from a row
    return count  # returns the count
  except Exception:
    #print("num_reviews failed:", err) #prints the error
    return -1


##################################################################
#
# get_movies:
#
# gets and returns all movies whose name are "like"
# the pattern. Patterns are based on SQL, which allow
# the _ and % wildcards. Pass "%" to get all stations.
#
# Returns: list of movies in ascending order by name;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_movies(dbConn, pattern):
  #pass
  #Sql quary to retrieve the film names/titles by the pattern
  sqlQuary = """SELECT Movie_ID ,Title, Strftime('%Y', Release_Date) As "Release_Year"  
                FROM MOVIES
                WHERE Title LIKE ?
                ORDER BY Movie_ID asc;"""
  rows = datatier.select_n_rows(dbConn, sqlQuary,
                                [pattern])  #retrieve data from quary
  movies = [
  ]  #create an array to store the movies names since rows is a 2D array with only one column

  for row in rows:
    movieBefore = Movie(row[0], row[1], row[2])
    movies.append(movieBefore)  #adds film titles to the array

  return movies  # return the complete array


##################################################################
#
# get_movie_details:
#
# gets and returns details about the given movie; you pass
# the movie id, function returns a MovieDetails object. Returns
# None if no movie was found with this id.
#
# Returns: if the search was successful, a MovieDetails obj
#          is returned. If the search did not find a matching
#          movie, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_movie_details(dbConn, movie_id):

  try:
    # Get everything we need from the movies table and the tagname 
    #the ifnulls on the select just is a checker is anything is null and inputs data at the null spots
    sqlQuary1 = """SELECT DISTINCT Movies.Movie_ID, Title, DATE(Release_Date), Runtime, Original_Language, Budget, Revenue, IFNULL(COUNT(Ratings.Rating), 0), IFNULL(AVG(Ratings.Rating), 0.0), IFNULL(Movie_Taglines.Tagline, "") FROM Movies
                  LEFT JOIN Ratings ON Ratings.Movie_ID = Movies.Movie_ID  
                  LEFT JOIN Movie_Taglines ON  Movie_Taglines.Movie_ID= Movies.Movie_ID 
                  WHERE Movies.Movie_ID = ?
                  GROUP BY Ratings.Movie_ID;          
    """
    #Query to get the genres of a film
    sqlQuary2 = """SELECT DISTINCT Genres.Genre_Name FROM Genres
                  JOIN Movie_Genres ON Movie_Genres.Genre_ID = Genres.Genre_ID 
                  WHERE Movie_Genres.Movie_ID = ?
                  ORDER BY Genre_Name asc;"""
    #Query to get the production company of a film
    sqlQuary3 = """SELECT DISTINCT Company_Name FROM Companies
                    JOIN Movie_Production_Companies ON Movie_Production_Companies.Company_ID = Companies.Company_ID
                    WHERE Movie_Production_Companies.Movie_ID = ?
                    ORDER BY Company_Name asc;"""

    row = datatier.select_one_row(dbConn, sqlQuary1, [movie_id]) # data retrival from movies table and tagline
    rows2 = datatier.select_n_rows(dbConn, sqlQuary2, [movie_id]) # gets the genres
    rows3 = datatier.select_n_rows(dbConn, sqlQuary3, [movie_id]) # gets the production company 

    if (row == ()):  #movie doesn't exist
      return None
 
    genres = [] # gets all the genres in a list 
    for rowGenre in rows2:
      genres.append(rowGenre[0])

    companies = [] # gets all the production company in a list
    for rowCompany in rows3:
      companies.append(rowCompany[0])     

    return MovieDetails(row[0], row[1], row[2], row[3], row[4], row[5], row[6], 
                        row[7], row[8], row[9], genres, companies) # put everything in the parameters

  except Exception:
    return None


##################################################################
#
# get_top_N_movies:
#
# gets and returns the top N movies based on their average
# rating, where each movie has at least the specified # of
# reviews. Example: pass (10, 100) to get the top 10 movies
# with at least 100 reviews.
#
# Returns: returns a list of 0 or more MovieRating objects;
#          the list could be empty if the min # of reviews
#          is too high. An empty list is also returned if
#          an internal error occurs (in which case an error
#          msg is already output).
#
def get_top_N_movies(dbConn, N, min_num_reviews):
  # sql query to retrieve all the arguments to make a Movie Rating object 
  sql = """SELECT Movies.Movie_ID, Title, Strftime('%Y', Release_Date) As "Release_Year", COUNT(Ratings.Rating), AVG(Ratings.Rating) FROM Movies
            JOIN Ratings ON Ratings.Movie_ID = Movies.Movie_ID 
            GROUP BY Movies.Movie_ID
            HAVING COUNT(Rating) >= ?
            ORDER BY AVG(Rating) desc
            LIMIT ? ;"""
  #retrieves the data from the query
  rows = datatier.select_n_rows(dbConn, sql, [min_num_reviews, N])
  list = []
  if not rows: # returns out if no data was retrieved
    return list
  for row in rows: # constructs a MovieRating object with the parameter
    list.append(MovieRating(row[0], row[1], row[2], row[3], row[4])) # and then append it to a list
  return list 


##################################################################
#
# add_review:
#
# Inserts the given review --- a rating value 0..10 --- into
# the database for the given movie. It is considered an error
# if the movie does not exist (see below), and the review is
# not inserted.
#
# Returns: 1 if the review was successfully added, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def add_review(dbConn, movie_id, rating):
  #query to check if the movie id entered actually even exists or not in the database
  sqlSearch = """SELECT Movie_ID FROM Movies
                 WHERE Movie_ID = ?
                 GROUP BY Movie_ID ;"""
  result = datatier.select_one_row(dbConn, sqlSearch, [movie_id]) 
  if (result == ()): #if the movie id is not in the list then returns a 0
    return 0
  #query to insert into the ratings table
  sqlInsert = """Insert Into Ratings(Movie_ID, Rating) Values(?,?) ;"""
  insertCheck = datatier.perform_action(dbConn, sqlInsert, [movie_id, rating]) 
  #performs the insert
  if insertCheck == -1 : #checks if the insert happened. Error checking
    return 0
  else:
    dbConn.commit() # saves the insert 
    return 1


##################################################################
#
# set_tagline:
#
# Sets the tagline --- summary --- for the given movie. If
# the movie already has a tagline, it will be replaced by
# this new value. Passing a tagline of "" effectively
# deletes the existing tagline. It is considered an error
# if the movie does not exist (see below), and the tagline
# is not set.
#
# Returns: 1 if the tagline was successfully set, returns
#          0 if not (e.g. if the movie does not exist, or if
#          an internal error occurred).
#
def set_tagline(dbConn, movie_id, tagline):
  #Checks if the movie actually even exists in the database  
  sqlQuary1 = """SELECT Movie_ID FROM Movies WHERE Movie_ID = ? ;"""
  row = datatier.select_one_row(dbConn, sqlQuary1, [movie_id])
  if (row == ()): # if the movie id is not in the database
    return 0
  #checks to see if it already has a tagline
  sqlQuary2 = """SELECT Movie_ID FROM Movie_Taglines WHERE Movie_ID = ? ;"""
  row2 = datatier.select_one_row(dbConn, sqlQuary2, [movie_id])

  if (row2 == ()): #if tagline doesnt exist
    sqlInsert = """Insert Into Movie_Taglines(Movie_ID, Tagline) Values(?,?) ;"""
    insertCheck = datatier.perform_action(dbConn, sqlInsert,
                                          [movie_id, tagline]) #inserts the tagline in the database
    if (insertCheck == -1): #if the insert didnt work, outputs 0 as error checking
      return 0
    else:
      dbConn.commit() #saves the insertion
      return 1
  #if tagline already exists then we update the tagline with the input
  #sql query for updating the tagline
  sqlUpdate = """Update Movie_Taglines
                   Set Tagline = ?
                   WHERE Movie_ID = ? ; 
                    """
  #performs the update 
  updateCheck = datatier.perform_action(dbConn, sqlUpdate, [tagline, movie_id]) 
  if (updateCheck == -1): #if tagline was not updated. error checking
    return 0
  else:
    dbConn.commit() #saves the update
    return 1
