# 🚨 Don't change the code below 👇

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
original = position
pos1 = int(position%10 - 1)
pos2 = int(original/10 - 1)
map[pos1][pos2] = 'x'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")