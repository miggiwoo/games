import random

money = 100

#Write your game of chance functions here
##Coin Game
def coin_flip(guess, bet):
	##error check
	if (money<bet):
		print("Error - Insufficient Money for bet")
		print("----------------------------------")
		return 0
	elif (bet<=0):
		print("Error - bet must be greater than zero")
		print("-------------------------------------")
		return 0
	elif (guess == "Heads" or guess == "heads" or guess =="Heads!"):
		guessno = 1
		
	elif (guess == "Tails" or guess == "tails" or guess == "Tails!"):
		guessno = 2
	else:
		print("Error - please guess Heads or Tails")
		print("-----------------------------------")
		return 0
	##game
	print("Let's flip a coin!")
	print("You guessed " + guess +"!")
	num = random.randint(1,2)
	if (num==1):
		print("The flip is Heads!")
		print("------------------")
	else:
		print("The flip is Tails!")
		print("------------------")
	##outcome
	if (guessno == num):
		print("You guessed right! You won $"+str(bet)+ " dollarbucks!")
		print("------------------------------------------------------")
		return bet
	else:
		print("You guessed wrong! You lost $"+str(bet)+ " dollarbucks!")
		print("-------------------------------------------------------")
		return -bet

## Cho Han
def cho_han(guess,bet):
	##ErrorCheck
	if (money<bet):
		print("Error - Insufficient Money for bet")
		print("----------------------------------")
		return 0
	elif (bet<=0):
		print("Error - bet must be greater than zero")
		print("-------------------------------------")
		return 0
	elif (guess == "Even" or guess == "even" or guess =="Even!"):
		guessno = 1
	elif (guess == "Odd" or guess == "odd" or guess == "odd!"):
		guessno = 2
	else:
		print("Error - please guess Even or Odd")
		print("-----------------------------------")
		return 0
	##Game
	print("Let's roll the dice!")
	print("You guessed "+guess+"!")
	num1 = random.randint(1,6)
	num2 = random.randint(1,6)
	print("The first dice is " +str(num1)+ "!")
	print("The second dice is " +str(num2)+ "!")
	if((num1+num2)%2==0):
		oddeven = 1
		print("The total, "+str(num1+num2)+", is Even!")
		print("------------------")
	else:
		oddeven = 2
		print("The total, "+str(num1+num2)+", is Odd!")
		print("-----------------")
	##outcome
	if(oddeven == guessno):
		print("You guessed right! You won $"+str(bet)+ " dollarbucks!")
		print("------------------------------------------------------")
		return bet
	else:
		print("You guessed wrong! You lost $"+str(bet)+ " dollarbucks!")
		print("-------------------------------------------------------")
		return -bet
	
##Card draw
card_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14]

def card_game(bet):
	##Error Check
	if (money<bet):
		print("Error - Insufficient Money for bet")
		print("----------------------------------")
		return 0
	elif (bet<=0):
		print("Error - bet must be greater than zero")
		print("-------------------------------------")
		return 0
	##game
	print("Let's Draw some cards!")
	drawn_cards = random.sample(card_deck,2)
	your_card = drawn_cards[0]
	their_card = drawn_cards[1]
	if(your_card<=10):
			print("Your card is " + str(your_card)+"!")
	elif(your_card == 11):
			print("Your card is a Jack!")
	elif(your_card == 12):
			print("Your card is a Queen!")
	elif(your_card == 13):
			print("Your card is a King!")
	elif(your_card == 14):
			print("Your card is an Ace!")

	if(their_card<=10):
			print("Their card is "+str(their_card)+ "!")
	elif(their_card ==11):
			print("Their card is a Jack!")
	elif(their_card ==12):
			print("Their card is a Queen!")
	elif(their_card ==13):
			print("Their card is a King!")
	elif(their_card ==14):
			print("Their card is an Ace!")
	##outcome
	print("--------------------------")
	if(your_card>their_card):
		print("Your card is Higher! You win $"+str(bet)+" dollarbucks!")
		print("--------------------------------------------------")
		return bet
	elif(your_card<their_card):
		print("Their card is Higher! You lose $"+str(bet)+" dollarbucks!")
		print("--------------------------------------------------")
		return -bet
	else:
		print("Your cards are the same! Your bet is returned!")
		print("--------------------------------------------------")
		return 0
	
	
## Roulette
outcomes_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36, "Even", "Odd", "High","Low"]
def roulette(guess,bet):
	##errorcheck
	if (money<bet):
		print("Error - Insufficient Money for bet")
		print("----------------------------------")
		return 0
	elif (bet<=0):
		print("Error - bet must be greater than zero")
		print("-------------------------------------")
		return 0
	elif (guess not in outcomes_list):
		print("Error - You must guess a number between 0 & 36, Even, Odd, High or Low")
		return 0
	##Game
	print("Let's Spin the Wheel!")
	spin = random.randint(0,36)
	if (guess == "Even" and spin%2 == 0 and guess !=0):
		print("The spin is " +str(spin) +" which is even! You win $" +str(bet) +" dollarbucks!")
		return bet
	elif (guess == "Odd" and spin%2 == 1):
		print ("The spin is " +str(spin) +" which is odd! You win $" +str(bet) +" dollarbucks!")
		return bet
	elif (guess == "High" and spin>=19):
		print("The spin is " +str(spin) +" which is high! You win $" +str(bet) +" dollarbucks!")
		return bet
	elif (guess =="Low" and spin <=18):
		print("The spin is " +str(spin) +" which is low! You win $" +str(bet) +" dollarbucks!")
		return bet
	elif (guess == spin):
		print("The spin is " +str(spin) +" which is your guess! You win $" +str(bet*35) +" dollarbucks!")
		return bet*35
	else:
		print("The spin is " +str(spin) +" which is not your guess! You lose $" +str(bet) +" dollarbucks!")
		return -bet





#Call your game of chance functions here

money += coin_flip("Heads", 5)
money += cho_han("Even",5)
money += card_game(5)
money += roulette("Even",10)

print("You have $" +str(money) + " left!")



