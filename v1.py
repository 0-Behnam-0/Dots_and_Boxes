rows = 3
columns = 3
# rows = int(input("Rows: "))
# columns = int(input("Columns :"))
list_size = (((rows*2)-1)*(columns-1)) +rows -1

base_elements = []
counter = 1
while counter<=list_size :
    base_elements.append(counter)
    counter += 1

verticals = []
horizontals = []

counter = 0
for k in range(((rows*2)-1)):
    if k%2 == 0:
        for i in range(columns-1):
            horizontals.append(base_elements[counter])
            counter += 1
    else:
        for j in range(columns):
            verticals.append(base_elements[counter])
            counter += 1

print("horizontals: "+str(horizontals))
print("verticals: "+str(verticals))

# availables = base_elements.copy()

# print(availables)


def game_map():
    for i in range(((rows*2)-1)):
        if i%2 == 0:
            for j in range(columns-1):
                print("*         ",end="")
            print("*")
        else:
            for j in range(columns) : print("        ",end="")
            print()
            for j in range(columns):
                print("11        ",end="")
            print()
            for j in range(columns) : print("        ",end="")
            print()

# player_input = int(input("input: "))
# base_elements[player_input-1] = "x"

print(base_elements)
# print(availables)

game_map()