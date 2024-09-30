# Import necessary functions for system commands and terminal size retrieval
from os import system, get_terminal_size

# Get the terminal window's size (columns and lines)
window_size_columns = get_terminal_size().columns
window_size_lines = get_terminal_size().lines

# Get the number of rows and columns for the game board from the user
rows = int(input("Rows: "))
columns = int(input("Columns: "))

# Loop until both player names are provided
while True:
    p1_name = input("The name of the FIRST player: ")
    p2_name = input("The name of the SECOND player: ")

    # Ensure both names are non-empty
    if p1_name and p2_name:
        break

# Initialize variables for the board and gameplay
list_size = (((rows * 2) - 1) * (columns - 1)) + rows - 1
peaked = []           # Tracks the selected points on the board
verticals = []        # Holds vertical positions on the board
availables = []       # Tracks available positions for players
horizontals = []      # Holds horizontal positions on the board
bonus_houses = []     # Additional bonus points for completed boxes
base_elements = []    # Stores the base game elements (board positions)

# Clear the screen
system('cls')

# Create the bonus house elements based on the grid size
for i in range((rows - 1) * (columns - 1)):
    bonus_houses.append(int(i + 1))

# Populate the base_elements and availables lists
counter = 1
while counter <= list_size:
    base_elements.append(counter)
    availables.append(counter)
    counter += 1

# Distribute elements into horizontal and vertical arrays for gameplay logic
counter = 0
for k in range(((rows * 2) - 1)):
    if k % 2 == 0:
        for i in range(columns - 1):
            horizontals.append(base_elements[counter])
            counter += 1
    else:
        for j in range(columns):
            verticals.append(base_elements[counter])
            counter += 1

# Function to display the current score status
def score_status():
    if value == 0: print("==> No point")
    if value == 2: print("==> Point on Top")
    if value == 4: print("==> Point on Right")
    if value == 8: print("==> Point on Bottom")
    if value == 10: print("==> Point on Top & Bottom")
    if value == 16: print("==> Point on Left")
    if value == 20: print("==> Point on Right & Left")

# Function to calculate the score based on player moves
def score_calculator():
    value = 0

    # Check if the selected point is in the vertical lines
    if player_input in verticals:
        # Check for completed boxes to the left and right
        if ((player_input + columns - 1) in peaked and (player_input + columns - 1) in horizontals) and \
           ((player_input - columns) in peaked and (player_input - columns) in horizontals) and \
           ((player_input - 1) in peaked and (player_input - 1) in verticals):
            value += 16
        if ((player_input - columns + 1) in peaked and (player_input - columns + 1) in horizontals) and \
           ((player_input + columns) in peaked and (player_input + columns) in horizontals) and \
           ((player_input + 1) in peaked and (player_input + 1) in verticals):
            value += 4
    
    # Check if the selected point is in the horizontal lines
    if player_input in horizontals:
        # Check for completed boxes above and below
        if ((player_input - (2 * columns) + 1) in peaked and (player_input - (2 * columns) + 1) in horizontals) and \
           ((player_input - columns + 1) in peaked and (player_input - columns + 1) in verticals) and \
           ((player_input - columns) in peaked and (player_input - columns) in verticals):
            value += 2
        if ((player_input + (2 * columns) - 1) in peaked and (player_input + (2 * columns) - 1) in horizontals) and \
           ((player_input + columns - 1) in peaked and (player_input + columns - 1) in verticals) and \
           ((player_input + columns) in peaked and (player_input + columns) in verticals):
            value += 8

    return value

# Function to render the game map/board
def game_map():
    counter = 0
    bonus_houses_counter = 0

    # Loop through each row of the board
    for i in range(rows):
        for j in range(columns - 1):
            print("●", end="")
            if str(base_elements[counter]).isnumeric():
                print("   " + str(base_elements[counter]) + "   ", end="") if base_elements[counter] >= 10 else print("   0" + str(base_elements[counter]) + "   ", end="")
            else:
                print("--------", end="")
            counter += 1
        if counter >= len(base_elements):  # End of row
            print("●")
            break
        print("●")
        
        # Print the vertical lines of the board
        stack = counter
        for k in range(columns):
            print("         ", end="") if str(base_elements[counter]).isnumeric() else print("¦        ", end="")
            counter += 1
        counter = stack
        print()

        # Print the box numbers and the horizontal/vertical separators
        for k in range(columns):
            house_id = "  "
            if str(base_elements[counter]).isnumeric():
                if k + 1 == columns: print(str(base_elements[counter]) + "  " + house_id + "   ", end="") if base_elements[counter] >= 10 else print("0" + str(base_elements[counter]) + "  " + house_id + "   ", end="")
                else:
                    print(str(base_elements[counter]) + "  " + house_id + "   ", end="") if base_elements[counter] >= 10 else print("0" + str(base_elements[counter]) + "  " + house_id + "   ", end="")
                    bonus_houses_counter += 1
            else:
                if k + 1 == columns: print("¦   " + house_id + "   ", end="")
                else:
                    if not str(bonus_houses[bonus_houses_counter]).isnumeric():
                        house_id = str(bonus_houses[bonus_houses_counter]) + " "
                    print("¦   " + house_id + "   ", end="") if bonus_houses_counter >= 9 else (print("¦   0" + house_id + "   ", end="") if str(house_id).isnumeric() else print("¦   " + house_id + "   ", end=""))
                    bonus_houses_counter += 1
            counter += 1
        print()
        counter = stack

        # Print the remaining vertical separators
        for k in range(columns):
            print("         ", end="") if str(base_elements[counter]).isnumeric() else print("¦        ", end="")
            counter += 1
        print()

# Prepare a dashed line separator for the available moves section
dash_count = ""
for i in availables:
    dash_count += str(availables[i - 1]) + "  "
if len(dash_count) + 12 > window_size_columns:
    dash_count = window_size_columns
else:
    dash_count = len(dash_count) + 12

# Display the initial game state
print("-" * dash_count)
print("Availables: " + str(availables))
print("Peaked: " + str(peaked))
print("-" * dash_count)

# Call the game map function to display the board
game_map()
print()

# Initialize variables for gameplay loop
counter = 0
p1_point = 0
p2_point = 0
player_input_status = True

# Main gameplay loop, continues as long as there are available moves
while player_input_status and availables:

    while availables:

        count_down = 4  # Set the number of chances per player
        player_input_status = False

        while True:
            # Determine the current player's turn
            player_turn = p1_name if counter % 2 == 0 else p2_name
            opposite_player = False

            # End turn after 4 invalid attempts
            if count_down == 0:
                opposite_player = p1_name if player_turn == p2_name else p2_name
                print("The number of requests for {} is over!".format(player_turn))
                break

            # Get the player's input (move)
            player_input = input("{}'s turn ({} chance left): ".format(player_turn, str(count_down)))

            # Check if input is valid
            try:
                player_input = int(player_input)
            except:
                pass

            # Validate the player's input
            if (player_input in availables) and not (player_input in peaked):
                system('cls')
                print("{}'s input accepted.".format(player_turn))
                player_input_status = True
                break
            else:
                if not player_input:
                    print("\n---------------------\nInvalid input!\n   -An input missing.\n---------------------\n")
                if not str(player_input).isnumeric() and player_input:
                    print("\n--------------------------\nInvalid input!\n   -Input must be integer.\n--------------------------\n")
                if not ((player_input in availables) or (player_input in peaked)) and str(player_input).isnumeric():
                    print("\n------------------------------\nInvalid input!\n   -This house does not exist.\n------------------------------\n")
                if player_input in peaked:
                    print("\n-----------------------------------------\nInvalid input!\n   -This house has already been selected.\n-----------------------------------------\n")

            count_down -= 1

        # If the input was valid, update the game state
        if player_input_status:
            availables.remove(player_input)
            peaked.append(player_input)
            base_elements[player_input - 1] = p1_name[0] if counter % 2 == 0 else p2_name[0]

            # Display the updated list of available and selected points
            print("-" * dash_count)
            print("Availables: " + str(availables))
            print("Peaked: " + str(peaked))
            print("-" * dash_count, end="\n")

            # Calculate the score based on the move
            value = score_calculator()
            if value == 2:    # Award points for completed box on top
                bonus_houses[horizontals.index(player_input - (2 * (columns - 1)) - 1)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                if counter % 2 == 0:
                    p1_point += 1
                else:
                    p2_point += 1
            if value == 4:    # Award points for completed box on right
                bonus_houses[horizontals.index(player_input - columns + 1)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                if counter % 2 == 0:
                    p1_point += 1
                else:
                    p2_point += 1
            if value == 8:    # Award points for completed box on bottom
                bonus_houses[horizontals.index(player_input)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                if counter % 2 == 0:
                    p1_point += 1
                else:
                    p2_point += 1
            if value == 10:   # Award points for completed boxes on top and bottom
                bonus_houses[horizontals.index(player_input - (2 * (columns - 1)) - 1)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                bonus_houses[horizontals.index(player_input)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                if counter % 2 == 0:
                    p1_point += 2
                else:
                    p2_point += 2
            if value == 16:   # Award points for completed box on left
                bonus_houses[horizontals.index(player_input - columns)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                if counter % 2 == 0:
                    p1_point += 1
                else:
                    p2_point += 1
            if value == 20:   # Award points for completed boxes on left and right
                bonus_houses[horizontals.index(player_input - columns + 1)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                bonus_houses[horizontals.index(player_input - columns)] = p1_name[0] if counter % 2 == 0 else p2_name[0]
                if counter % 2 == 0:
                    p1_point += 2
                else:
                    p2_point += 2

            # Display the updated points for both players
            print("{}'s total point: {}\n{}'s total point: {}".format(p1_name, str(p1_point), p2_name, str(p2_point)))
            print("-" * (len(p1_name) + len(p2_name) + 16), "\n")

            # Update and display the game map
            game_map()
            score_status()
            print()

            if value == 0:
                break

        else:
            break

    counter += 1

# Determine and display the winner
if p1_point > p2_point:
    print(p1_name + " won.")
elif p1_point < p2_point:
    print(p2_name + " won.")
elif (p1_point == p2_point) and opposite_player:
    print(opposite_player + " won.")
elif p1_point == p2_point:
    print("Draw.")
else:
    print("There was a problem in determining the winner!")
