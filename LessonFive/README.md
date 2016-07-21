# Lesson Four!
What we learned today:

  * Object Oriented Programming
  * Objects and classes
  * Encapsulation
  * Polymorphism
  * Abstraction
  * Inheritance

# Homework Assignments
I'm gonna have to hold off on making more story lines so I can actually get these homeworks out quickly :'), but I'll come back and work on them sometime!

### 1. Hit Me (Creds. to Professor Mitra)
This is....a program to play blackjack! This is exactly from my data structure's class (Thanks to Prof. Mitra!)

In this program you will use the following classes - Card, Deck, Player, Dealer, and Blackjack. The intent of this assignment is for you to simulate a Blackjack game using classes and object-oriented programming similar to your last programming assignment. This program will introduce the concept of inheritance.

```Python
class Card (object):
...

class Deck (object):
...

class Player (object):
...

class Dealer (Player):
...

class Blackjack (object):
...

def main():
...

main()
```

In Blackjack you want to have a hand value that is closer to 21 than that of the dealer, without going over 21. You are playing strictly against the dealer and not against the other players at the table. The values of the cards are as follows:

An Ace can count either as 1 or 11 to make the best hand.
Cards from 2 through 10 are valued at their face value.
Jack, Queen, and King are all valued at 10.
All suits have the same value.
The value of a hand is simply the sum of the point counts of each card. If the first two cards in your hand is (Ace, 8) and stop there, then Ace will count as 11 and your hand is worth 19 points. If, on the other hand, you get another card and it is another 8, you now have (Ace, 8, 8) and in this case Ace is 1 and your hand is worth 17 points.
The dealer deals two cards to all the players including himself. The players' cards are dealt face up. Only one of the cards of the dealer is face up and the other is face down.

Once the cards are dealt, each player in turn indicates to the dealer how he wishes to play his hand. After each player has finished, the dealer will complete his hand. In a casino the dealer will either pay or collect the players' bets. In your program you will write out whether the players won or lost or tied with the dealer.

The dealer has no choice in how he plays his hand. He must continue to take cards ("hit") until his total is 17 or greater. An Ace in the dealer's hand is always counted as 11 if possible without the dealer going over 21. So if the dealer has (Ace, 9), then his total will be 20 and he stops drawing cards ("stand"). However, if the dealer had (5, 7) and then added an Ace and his hand was (5, 7, Ace) then the total is 13 and so he hits again. Supposing he now he draws a 5, then is hand (5, 7, Ace, 5) totals 18 and he stands.

In the case of the player we have simplified the options that he has. The player can either hit or stand. Doubling or splitting pairs are not options that you will simulate in your program.

Your program will allow anywhere between 1 and 6 players (inclusive). Here is what your output will look like:

```
Enter number of players: 2

Player 1: 7S 5D - 12 points
Player 2: 4H JC - 14 points
Dealer: 10D

Player 1, do you want to hit? [y / n]: y
Player 1: 7S 5D 8H - 20 points
Player 1, do you want to hit? [y / n]: n

Player 2, do you want to hit? [y / n]: y
Player 2: 4H JC 9S - 23 points

Dealer: 10D 9C - 19 points

Player 1 wins
Player 2 loses
```
Here are some special cases to consider. If the Dealer goes over 21, all players who are still standing win. But the players that are not standing have already lost. If the Dealer does not go over 21 but stands on say 19 points then all players having points greater than 19 win. All players having points less than 19 lose. All players having points equal to 19 tie. This last case we made up to simplify your programming.


### 2. ProjectEuler #1
For this problem, we will demonstrate time complexity and algorithmic thinking. Remember that to solve this problem, you will need to be as efficient as possible, both with your resources and methodology. This problem is a reproduction from the projecteuler page. Google it to learn more about the problems there.

For any given number N, find and sum all of the numbers below that number N which are divisible by 3 or 5. For example:

 * N = 10
 * Numbers below N divisible by 3 or 5: 3 5 6 9
 * Answer: 23

To answer this question, you will create two methods which will be iterations of the solution. The first will be the first method that comes to mind to be able to solve the simpler and smaller test cases. The second iteration will require more complex thinking, research, and effcient code.

The first solution that you create will solve the problem, but will probably not be the best solution to the problem. This homework is to show you that you can always make a better program to solve the problem.

 * N = the N for each test case
 * T = number of N's (or test cases)

The constraints are:
 * 1 <= T <= 10^5
 * 1 <= N <= 10^9
 * You will have 10 seconds to output all off the correct answers for each method (10 seconds for slower, and another 10 for faster)
 
Print out each N to its corresponding answer. An example would be:
```
10: 23
100: 2318
```

There are two input files: slower_euler.txt and faster_euler.txt. It is formatted as:
```
T
N
N
...
```
Example:
```
2 (The number of the following test cases)
10 (a test case)
100 (a test case)
```

There is some starter code for you to work on. Fill in the slower_euler first, then the faster_euler! Try to copy and paste your slower_euler code into faster_euler to see if your code is worthy enough to run all test cases!