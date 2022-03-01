# CodingChallenge
 application that takes a single integer input and print a list of all pairs of players whose height in inches adds up to the integer input to the application.


Welcome to my solution for this coding challenge,
the virtual environment was design using PyCharm software and is and algorithm of O(n)
to run this file, please download the project name Coding Challenge and run main.py file

1. the solution ask for a number to check the player pairs which heights when summed are equal to input number.
2. then request the information  from web.
3. this information is change to Json data to be more efficient to handle.
4. then  default items are created using defaultdict(list), which returns a new empty list object.
5. whe use a for loop to set the new dictionary with players Height inches, name and lastname.
6. that return pairs of players which heights are equal to the number provide it, using the following logic:
    a dictionary keyed by heights, and with as vlue the list of people (full names) that have the same height.
7. the solution will print the pairs name of basketball players that correspond to the number input.
8.  if no matches are found, the application will print "No matches found" and ask for a number again.
