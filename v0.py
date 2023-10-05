from os import system, get_terminal_size


window_size_columns = get_terminal_size().columns
window_size_lines = get_terminal_size().lines

rows = int(input("Rows: "))
columns = int(input("Columns :"))

p1_name = input("The name of the FIRST player: ")
p2_name = input("The name of the SECOND player: ")

list_size = (((rows*2)-1)*(columns-1)) + rows - 1

peaked = []
verticals = []
availables = []
horizontals = []
bonus_houses = []
base_elements = []

system('cls')

for i in range((rows-1)*(columns-1)):
    bonus_houses.append(int(i+1))

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


def score_status():
    if value == 0  : print("==> No point")
    if value == 2  : print("==> Point on Top")
    if value == 4  : print("==> Point on Right")
    if value == 8  : print("==> Point on Bottom")
    if value == 10 : print("==> Point on Top & Bottom")
    if value == 16 : print("==> Point on Left")
    if value == 20 : print("==> Point on Right & Left")


def score_calculator():
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
                    print(str(base_elements[counter])+"  "+house_id+"   ", end="") if base_elements[counter] >= 10 else print("0"+str(base_elements[counter])+"  "+house_id+"   ", end="")
                    bonus_houses_counter += 1
            else:
                if k+1 == columns : print("¦   "+house_id+"   ", end="")
                else:
                    if not str(bonus_houses[bonus_houses_counter]).isnumeric() :
                        house_id = str(bonus_houses[bonus_houses_counter])+" "
                    print("¦   "+house_id+"   ", end="") if bonus_houses_counter>=9 else ( print("¦   0"+house_id+"   ", end="") if str(house_id).isnumeric() else print("¦   "+house_id+"   ", end="") )
                    bonus_houses_counter += 1
            counter += 1
        print()
        counter = stack
        for k in range(columns):
            print("         ", end="") if str(base_elements[counter]).isnumeric() else print("¦        ", end="")
            counter += 1
        print()


dash_count = ""
for i in availables:
    dash_count += str(availables[i-1])+"  "
if len(dash_count)+12>window_size_columns : dash_count=window_size_columns
else : dash_count=len(dash_count)+12

print("-"*dash_count)
print("Availables: "+str(availables))
print("Peaked: "+str(peaked))
print("-"*dash_count)

game_map()
print()
counter = 0
p1_point = 0
p2_point = 0
player_input_status = True
while player_input_status and availables:

    while availables:

        count_down = 4
        player_input_status = False
        while True:
            player_turn = p1_name if counter%2 == 0 else p2_name
            opposite_player = False

            if count_down == 0 :
                opposite_player = p1_name if player_turn == p2_name else p2_name
                print("The number of requests for {} is over!".format(player_turn))
                break
            
            player_input = input("{}'s turn ({} chance left): ".format((player_turn), str(count_down)))
            
            try : player_input = int(player_input)
            except : pass

            if (player_input in availables) and not(player_input in peaked):
                system('cls')
                print("{}'s input accepted.".format(player_turn))
                player_input_status = True
                break
            else:
                if not player_input :
                    print("\n---------------------\nInvalid input!\n   -An input missing.\n---------------------\n")
                if not(str(player_input).isnumeric()) and player_input :
                    print("\n--------------------------\nInvalid input!\n   -Input must be integer.\n--------------------------\n")
                if not((player_input in availables) or (player_input in peaked)) and str(player_input).isnumeric() :
                    print("\n------------------------------\nInvalid input!\n   -This house does not exist.\n------------------------------\n")
                if player_input in peaked :
                    print("\n-----------------------------------------\nInvalid input!\n   -This house has already been selected.\n-----------------------------------------\n")

            count_down -= 1

        if player_input_status:
            availables.remove(player_input)
            peaked.append(player_input)
            base_elements[player_input-1] = p1_name[0] if counter%2 == 0 else p2_name[0]

            print("-"*dash_count)
            print("Availables: "+str(availables))
            print("Peaked: "+str(peaked))
            print("-"*dash_count, end="\n")

            value = score_calculator()
            if value == 2  :    # write symbol on top
                bonus_houses[horizontals.index(player_input-(2*(columns-1))-1)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                if counter%2 == 0 : p1_point += 1
                else : p2_point += 1
            if value == 4  :    # write symbol on right
                bonus_houses[horizontals.index(player_input-columns+1)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                if counter%2 == 0 : p1_point += 1
                else : p2_point += 1
            if value == 8  :    # write symbol on bottom
                bonus_houses[horizontals.index(player_input)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                if counter%2 == 0 : p1_point += 1
                else : p2_point += 1
            if value == 10 :    # write symbol on top & bottom
                bonus_houses[horizontals.index(player_input-(2*(columns-1))-1)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                bonus_houses[horizontals.index(player_input)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                if counter%2 == 0 : p1_point += 2
                else : p2_point += 2
            if value == 16 :    # write symbol on left
                bonus_houses[horizontals.index(player_input-columns)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                if counter%2 == 0 : p1_point += 1
                else : p2_point += 1
            if value == 20 :    # write symbol on right & left
                bonus_houses[horizontals.index(player_input-columns+1)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                bonus_houses[horizontals.index(player_input-columns)] = p1_name[0] if counter%2 == 0 else p2_name[0]
                if counter%2 == 0 : p1_point += 2
                else : p2_point += 2

            print("{}'s total point: {}\n{}'s total point: {}".format(p1_name, str(p1_point), p2_name, str(p2_point)))
            print("-"*(len(p1_name)+len(p2_name)+16), "\n")

            game_map()
            score_status()
            print()

            if value == 0 : break

        else : break

    counter += 1

if p1_point > p2_point : print(p1_name+" won.")
elif p1_point < p2_point : print(p2_name+" won.")
elif (p1_point == p2_point) and opposite_player : print(opposite_player+" won.")
elif p1_point == p2_point : print("Draw.")
else : print("There was a problem in determining the winner!")
