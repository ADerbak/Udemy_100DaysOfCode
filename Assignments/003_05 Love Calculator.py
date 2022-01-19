# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true = 0
love = 0

for i in name1.lower():
    #print(i)
    if i in 'true':
        true+=1
    if i in 'love':
        love+=1

for i in name2.lower():
    #print(i)
    if i in 'true':
        true+=1
    if i in 'love':
        love+=1

truelove = int(str(true)+str(love))

if truelove < 10 or truelove > 90:
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove > 40 and truelove < 50:
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")