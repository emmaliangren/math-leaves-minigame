# MATH LEAVES MINIGAME

## Description

This minigame challenges the player's quick arithmetic abilities and gets increasingly difficult as the game progresses. Falling leaf elements that have simple math equations on 
them disappear as the user correctly inputs the answers.

## Getting Started

### Executing program

Run the program at the 'math leaves' file depth: `math-leaves-minigame/math leaves` with the command `python3 math leaves.py`

## Limitations & Possible Improvements

The input mechanism is a incrementally resetting string, which could lead to incorrectly adding points in the case that leaves created following the user input, but before the reset of the string get
attributed to past user input and then validated as the correct answer. Increases in game difficulty, specifically in increasing the speed at which the leaves fall, is quite abrupt as Pygame doesn't 
support displaying images in quantities at any less than increments of half pixels. The first issue could be fixed by implementing a dictionary which stores the time at which input was typed and 
implementing a "time created" member variable to the leaf class, and then only validating input typed in after the creation of the leaf. The second issue could be improved by toying with incrementing
combinations of the pygame.time.delay function and increasing the speed at which the leaves fall.
