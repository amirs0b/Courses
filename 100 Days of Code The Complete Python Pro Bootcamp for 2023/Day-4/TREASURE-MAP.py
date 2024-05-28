line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


#my code
row = position[0].lower()
column = int(position[1])-1

if row == "a":
    row = 0
elif row == "b":
    row = 1
elif row == "c":
    row = 2
map[column][row] = "X"
#second solution

row = int(position[1])-1
column = {"A":0,
         "B":1,
         "C":2}
map[row][column[position[0]]] = "X"

#third solution

row = position[0].lower()
column = int(position[1])-1

if row in ['a', 'b', 'c']:
    map[column][ord(row) - ord('a')] = "X"

#lecturer

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")A2
