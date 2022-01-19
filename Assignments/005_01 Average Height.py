# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#total = sum(student_heights)
#n = len(student_heights)

# done with for loops

total = 0
n = 0

for i in student_heights:
    total += i
    n += 1


print(int(round(total/n,0)))
