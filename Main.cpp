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
    if(input_ == "3") scores[3] = "not playing";
    if(input_ == "2") scores = {"0", "0", "not playing", "not playing"};
    if(input_ == "1") {cout << "COMs currently in development. Sorry, no single player yet."; return 0;}
    
    printScores(scores);
    return 0;
}
