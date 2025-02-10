import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)
# print(f"The correct answer is {number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
  attempts = 10
elif difficulty == 'hard':
  attempts = 5

while attempts != 0:
  print(f"You have {attempts} remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess < number:
    print("Too low.\nGuess again.")
    attempts -= 1
  elif guess > number:
    print("Too high.\nGuess again.")
    attempts -= 1
  elif guess == number:
    print(f"You got it! The answer was {number}.")
    break
  if attempts == 0:
    print("You have run out of guesses, you lose.")
