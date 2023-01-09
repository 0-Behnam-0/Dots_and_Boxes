rows = 3
columns = 3

# rows = int(input("Rows: "))
# columns = int(input("Columns :"))
list_size = (((rows*2)-1)*(columns-1)) + rows - 1

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
    return value
    # if value == 0: print("*** No point ***")
    # if value == 2: print("*** Point on Top ***")
    # if value == 4: print("*** Point on Right ***")
    # if value == 8: print("*** Point on Bottom ***")
    # if value == 10: print("*** Point on Top & Bottom ***")
    # if value == 16: print("*** Point on Left ***")
    # if value == 20: print("*** Point on Right & Left ***")


def game_map():
    counter = 0
    for i in range(rows):
        for j in range(columns-1):
            print("●", end="")
            if str(base_elements[counter]).isnumeric():
                print("   "+str(base_elements[counter])+"   ", end="") if base_elements[counter] >= 10 else print(
                    "   0"+str(base_elements[counter])+"   ", end="")
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
                print(str(base_elements[counter])+"       ", end="") if base_elements[counter] >= 10 else print(
                    "0"+str(base_elements[counter])+"       ", end="")
            else:
                print("¦        ", end="")
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

    
    if counter%2 == 0:
        while True:
            player_input = int(input("Player A turn: "))
            peaked.append(base_elements[player_input-1])
            base_elements[player_input-1] = "A"
            game_map()
            if score()==0 :
                break
    else:
        while True:
            player_input = int(input("Player B turn: "))
            peaked.append(base_elements[player_input-1])
            base_elements[player_input-1] = "B"
            game_map()
            if score()==0 :
                break



    counter += 1