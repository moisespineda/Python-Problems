#A string contains a list of color names that are separated by single space. The list is mixed but each color has its position number at the end of each color name. Sort the list to the position that it has to have following the number at end of each color...

#Example: "red2 blue5 black4 green1 gold3" --->  green red gold black blue

string="red2 blue5 black4 green1 gold3"
# red2 blue5 black4 green1 gold3
new_string=string.split(" ")
# ['red2', 'blue5', 'black4', 'green1', 'gold3']

ordenado=sorted(new_string, key=lambda row: int(row[-1]))
# ['green1', 'red2', 'gold3', 'black4', 'blue5']

lista=""
for j in ordenado:
    #take the character from each elements until the last character before the str(number) and it is added to a new string
    lista+=j[:-1] + " "
# the list output has to be -> green red gold black blue

print(lista)
# green red gold black blue

