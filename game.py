from tkinter import *
import random
from PIL import Image, ImageTk
import ctypes
import time
#initalize shared library
blackjack = ctypes.CDLL("blackjack.so")

#initalized cards and players in
blackjack.initGame()

global playerscore
playerscore = 0

global dealerscore
dealerscore = 0
root = Tk()
root.title('Black Jack')
root.geometry("900x500")
root.configure(background="green")

# Resize Cards
def resize_cards(card):
	# Open the image
	card_img = Image.open(card)

	# Resize The Image
	card_resize_image = card_img.resize((150, 218))
	
	# output the card
	global card_image
	card_image = ImageTk.PhotoImage(card_resize_image)

	# Return that card
	return card_image

# Shuffle The Cards
def shuffle():
	# Define Our Deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(1, 13)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')

	# Create our players
	global dealer, player
	dealer = []
	player = []
		
		
# Deal Out Cards
def deal_player():
    #deal_card1()
    deal_card2()
    deal_card3()

def deal_card1():
				blackjack.deal_player()
				x = blackjack.player_card_suit()
				y = blackjack.player_card_value()
				suit = "";
				if(x == 0):
					suit = "spades"
				if(x == 1):
					suit = "hearts"
				if(x == 2):
					suit = "diamonds"
				if(x == 3):
					suit = "clubs"
				y = str(y)
				card = y +"_of_"+ suit
				# Get the deler Card
				# Output Card To Screen
				global player_card1_image
				player_card1_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				player_card1_label.config(image=player_card1_image)
				card_button.configure(command=deal_card2)
    
def deal_card2():
				blackjack.deal_player()
				x = blackjack.player_card_suit()
				y = blackjack.player_card_value()
				suit = "";
				if(x == 0):
					suit = "spades"
				if(x == 1):
					suit = "hearts"
				if(x == 2):
					suit = "diamonds"
				if(x == 3):
					suit = "clubs"
				y = str(y)
				card = y +"_of_"+ suit
				#player_card1_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				player_card1_label.config(image=player_card1_image)
				global player_card2_image
				player_card2_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				player_card2_label.config(image=player_card2_image)
				card_button.configure(command=deal_card3)
				playerscore = blackjack.player_score()
				#make ace worth 11 instead of 1
				if(y == 1):
					playerscore += 10
				
				player_card1_frame.configure(text="player score: " + str(playerscore))
    
def deal_card3():
				blackjack.deal_player()
				x = blackjack.player_card_suit()
				y = blackjack.player_card_value()
				suit = "";
				if(x == 0):
					suit = "spades"
				if(x == 1):
					suit = "hearts"
				if(x == 2):
					suit = "diamonds"
				if(x == 3):
					suit = "clubs"
				y = str(y)
				card = y +"_of_"+ suit
				player_card1_label.config(image=player_card1_image)
				player_card2_label.config(image=player_card2_image) 
				global player_card3_image
				player_card3_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				player_card3_label.config(image=player_card3_image)
				card_button.configure(command=deal_card4)
				playerscore = blackjack.player_score()
				#make ace worth 11 instead of 1
				if(y == 1):
					playerscore += 10
				player_card1_frame.configure(text="player score: " + str(playerscore))
				x = blackjack.player_over()
				if(x == 1):
					card_button.configure(text="Dealer Wins!", command=None)
					stand_button.configure(text="Play again?", command=playagain)
    
def deal_card4():
				blackjack.deal_player()
				x = blackjack.player_card_suit()
				y = blackjack.player_card_value()
				suit = "";
				if(x == 0):
					suit = "spades"
				if(x == 1):
					suit = "hearts"
				if(x == 2):
					suit = "diamonds"
				if(x == 3):
					suit = "clubs"
				y = str(y)
				card = y +"_of_"+ suit
    
				player_card1_label.config(image=player_card1_image)
				player_card2_label.config(image=player_card2_image)
				player_card3_label.config(image=player_card3_image)  
				global player_card4_image
				player_card4_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				player_card4_label.config(image=player_card4_image)
				playerscore = blackjack.player_score()
				#make ace worth 11 instead of 1
				if(y == 1):
					playerscore += 10
				player_card1_frame.configure(text="player score: " + str(playerscore))
				card_button.place(50,50)
				x = blackjack.player_over()
				if(x == 1):
					card_button.configure(text="Dealer Wins!", command=None)
					stand_button.configure(text="Play again?", command=playagain)
					
			
def dealer_card1():
	blackjack.deal_dealer()
	x = blackjack.dealer_card_suit()
	y = blackjack.dealer_card_value()
	suit = ""
	if(x == 0):	
		suit = "spades"
	if(x == 1):
		suit = "hearts"
	if(x == 2):
		suit = "diamonds"
	if(x == 3):
		suit = "clubs"
	y = str(y)
	card = y +"_of_"+ suit
				# Get the deler Card
				#card = random.choice(deck)
				# Remove Card From Deck
	
				# Append Card To Dealer List
				#player.append(card)
				# Output Card To Screen
	global dealer_image
	dealer_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
	dealer_label.config(image=dealer_image)				
	dealerscore = blackjack.dealer_score()
				#make ace worth 11 instead of 1
	if(y == 1):
		dealerscore += 10
	dealer_frame.configure(text="dealer score: " + str(dealerscore))
def dealer_card2():
				blackjack.deal_dealer()
				x = blackjack.dealer_card_suit()
				y = blackjack.dealer_card_value()
				suit = ""
				if(x == 0):
					suit = "spades"
				if(x == 1):
					suit = "hearts"
				if(x == 2):
					suit = "diamonds"
				if(x == 3):
					suit = "clubs"
				y = str(y)
				card = y +"_of_"+ suit
				# Get the deler Card
				#card = random.choice(deck)
				# Remove Card From Deck
				# Append Card To Dealer List
				#player.append(card)
				# Output Card To Screen
				global dealer_card2_image
				dealer_card2_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				dealer_card2_label.config(image=dealer_card2_image)				
				dealerscore = blackjack.dealer_score()
				#make ace worth 11 instead of 1
				if(y == 1):
					dealerscore += 10
				dealer_label.config(image=dealer_image)
				dealer_frame.configure(text="dealer score: " + str(dealerscore))
    
def dealer_card3():
				blackjack.deal_dealer()
				x = blackjack.dealer_card_suit()
				y = blackjack.dealer_card_value()
				suit = ""
				if(x == 0):
					suit = "spades"
				if(x == 1):
					suit = "hearts"
				if(x == 2):
					suit = "diamonds"
				if(x == 3):
					suit = "clubs"
				y = str(y)
				card = y +"_of_"+ suit
				# Get the deler Card
				#card = random.choice(deck)
				# Remove Card From Deck
				
				# Append Card To Dealer List
				#player.append(card)
				# Output Card To Screen
				global dealer_card3_image
				dealer_card3_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				dealer_card3_label.config(image=dealer_card3_image)				
				dealerscore = blackjack.dealer_score()
				#make ace worth 11 instead of 1
				if(y == 1):
					dealerscore += 10
				dealer_label.config(image=dealer_image)
				dealer_frame.configure(text="dealer score: " + str(dealerscore))
def dealer_card4():
				blackjack.deal_dealer()
				x = blackjack.dealer_card_suit()
				y = blackjack.dealer_card_value()
				suit = ""
				if(x == 0):
					suit = "spades"
				if(x == 1):
					suit = "hearts"
				if(x == 2):
					suit = "diamonds"
				if(x == 3):
					suit = "clubs"
				y = str(y)
				card = y +"_of_"+ suit
				# Get the deler Card
				#card = random.choice(deck)
				# Remove Card From Deck
		
				# Append Card To Dealer List
				#player.append(card)
				# Output Card To Screen
				global dealer_card4_image
				dealer_card4_image = resize_cards(f'Playing Cards/PNG-cards-1.3/{card}.png')
				dealer_card4_label.config(image=dealer_card4_image)				
				dealerscore = blackjack.dealer_score()
				#make ace worth 11 instead of 1
				if(y == 1):
					dealerscore += 10
				dealer_label.config(image=dealer_image)
				dealer_frame.configure(text="dealer score: " + str(dealerscore))
    

def stand():
	dealer_card2()
	x = blackjack.stand()
	if(x == 0):
		dealer_card3()
	x = blackjack.stand()
	if(x == 0):
		dealer_card4()
	x = blackjack.stand()
	if(x == 1):
		card_button.configure(text="Dealer Wins!")
		stand_button.configure(text="Play again?", command=playagain)
	if(x== 0):
		card_button.configure(text="You Win!")
		stand_button.configure(text="Play again?", command=playagain)
   

   

frame = Frame(root, bg="green")
frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(frame, text='dealer score: ' + str(dealerscore), bd=0, background='green')
dealer_frame.grid(row=0, column=0, padx=20, ipadx=10)

dealer_card2_frame = LabelFrame(frame, text="", bd=0, background='green')
dealer_card2_frame.grid(row=0, column=1, padx=20, ipadx=10)

dealer_card3_frame = LabelFrame(frame, text="", bd=0, background='green')
dealer_card3_frame.grid(row=0, column=2, padx=20, ipadx=10)

dealer_card4_frame = LabelFrame(frame, text="", bd=0, background='green')
dealer_card4_frame.grid(row=0, column=3, padx=20, ipadx=10)

player_card1_frame = LabelFrame(frame, text="Player", bd=0, background='green')
player_card1_frame.grid(row=10, column=0, ipadx=10)

player_card2_frame = LabelFrame(frame, text="", bd=0, background='green')
player_card2_frame.grid(row=10, column=1, ipadx=10)

player_card3_frame = LabelFrame(frame, text="", bd=0, background='green')
player_card3_frame.grid(row=10, column=2, ipadx=10)

player_card4_frame = LabelFrame(frame, text="", bd=0, background='green')
player_card4_frame.grid(row=10, column=3, ipadx=10)

# Put cards in frames
dealer_label = Label(dealer_frame, text = '', background='green')
dealer_label.pack(pady=20)

dealer_card2_label = Label(dealer_card2_frame, text='', background='green')
dealer_card2_label.pack(pady=20)

dealer_card3_label = Label(dealer_card3_frame, text='', background='green')
dealer_card3_label.pack(pady=20)

dealer_card4_label = Label(dealer_card4_frame, text='', background='green')
dealer_card4_label.pack(pady=20)

player_card1_label = Label(player_card1_frame, text='', background='green')
player_card1_label.pack(pady=20)

player_card2_label = Label(player_card2_frame, text='', background='green')
player_card2_label.pack(pady=20)

player_card3_label = Label(player_card3_frame, text='', background='green')
player_card3_label.pack(pady=20)

player_card4_label = Label(player_card4_frame, text='', background='green')
player_card4_label.pack(pady=20)


global card_button
card_button = Button(root, text="hit", font=("Helvetica", 14), command=deal_card3)
card_button.pack(pady=20)

global stand_button
stand_button = Button(root, text="stand", font=("Helvetica", 14), command=stand)
stand_button.pack(pady=20)



# Shuffle Deck On Start
shuffle()
dealer_card1()
deal_card1()
deal_card2()
#deal_player()
def playagain():
	blackjack.initGame()
	dealer_label.configure(text="dealer score: ")
	player_card1_label.configure(text="player score: ")
	player_card1_label.config(image="")
	player_card2_label.config(image="")
	player_card3_label.config(image="")
	player_card4_label.config(image="")
	dealer_label.config(image="")	
	dealer_card2_label.config(image="")	
	dealer_card3_label.config(image="")	
	dealer_card4_label.config(image="")
	card_button.config(text="hit", command=deal_card3)
	stand_button.config(text="stand", command=stand)
	shuffle()
	dealer_card1()
	deal_card1()
	deal_card2()	

root.mainloop()
