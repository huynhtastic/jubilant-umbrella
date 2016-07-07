# Lesson Three!
What we learned today:

  * Modules and Importing
  * Functions
  * Arguments

# Homework Assignments
It's been a while since your last adventure in Cintely. Here are your next problems for Lesson Three:

### 1. The Key to Success
We resume our adventures in the vast city of Cintely and have a huge bank of knowledge to work with. While you were diligently in your classes, a person has been lurking around Cintely, leaving a ton of gibberish all over the city. The police have dubbed this person, "The Lurker", or Lurk for short. The police have also been collecting a bunch of items that Lurk has been leaving across the city and have called you for your expert advice.

You arrive at the at the call and beckon of Officer Hanro and Deputy Jon Terzei. They have gathered all of the gibberish left by Lurk, but they can't make out anything from what they've gathered. A block etched with letters says the following:

**"c fbvcvejs bv mygblr. ylki edyvj qysedi qbkk vjj edbv qcslblr. edj nlyqkjfrj yo edj mbpdjs qbkk wj iyxs ejve ey ckkyq pcvvcrj ey iyxs vcojei."**

Below that says:

**"Heed my power or my knowledge. The key lies within the 'inscriptions in hollow on side of inlet puzzled professor'."**

At first glance, it looks like gibberish to the untrained eye, but not to yours. You have seen this before. Your vast knowledge has trained you to see that this is a _Simple Substitution Cipher_, a basic ciphering method that uses a key to encipher some text (and if you haven't before, take a look at 
http://practicalcryptography.com/ciphers/simple-substitution-cipher/). But 'inscriptions in hollow on side of inlet puzzled professor'? The key must relate to that somehow.

After figuring all of this out, Deputy Jon Terzei has asked you to create two methods, "encipher" and "decipher", that take in some text, encipher or deciphers it, then **returns** the result. The deputy will then use these methods to be able to look through the rest of the encrypted text that Lurk has left behind.

### 2. Shop 'til You Drop
The cipher has been solved and you leave the police of Cintely to do their work with their newfound tools. It will take a while to be able to get through all of the items that Lurk has left throughout the city, especially since they are still finding new items by the hour. But your part is done for now, and it's time to get some groceries from the local market.

You make your way to HIB where all of the locals do their shopping for groceries. After picking up all of the items needed to make dinner for tonight, you make your way over to the cash register, but you see the cashiers checking everybody out... BY HAND! Lines have backed up from the slow process, and you even see people leave the lines and go home. Appalled by the lack of technology, you manage to spot a good friend of yours that works here, Makash Johnny. You go up to her and ask her why no one is using the scanners. According to Makash, the operating systems from the registers have been wiped clean, but their database and scanners are working just fine. To get this place up and running, you decide to create a program to replace the OS that has been wiped from the registers.

The scanners scan the barcodes and puts the item names into a .txt file. Your job is to be able to run through the .txt file, figure out what items were scanned, and then use the database (which will be a Python Dictionary to interface quickly with your program) to figure out how much each item costs. But luckily for you, there is also a promotion for HIB today! If you buy a certain amount of a certain item, customers get a discount! That makes your job so much better, cause that means you get a bigger challenge to test your skills on.

You decide that it's easier to create three functions: 

  * One that aggregates all of the items that were bought
  * One that determines the subtotal of the transaction
  * And one that determines the discounts applicable to the transaction

Whenever a certain item is bought enough times during the transaction, the buyer is given a 25% discount **for that particular item**. For example, if the buyer gets 6 apples and the amount of apples that they need to buy is at least 4 apples to get the discount, they will receive 25% off their total with the apples only. Everything else bought is still full price unless those items reach their respective thresholds as well.

To help you get started, the HIB team has given you the database converted to a Python Dictionary with the prices and discounts. They will look like this:

```python
items = {
    'apple': 0.99,
    'banana': 0.50,
    'orange': 1.00,
    'steak': 5.00,
    'chicken': 3.25,
    'beans': 2.45,
    'milk': 2.99,
    'dozen eggs': 1.67,
    'frozen pizza': 4.54,
    'UnderWatch Root Edition': 49.99
}

discounts = {
    'apple': 4,
    'banana': 9,
    'orange': 5,
    'steak': 4,
    'chicken': 5,
    'beans': 5,
    'milk': 2
    'dozen eggs': 3,
    'frozen pizza': 10,
    'UnderWatch Root Edition': 3
}
```
  
Be sure to download the starter code for this problem!
