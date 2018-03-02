'''
http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

string = str(input("Enter a string: "))

rev = string[::-1]

print(rev)

if string == rev:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")