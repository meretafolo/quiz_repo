# Created by Mele Tafolo
# Date: 21/03/2023
# Demonstrate asking the user a question, provide multiple choice answers, get the user's answer, check if it's correct

# This is a function called check(). It requires 2 arguments. One list and one user input. It returns True if the user input is in the list. It returns False if the user input is not in the list.
def check(options, user_input):
    if user_input in options:
        return True
    else:
        return False

options = ["genesis"]
question_one = input("What is the first book of the Bible: \n genesis \n danie \n mark \n luke").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")

    
    
options = ["Genesis, Exodus, Leviticus, Numbers, Deuteronomic"]
question_one = input("What are the 5 books of Moses: \n Genesis, John, Luke, Acts, Revelation \n Mathew, Mark, Luke, John, Acts \n Daniel, Revelation, 1st Peter, 2nd Peter, 1st John").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")

    


options = ["23"]
question_one = input("How many commandments are there: \n 5 \n 9 \n 10").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")

    

options = ["39"]
question_one = input("How many books are there in the Old Testament:\n 23\n 17 \n 1 ").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")




options = ["27"]
question_one = input("How many books are there in the New Testament: \n 39 \n 56 \n 44 ").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")




options = ["Adam and Eve", "Joseph and Marry", "Abraham and Serah", "Jacob and Leah"]
question_one = input("Who was the first parent here on earth: \n Joseph and Marry \n Abraham and Serah \n Jacob and Leah").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")

   


options = ["6"]
question_one = input("How many days did it take for the creation: \n 10 \n 7 \n 22 ").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")


 


options = ["12"]
question_one = input("How old was Jesus when he became a teacher: \n 5 \n 16 \n 21").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")
   


 


options = ["12"]
question_one = input("How many disciples did Jesus have: \n 20 \n 6 \n 32 ").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")
   
 


options = ["13"]
question_one = input("How many siblings did Joseph have: \n 1 \n 23 \n 12 ").lower().strip()

#print(check(options, question_one))
if check(options, question_one):
    print("Your input is in the list")
else:
    print("Your input is not in the list")