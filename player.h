#ifndef PLAYER_H
#define PLAYER_H

#include "card.h"
#include <stdlib.h>
#include <unistd.h>

#define NAME_LENGTH 10 //# char permissible in a player name
#define HAND_SIZE 20 // max cards in hand
//#define ENTER 
#define PLAYER_COUNT 2

typedef struct {
    Card *cards[HAND_SIZE]; //the cards the hand holds
    char cardsInHand; //number of cards in a hand
    int wager;
    int size;
} Hand;

typedef struct{
    char name[NAME_LENGTH];
    Hand hand1;
    Hand hand2;
    char selectedCard; //selected card index
    unsigned char score; //score
    int bankroll;
    int split;
    int score1;
    int score2;
} Player;

void playersInit();

int place_bet(int bet, Hand *hand);

#endif
