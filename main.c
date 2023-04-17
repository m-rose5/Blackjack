#include <stdio.h>
#include <string.h>
#include <locale.h> //unicode
#include <wchar.h> //unicode
#include "deck.h"
#include "card.h"
#include "player.h"

#define PLAYER_COUNT 2

// For now player.c defines players, and main accesses it
// Future - update playersInit to have parameters
extern Player players[PLAYER_COUNT]; //initialize players

const static char *RESET_COLOR = "\x1b[36m";

Card deck[DECK_SIZE];
Card *shuffled[DECK_SIZE];

void deal_dealer(){
    deal(shuffled, &players[0].hand1, players[0].hand1.size);
    //increment dealer hand size after deal
    players[0].hand1.size++;
    players[0].score1 = players[0].score1 + players[0].hand1.cards[players[0].hand1.size-1]->value;
}

//might need to be written in python to get user input

//returns an array, x[0] = the cards face value, a[1] is the suit
void deal_player(){
    deal(shuffled, &players[1].hand1, players[1].hand1.size);
    //increment player hand size after deal
    players[1].hand1.size++;
    //ad the value of the card to the total points of the hand after the card is dealt
    players[1].score1 = players[1].score1 + players[1].hand1.cards[players[1].hand1.size-1]->value;
     
}
//return 0 for player win, 1 for dealer win
int stand(){
        if(players[1].score1 > players[0].score1 || players[0].score1 > 21){
            return 0;
        }else{
            return 1;
        }
    }

int dealer_score(){
    return players[0].score1;
}

int player_score(){
    return players[1].score1;
}

int player_hand_size(){
    return players[1].hand1.size;
}

int dealer_card_value(){
    
    return players[0].hand1.cards[players[0].hand1.size-1]->value;
    
}

int dealer_card_suit(){
    return players[0].hand1.cards[players[0].hand1.size-1]->suit;
}

//call after dealing to get the value and suit of the card for python gui
int player_card_value(){
    
    return players[1].hand1.cards[players[1].hand1.size-1]->value;
    
}

int player_card_suit(){
    return players[1].hand1.cards[players[1].hand1.size-1]->suit;
}

int player_over(){
    if(players[1].score1 > 21){
        return 1;
    }else
    {
        return 0;
    }
    
}

void check_pairs(){
    //if the cards in the inital deal are pairs pairs have the option to split
    //turn the boolean pairs on for the hand
    if(players[1].hand1.cards[0]->type == players[1].hand1.cards[1]->type){
        printf("Would you like to split your pair? 0:no, 1:yes :\n");
        scanf("%d", &players[1].split); 
    }

    if(players[1].split == 1){
        //decrement hand score
        players[1].score1 = players[1].score1 - players[1].hand1.cards[players[1].hand1.size-1]->value;
        //set the first card in the split hand to the second dealt pair
        players[1].hand2.size++;
        players[1].hand2.cards[0] = players[1].hand1.cards[1];
        //increment hand 2 score
        players[1].score2 = players[1].score2 + players[1].hand2.cards[players[1].hand2.size-1]->value;
        //remove the pair from the first hand
        players[1].hand1.cards[1] = NULL;
        //decrement the first hand size
        players[1].hand1.size = players[1].hand1.size - 1;
    }
}

void initGame(){
    
    initCard(); // set up unicode printing
    initDeck(deck);
    shuffleDeck(shuffled, deck);
    Card *c = cutDeck(shuffled);
    //printf("suit: %d, type: %d\n", c->suit, c->type);
    //system("clear"); //clear console
    //printf("Cut Card.\n");
    //c->hidden = 1;   // hidden==1 shows ???
    c->selected = 1; // changes card border color, 1 is red, 0 is green
   // printCard(c, "\n");
    c->selected = 0; // make green for rest of deck
   // printf("Deck before dealing:\n");
    //printRestOfDeck(shuffled); // Printing the deck makes the cards visible
    //system("clear");
    playersInit();
    
}

int main(int argc, char **argv) {
    return 0;
}
