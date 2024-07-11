#CS 341 Project 2
#Name: Ahmed Shah
#Console based Python program using input commands to retrieve data from
#the SQL MovieLens database
import sqlite3
import objecttier

#prints the data with no. of movies and reviews
def print_stats(dbConn) :
  numMovies = objecttier.num_movies(dbConn)   
  numReviews = objecttier.num_reviews(dbConn)

  print("General stats:")
  print(f"  # of movies: {numMovies:,}")
  print(f"  # of reviews: {numReviews:,}")
  return

#Prints all the movies in a list with the Release Year 
def PrintMovieFromList(movieList):
  for movie in movieList:
    print(f"{movie.Movie_ID} : {movie.Title} ({movie.Release_Year})")
  return

#Builds the string for Genres and Production Companies
def BuildStringFromList(listString):
  baseString = ""
  for eachString in listString:
    baseString = baseString + eachString + ", "
  return baseString

#Prints all the information on a film in the database
def PrintDetails(filmDetails): 
  print(f"\n{filmDetails.Movie_ID} : {filmDetails.Title}")
  print(f" Release date: {filmDetails.Release_Date}")
  print(f" Runtime: {filmDetails.Runtime} (mins)")
  print(f" Orig language: {filmDetails.Original_Language}")
  print(f" Budget: ${filmDetails.Budget:,} (USD)")
  print(f" Revenue: ${filmDetails.Revenue:,} (USD)")
  print(f" Num reviews: {filmDetails.Num_Reviews}")
  print(f" Avg rating: {filmDetails.Avg_Rating:.2f} (0..10)")
  genreString = BuildStringFromList(filmDetails.Genres)
  print(f" Genres: {genreString}")
  proCompString = BuildStringFromList(filmDetails.Production_Companies)
  print(f" Production companies: {proCompString}")
  print(f" Tagline: {filmDetails.Tagline}")

  return

 #Prints all the top N movies with their avg and total number of ratings
def PrintTopNMoies(movieList):
  for movieRating in movieList:
    print(f"{movieRating.Movie_ID} : {movieRating.Title} ({movieRating.Release_Year}), avg rating = "f"{movieRating.Avg_Rating:.2f}"f" ({movieRating.Num_Reviews} reviews)")
  return    
  

    
#########################################################################
### All commands of the Program  

#Enter a film name or a pattern name and outputs all the names with pattern
def Command1(dbConn): 
  pattern = input("\nEnter movie name (wildcards _ and % supported): ")
  movieList = objecttier.get_movies(dbConn, pattern) #calls the get movies function from the objecttier file
  count = len(movieList) 
  print("\n# of movies found:", count) # prints the total number of movies with the pattern
  if(len(movieList)>100):
    print("There are too many movies to display, please narrow your search and try again...")
    return
    
  if (len(movieList) >0):
    print()
    PrintMovieFromList(movieList) # calls the print movie helper function 
  return 


#input a specific movieID and outputs detailed movie information about this movie --- tagline, budget, revenue, genres, etc.
def Command2(dbConn):
  movieID = input("\nEnter movie id: ") 
  filmDetails = objecttier.get_movie_details(dbConn, movieID)
#grabs the film details object from the objecttier 
  if filmDetails is None: #if invalid id inputted
    print("\nNo such movie...")
    return 
  PrintDetails(filmDetails) #Uses the helper function


#Lists out the most N movies bounded by specific least number of reviews
def Command3(dbConn):
  N = int(input("\nN? ")) 
  if (N <= 0): #if invalid minimum reviews inputted
    print("Please enter a positive value for N...")
    return
  
  min_num = int(input("min number of reviews? "))
  if (min_num < 1): #if invalid minimum reviews inputted
    print("Please enter a positive value for min number of reviews...")
    return
#calls topNMovies function from the objecttier
  
  movieList = objecttier.get_top_N_movies(dbConn,N,min_num) 
  if(len(movieList) > 0):
    print()
    PrintTopNMoies(movieList)
    

  #adds a review into the database for a film
def Command4(dbConn):
  rating = int(input("\nEnter rating (0..10): "))
  if ((rating < 0) or (rating >10)) : #if invalid input is added
    print("Invalid rating...")
    return

  movieID = int(input("Enter movie id: "))
  insertStatus = objecttier.add_review(dbConn,movieID,rating)
#uses objecttier's add review function to add a review
  if insertStatus == 0 : #if invalid movie was inputted 
    print("\nNo such movie...")
    return
  elif insertStatus == 1: #if everything went right 
    print("\nReview successfully inserted")
    return

  
#adds a tagline or updates a movies tagline
def Command5(dbConn):
  tagline = input("\ntagline? ")
  movieID = input("movie id? ")
  #uses the objecttier's set tagline function 
  taglineInsert = objecttier.set_tagline(dbConn,movieID,tagline)
  if taglineInsert == 0: #if invalid movie id was entered
    print("\nNo such movie...")
    return
  elif taglineInsert == 1: #if everything went right
    print("\nTagline successfully set")
    return


##################################################################  
#
# main
#
print("** Welcome to the MovieLens app **\n")
dbConn = sqlite3.connect('MovieLens.db') #get conncected with the MovieLens database
print_stats(dbConn)#function call for the display

loopRun = True # the condition to run our command menu 
while loopRun == True:
  #Prompt user input to pick a command
  command = input("\nPlease enter a command (1-5, x to exit): ")
  
######################################################################
##########Command X Exit the Loop
  if command ==  'x': #ends the program
    loopRun = False #condition to run the loop is no more

######################################################################
##########Command 1
  elif command == '1':
    Command1(dbConn)
  ######################################################################
##########Command 1
  elif command == '2':
    Command2(dbConn)
    ######################################################################
##########Command 3
  elif command == '3':
    Command3(dbConn)
    ######################################################################
##########Command 4
  elif command == '4':
    Command4(dbConn)
    ######################################################################
##########Command 5
  elif command == '5':
    Command5(dbConn)


    



