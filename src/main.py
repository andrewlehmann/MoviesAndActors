from GetMoviesFromActor import *
from GetReviews import *


def main_menu():
	print("Hi welcome to: What Were They In And Is It any Good! \n \n")
	print("Press one to search by Actor/Actress! \n")
	print("Press two to search by Movie! \n")
	print("Press three to Exit! \n")
	answer = input("Please enter your choice(1,2,3): ")
	
	#the different options
	if answer == "1":
	  print("\n")
	  name = input("Please enter a name you would like to search: ")
	  print("\n")
	  print(get_movies_by_actor(name))
	  print("\n")
	  check = input("Enter a movie name to check review: ")
	  print("The movie got a score of: ", reviewScore(check))
	  print("\n")
	  return main_menu() 
	elif answer == "2":
	  print("\n")
	  movie = input("Please enter a movie name: ")
	  print("\n")
	  print("The movie got a score of: ", reviewScore(movie))
	  print("\n")
	  return main_menu()
	elif answer == "3":
	  print("So Long Have A Good Day!")
	  return 0
	else:
		print("Oh that was not something I could understand! /n")
		return main_menu()
		
		
		
		
		
main_menu()

