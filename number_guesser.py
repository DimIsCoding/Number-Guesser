import random

g_num = random.randint(1,20)

user = input("Welcome to NumGuesser! What is your Username: ")
print(f"Hello,"+user+"let's start!")
g =0

print("Let's start "+user+ " I will guess a number, starting from 1 to 20!:")
while g < 7:
    guess = int(input())
    g+=1
    if guess < g_num:
        print("Your guess is under the number!")
    if guess > g_num:
        print("Your guess is over the number!")
    if guess == g_num:
        break
if guess == g_num:
    
    print("You found the number!You tried " + str(g)+ " times")
else:
    print("You did not guess the number, The number was " + str(g_num))