#include <iostream>
#include <array>
#include <string>
using namespace std;
string input() {
    string functionX;
    cin >> functionX;
    return functionX;
}
void printScores(array <string, 4> scores) {
    cout << "\n\nPlayer 1: " << scores[0] << "\nPlayer 2: " << scores[1] << "\nPlayer 3: " << scores[2] << "\nPlayer 4: " << scores[3];
}
int main() {
    cout << "How many players? ";
    array <string, 4> scores = {"0", "0", "0", "0"};
    string input_ = input();
    if(input_=="3"||input_=="2"||input_=="4") {cout << "Multiplayer currently in devlopment. Sorry."; return 0;} 
    if(input_=="1") int players = 1;
    array <string, 13> hearts = {"Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts","5 of Hearts","6 of Spad\
    es","7 of Hearts", "8 of Hearts", "9 of Hearts","10 of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts"};
    
    array <array, 4> cardIndex = {{"Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs","5 of Clubs","6 of Spad\
    es","7 of Clubs", "8 of Clubs", "9 of Clubs","10 of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs"},{"Ace of Diamonds", "2 of D\
    iamonds", "3 of Diamonds", "4 of Diamonds","5 of Diamonds","6 of Spad\
    es","7 of Diamonds", "8 of Diamonds", "9 of Diamonds","10 of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds"},{"Ac\
    e of Spades", "2 of Spades", "3 of Spades", "4 of Spades","5 of Spades","6 of Spad\
    es","7 of Spades", "8 of Spades", "9 of Spades","10 of Spades","Jack of Spades","Queen of Spades","King of Spades"},hearts};
    
    array <string, 13> playerOneCards = {cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]],cardIndex[rand()%4[rand()%13]]};
    
    printScores(scores);
    return 0;
}
