"""
    TODO create pointing system
"""

rows = 2
columns = 2

# rows = int(input("Rows: "))
# columns = int(input("Columns :"))

# p1_name = input("The name of the FIRST player: ")
# p2_name = input("The name of the SECOND player: ")

list_size = (((rows*2)-1)*(columns-1)) + rows - 1

peaked = []
verticals = []
availables = []
horizontals = []
bonus_houses = []
base_elements = []

for i in range((rows-1)*(columns-1)):
    bonus_houses.append(int(i+1))
print(bonus_houses)

counter = 1
while counter <= list_size:
    base_elements.append(counter)
    availables.append(counter)
    counter += 1

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

def score():
    print(str(peaked)+" || "+str(player_input))
    print("col = "+str(columns))
    value = 0
    if (player_input in verticals):
        if (((player_input+columns-1) in peaked) and ((player_input+columns-1) in horizontals))          \
        and (((player_input-columns) in peaked) and ((player_input-columns) in horizontals))             \
        and (((player_input-1) in peaked) and ((player_input-1) in verticals))                           :
            value += 16
        if (((player_input-columns+1) in peaked) and ((player_input-columns+1) in horizontals))          \
        and (((player_input+columns) in peaked) and ((player_input+columns) in horizontals))             \
        and (((player_input+1) in peaked) and ((player_input+1) in verticals))                           :
            value += 4
    if (player_input in horizontals):
        if (((player_input-(2*columns)+1) in peaked) and ((player_input-(2*columns)+1) in horizontals))  \
        and (((player_input-columns+1) in peaked) and ((player_input-columns+1) in verticals))           \
        and (((player_input-columns) in peaked) and ((player_input-columns) in verticals))               :
            value += 2
        if (((player_input+(2*columns)-1) in peaked) and ((player_input+(2*columns)-1) in horizontals))  \
        and (((player_input+columns-1) in peaked) and ((player_input+columns-1) in verticals))           \
        and (((player_input+columns) in peaked) and ((player_input+columns) in verticals))               :
            value += 8

    if value == 0  : print("*** No point ***")
    if value == 2  : print("*** Point on Top ***")
    if value == 4  : print("*** Point on Right ***")
    if value == 8  : print("*** Point on Bottom ***")
    if value == 10 : print("*** Point on Top & Bottom ***")
    if value == 16 : print("*** Point on Left ***")
    if value == 20 : print("*** Point on Right & Left ***")

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
            house_id = "  "
            if str(base_elements[counter]).isnumeric():
                if k+1 == columns : print(str(base_elements[counter])+"  "+house_id+"   ", end="") if base_elements[counter] >= 10 else print("0"+str(base_elements[counter])+"  "+house_id+"   ", end="")
                else:
                    house_id = str(bonus_houses[bonus_houses_counter]) if bonus_houses_counter>=9 else "0"+str(bonus_houses[bonus_houses_counter])
                    print(str(base_elements[counter])+"  "+house_id+"   ", end="") if base_elements[counter] >= 10 else print("0"+str(base_elements[counter])+"  "+house_id+"   ", end="")
                    bonus_houses_counter += 1
            else:
                if k+1 == columns : print("¦   "+house_id+"   ", end="")
                else:
                    house_id = str(bonus_houses[bonus_houses_counter]) if str(bonus_houses[bonus_houses_counter]).isnumeric() else str(bonus_houses[bonus_houses_counter])+" "
                    print("¦   "+house_id+"   ", end="") if bonus_houses_counter>=9 else ( print("¦   0"+house_id+"   ", end="") if str(house_id).isnumeric() else print("¦   "+house_id+"   ", end="") )
                    bonus_houses_counter += 1
            counter += 1
        print()
        counter = stack
        for k in range(columns):
            print("         ", end="") if str(base_elements[counter]).isnumeric() else print("¦        ", end="")
            counter += 1
        print()

print("Availables: "+str(availables))
print("peaked: "+str(peaked))
game_map()
counter = 0
player_input_status = True
while player_input_status and availables:
    print(base_elements)
    # print(availables)
    print(peaked)

    print()

    while True and availables:

        count_down = 4
        player_input_status = False
        while True:
            if count_down == 0 :
                print("Request timed out!")
                break

            player_input = input("{}'s turn ({} chance left): ".format(("A" if counter%2 == 0 else "B"), str(count_down)))
            
            try : player_input = int(player_input)
            except : pass

            if (player_input in availables) and not(player_input in peaked):
                print("{}'s input accepted.".format("A" if counter%2 == 0 else "B"))
                player_input_status = True
                break
            else:
                print("Invalid input!")
                if not player_input :
                    print("   -An input missing.")
                if not(str(player_input).isnumeric()) and player_input :
                    print("   -Input must be integer.")
                if not((player_input in availables) or (player_input in peaked)) and str(player_input).isnumeric() :
                    print("   -This house does not exist.")
                if player_input in peaked :
                    print("   -This house has already been selected.")

            count_down -= 1

        if player_input_status:
            availables.remove(player_input)
            peaked.append(player_input)
            base_elements[player_input-1] = "A" if counter%2 == 0 else "B"

            print("Availables: "+str(availables))
            print("peaked: "+str(peaked))

            value = score()
            if value == 2  :    # write symbol on top
                bonus_houses[horizontals.index(player_input-(2*(columns-1))-1)] = "A" if counter%2 == 0 else "B"
            if value == 4  :    # write symbol on right
                bonus_houses[horizontals.index(player_input-columns+1)] = "A" if counter%2 == 0 else "B"
            if value == 8  :    # write symbol on bottom
                bonus_houses[horizontals.index(player_input)] = "A" if counter%2 == 0 else "B"
            if value == 10 :    # write symbol on top & bottom
                bonus_houses[horizontals.index(player_input-(2*(columns-1))-1)] = "A" if counter%2 == 0 else "B"
                bonus_houses[horizontals.index(player_input)] = "A" if counter%2 == 0 else "B"
            if value == 16 :    # write symbol on left
                bonus_houses[horizontals.index(player_input-columns)] = "A" if counter%2 == 0 else "B"
            if value == 20 :    # write symbol on right & left
                bonus_houses[horizontals.index(player_input-columns+1)] = "A" if counter%2 == 0 else "B"
                bonus_houses[horizontals.index(player_input-columns)] = "A" if counter%2 == 0 else "B"

            print("bonus_houses: "+str(bonus_houses))
            game_map()

            if score() == 0 : break

        else : break
    
    counter += 1