# Exercise 1

# Accept two user ages as inputs and give us the difference between them. (The Answer should always be a positive output)

age1 = int(input("How old are you? "))
age2 = int(input("How old is your mom? "))

age_difference = abs(age1 - age2)

print(f"The age difference between you and your mom is {age_difference} years.")



# Exercise #2 

# Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.

animal = input("Enter your favorite animal: ")
action = input("What sound does your favorite animal make? ")
description = input("Describe your favorite animal in one word: ")

formatted_string = f"The {description} {animal} {action}."

print(formatted_string)



# Exercise #3

# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors.

age = int(input("How old are you?: "))

if age < 18:
    print("Ok, zoomer.. you're still a kid.")
elif age <= 65:
    print("I guess you're acceptable, probbo' a millenial adult!")
else:
    print("I respect my elders, you're a senior.")



# Exercise 4

# Take in a number from a user input, output the number squared

num1 = int(input("What is your favorite number? "))

number_squared = num1 ** 2

print(f"The number {num1} squared is {number_squared}.")



# Exercise #5

# Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False.

word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

word_list = {"panini", "bulbasaur", "pie", "dolphin", "dog"}

for word in word_list:
    if len(word) > 5:
        print(f"True: The word {word} has a length greater than 5.")
    else:
        print(f"False: The word {word} has a length less than 5.")