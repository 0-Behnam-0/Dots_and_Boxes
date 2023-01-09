from math import ceil

rows = 6
columns = 6

# rows = int(input("Rows: "))
# columns = int(input("Columns :"))
list_size = (((rows*2)-1)*(columns-1)) + rows - 1

bonus_houses = []
for i in range((rows-1)*(columns-1)):
    bonus_houses.append(int(i+1))
print(bonus_houses)


peaked = []

base_elements = []
counter = 1
while counter <= list_size:
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

# availables = base_elements.copy()
# print(availables)


def score():
    print(str(peaked)+" || "+str(player_input))
    print("col = "+str(columns))
    value = 0
    if (player_input in verticals):
        if ((player_input-columns) in peaked) and ((player_input+columns-1) in peaked) and ((player_input-1) in peaked):
            value += 16
        if ((player_input-columns+1) in peaked) and ((player_input+1) in peaked) and ((player_input+columns) in peaked):
            value += 4
    if (player_input in horizontals):
        if ((player_input-columns) in peaked) and ((player_input-columns+1) in peaked) and ((player_input-(2*columns)+1) in peaked):
            value += 2
        if ((player_input+columns) in peaked) and ((player_input+columns-1) in peaked) and ((player_input+(2*columns)-1) in peaked):
            value += 8
    if value == 0: print("*** No point ***")
    if value == 2: print("*** Point on Top ***")
    if value == 4: print("*** Point on Right ***")
    if value == 8: print("*** Point on Bottom ***")
    if value == 10: print("*** Point on Top & Bottom ***")
    if value == 16: print("*** Point on Left ***")
    if value == 20: print("*** Point on Right & Left ***")
    return value


def game_map():
    counter = 0
    bonus_houses_counter = 0
    for i in range(rows):
        for j in range(columns-1):
            print("●", end="")
            if str(base_elements[counter]).isnumeric():
                print("   "+str(base_elements[counter])+"   ", end="") if base_elements[counter] >= 10 else print("   0"+str(base_elements[counter])+"   ", end="")
            else:
                print("--------", end="")
            counter += 1
        if counter >= len(base_elements):  # break point (always runs onec only)
            print("●")
            break
        print("●")
        stack = counter
        for k in range(columns):
            print("         ", end="") if str(
                base_elements[counter]).isnumeric() else print("¦        ", end="")
            counter += 1
        counter = stack
        print()
        for k in range(columns):
            if str(base_elements[counter]).isnumeric():
                if k+1 == columns:
                    house_id = "  "
                    print(str(base_elements[counter])+"  "+house_id+"   ", end="") if base_elements[counter] >= 10 else print("0"+str(base_elements[counter])+"  "+house_id+"   ", end="")
                else:
                    house_id = str(bonus_houses[bonus_houses_counter]) if bonus_houses_counter>=9 else "0"+str(bonus_houses[bonus_houses_counter])
                    print(str(base_elements[counter])+"  "+house_id+"   ", end="") if base_elements[counter] >= 10 else print("0"+str(base_elements[counter])+"  "+house_id+"   ", end="")
                    bonus_houses_counter += 1
            else:
                if k+1 == columns:
                    house_id = " "
                    print("¦   "+house_id+"    ", end="")
                else:
                    house_id = str(bonus_houses[bonus_houses_counter]) if str(bonus_houses[bonus_houses_counter]).isnumeric() else str(bonus_houses[bonus_houses_counter])+" "
                    print("¦   "+house_id+"   ", end="") if bonus_houses_counter>=9 else print("¦   0"+house_id+"    ", end="")
                    bonus_houses_counter += 1
            counter += 1
        print()
        counter = stack
        for k in range(columns):
            print("         ", end="") if str(base_elements[counter]).isnumeric() else print("¦        ", end="")
            counter += 1
        print()


game_map()
counter = 0
while True:
    print(base_elements)
    # print(availables)
    print(peaked)

    print()

    while True:
        player_input = int(input("Player {} turn: ".format("A" if counter%2 == 0 else "B")))
        peaked.append(base_elements[player_input-1])
        base_elements[player_input-1] = "A" if counter%2 == 0 else "B"
        row_index = ceil(player_input/rows)-1

        if score() == 2 : bonus_houses[horizontals.index(player_input-(2*(columns-1))-1)] = "A" if counter%2 == 0 else "B"    # write letter on top
        if score() == 4 : bonus_houses[horizontals.index(player_input-columns+1)] = "A" if counter%2 == 0 else "B"    # write letter on right
        if score() == 8 : bonus_houses[horizontals.index(player_input)] = "A" if counter%2 == 0 else "B"    # write letter on bottom
        if score() == 16 : bonus_houses[horizontals.index(player_input-columns)] = "A" if counter%2 == 0 else "B"    # write letter on left

        print("bonus_houses: "+str(bonus_houses))
        game_map()

        if score() == 0 : break


    counter += 1