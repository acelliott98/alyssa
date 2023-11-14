import random 
name = input("hello whats your name")
print("welcome " + name + "Im thinking of a \
  number between 1 and 100")

my_number = random.randint(1, 100)

guesses = []
range(1,11)
for guess in range(1,11):
  valid_guess = False
  while not valid_guess:
    try:
        user_guess = int(input("Take a guess....\n"))
        valid_guess=True
    except ValueError:
      print("please enter a number")
  
  difference = abs(my_number - user_guess)
  guesses.append(user_guess)
  

  if user_guess < my_number and difference > 10:
    print("your guess is very low, Try again.")
  elif user_guess < my_number and difference < 10:
    print("your guess is a little low, Try again.")
  elif user_guess > my_number and difference > 10:
    print( "your guess is very high, Try again.")
  elif user_guess > my_number and difference < 10:
    print("your guess is a little high, Try again.")
  else:
    break
    
if user_guess == my_number:
  print("You won " + name + "! You guessed my number in   " + str(user_guess) + " guesses.")
  print("your guesses were: " + " ".join(str(x) for x in guesses))
else:
  print("Sorry! you didn't guess my number. The number I am \
    thinking of is " + str(my_number))