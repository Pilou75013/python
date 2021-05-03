###The price is right


# import random

# r=random.randint(0, 101)
# tries=42

# print("Find the number between 0 & 101")
# while True:
#     response = input()
#     if int(response) == r:
#         print("Congatz'")
#         break
#     else:
#         if int(response) > r:
#             print("Less")
#             tries = tries - 1
#         else:
#             print("More")
#             tries = tries -1
#print("End oh the game")

###Chifumi

# import random

# #score
# user_score = 0
# cp_score = 0

# #asking number of rounds
# user_nb_round = int(input('How many rounds ? '))
# nb_round = 0
# while (nb_round < user_nb_round):

# 	#user choice
# 	user_choice = input('Choose between Rock, Paper & Scissors : ')
# 	if(user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors'):

# 		#separation rounds
# 		print('--------------------------')

# 		#computer's choice
# 		can_use = ['rock', 'paper', 'scissors']
# 		cp_choice = random.choice(can_use)

# 		#show computer's choice
# 		print('Computer chooses : ', cp_choice)

# 		#game algorythm
# 		if(user_choice == cp_choice):
# 			print('Par')
# 		elif(user_choice == 'rock' and cp_choice == 'paper'):
# 			print('Computer wins !')
# 			cp_score = cp_score + 1
# 		elif(user_choice == 'rock' and cp_choice == 'scissors'):
# 			print('Player wins')
# 			user_score = user_score + 1
# 		elif(user_choice == 'paper' and cp_choice == 'rock'):
# 			print('Player wins')
# 			user_score = user_score + 1
# 		elif(user_choice == 'paper' and cp_choice == 'scissors'):
# 			print('Computer wins !')
# 			cp_score = cp_score + 1
# 		elif(user_choice == 'scissors' and cp_choice == 'rock'):
# 			print('Computer wins !')
# 			cp_score = cp_score + 1
# 		elif(user_choice == 'scissors' and cp_choice == 'paper'):
# 			print('Player wins !')
# 			user_score = user_score + 1

# 		nb_round = nb_round + 1
# 		print('Round number ', nb_round, ' of ', user_nb_round)

# 		#Show score
# 		print('You have ', user_score, ' points')
# 		print('Computer have ', cp_score, ' points')

# 	else:
# 		print('I can\'t understand...')

# #determine the win
# if(user_score > cp_score):
# 	print('------You\'ve defaited the Computer ! :)------')
# elif(cp_score > user_score):
# 	print('------You\'ve lost against the Computer :(------')
# else:
# 	print('------It ends in a draw :/------')

###Hanged Man

# import random
# choice = ["python", "project"]
# solution = random.choice(choice)

# solution = "python"
# attempt = 7
# view = ""
# found_letters = ""

# for l in solution:
# view = view + "_ "

# print(">> Welcome to the hanged man <<")

# while attempt > 0:
# print("\nWord to guess : ", view)
# proposition = input("Suggest a letter : ")[0:1].lower()

# if proposition in solution:
#     found_letters = found_letters + proposition
#     print("-> Well done!")
# else:
#     attempt = attempt - 1
#     print("-> Nope", int(attempt))
    

# view = ""
# for x in solution:
#     if x in found_letters:
#         view += x + " "
#     else:
#         view += "_ "

# if "_" not in view:
#     print(">>> You won! <<<")
#     break
    
# print("\n    * End of the game *    ")