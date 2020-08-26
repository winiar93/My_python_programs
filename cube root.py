epsilon = 0.001
y = 54.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess -y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) -y)/(2*guess))
print("ilosc odgadniec" + str(numGuesses))
print("pierwiastek kwadratowy" + str(y) + "to" + str(guess))    
