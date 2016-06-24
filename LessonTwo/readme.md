# Lesson Two!
What we learned today:

  * Using GitHub and SourceTree
  * 'in' operator
  * Python Range & List data structures
  * Python Control Structures
    * For and while loops
    * If, elif, and else (else also for loop) statements
    * Break, continue, and pass keywords
    * Nested loops

# Homework Assignments
Continuing with your adventures in the city of Cintely, here are your next homework assignment(s):

### 1. The Odd One
It's a hot day out and everybody's in the mood for ice cream. Word on the street is there's a new ice cream startup in town that's supposedly run by Oddity Kelpy. When you go over to see what the hype is all about, you see Oddity Kelpy outside of the ice cream store frantically running about. She sees you and rushes over to see if you can help her with her problem. 

There are too many people lining up at the door for the big opening of her ice cream shop, Creamtel, because there aren't enough workers to make the cones for all ice cream being sold. Oddity Kelpy's trade secret is that her cones are made of 0's and 1's, and the extra work needed to make these cones keeps her from being able to mass produce these cones quickly. She needs a program that will help her make cones on demand and allows her to be able to input the biggest width of a cone, and print out a schematic for what that would look like. She can then use a 3-D printer to print out the cone.

For example, if she wanted a cone with a width of 5, then her desired cone schematic would be:

```
    01010
     010
      0
```

Each layer of the cone will start with a 0 and alternate between 1's and 0's from there. The output will be centered as shown with spaces as filler.

### 2. Let's Make a Deal (Taken from my CS class)
After masterfully helping create a cone-printing program, you sit down enjoying the free ice cream Oddity Kelpy gave you for helping her out. All of a sudden, you spot Charley, the kid from Gintel coming up to you with a giant slab of ice cream. He sits down next to you and thanks you for helping him with his earlier problem with solving the quadratic formula. He then proceeds to ask you about a game show in the past, Let's Make a Deal, and whether or not you know about the game show. 

With your overflowing intelligence, you acknowledge the game show, knowing that it was a game show aired during the 70's. You continue to explain more about the game:

"The game starts with the game show host, Monty Hall, showing a contestant 3 doors. Behind one door was the game's grand prize, and the contestant would have to pick which door it was behind. When the contestant made a guess, Monty Hall would proceed to open one of the other doors that did not have the prize behind it. Then the contestant had the choice of sticking with their original answer or switch to the other door that was still closed. Monty Hall would then open the door with the prize."

Charley is in awe with your knowledge, but he continues to tell you that his teacher, Mary Lin vos Savant, had said that to maximize their chances of winning, that they should always switch doors after choosing one door. He thought that there would be a 50% chance of winning once a door was open and doesn't understand how could it possibly be better to always switch. To show him the statistics, you decide to simulate the game using a program with the following logic:

You will prompt the user to enter the number of times he or she wants to play this game.  
You will create a variable to keep track of the number of times the contestant wins by switching.  
Generate a random number between 1 and 3 (inclusive) that will denote the door that conceals the prize.  
Generate another random number between 1 and 3 (inclusive) that will denote the guess the contestant makes.  
From those two numbers, compute a number that does not conceal the prize nor is it the contestant's guess. This is the door that is opened by Monty Hall and we shall call it view.  
At this point the contestant changes his mind makes a newGuess that is not the original guess nor is it the view.  
You will compare the value of the newGuess with that of prize. If they are the same, the contestant won by switching, and you increment the variable that was keeping track of that.  
You will run this simulation for however many times the user had specified.  
To obtain the probability for winning if you switch divide the number of times the contestant wins by switching by the total number of games played.  
To obtain the probability of winning by not switching subtract the above number from one.  

The program will look something like this:
```
Enter number of times you want to play: 10

  Prize      Guess       View    New Guess 
    2          2          3          1     
    1          3          2          1     
    1          1          2          3     
    3          1          2          3     
    3          1          2          3     
    3          1          2          3     
    2          2          3          1     
    2          1          3          2     
    3          2          1          3     
    2          1          3          2     

Probability of winning if you switch = 0.70
Probability of winning if you do not switch = 0.30
```


You will need to learn more about a few topics that we have not discussed yet, and there will be base code to help start you on this homework! Pull from the repo to get started.