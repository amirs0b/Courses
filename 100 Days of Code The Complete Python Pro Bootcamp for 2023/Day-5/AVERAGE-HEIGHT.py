# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
hight = sum(student_heights)
count = len(student_heights)

average  = hight / count

print(f"total height = {hight}")
print(f"number of students = {count}")
print(f"average height = {round(average)}")