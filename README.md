# Word Play

## Exercises 1 - 6 can be done in one module, just define separate functions for each.  
### Be sure to include docstrings explaining what each function does.

**Exercise #1** 

Write a function, *at_least* that reads words.txt and prints only the words with at least 20 characters (not counting whitespace).

**Exercise #2**

In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do.

In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility. All right, I’ll stop now. Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

Write a function *no_e* that ~~prints~~ counts only the words that have no “e” and compute the percentage of the words in the list that have no “e”.

**Exercise #3** 

Write a function named *avoids* that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters.

Write a function *count_avoids* that prompts the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

**Exercise #4**

Write a function named *uses_only* that takes a word and a string of letters, and that returns True if the word contains only letters in the list. 

Write a function *words_with_only* that takes in a string of letters and prints all of the words with only those letters.  Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”

**Exercise #5**

Write a function named *uses_all* that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once. 

Write a function *how_many_uses_all* that takes a string of required letters and prints the number of words that use all of the required letters.  How many words are there that use all the vowels aeiou? How about aeiouy?

**Exercise #6**

Write a function called *is_abecedarian* that returns True if the letters in a word appear in alphabetical order (double letters are ok). 

Write a function *count_abecedarian* that prints the number of words that are abecedarian.  How many abecedarian words are there?

## Exercises 7 - 9 should each be done in separate modules.  
### Still use functions, and include doc strings, but when the program is run, the answer to the question should print out!

**Exercise #7**

Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work. But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?

**Exercise #8**

I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.  Now, what I saw that day was very interesting.  I noticed that the last 4 digits were palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5. One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic! The question is, what was on the odometer when I first looked?

**Exercise #9**

Recently I had a visit with my mom and we realized that the two digits that make up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer. When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we’re lucky it would happen again in a few years, and if we’re really lucky it would happen one more time after that. In other words, it would have happened 8 times over all. So the question is, how old am I now?
