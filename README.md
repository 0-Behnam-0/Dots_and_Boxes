<style>
    @font-face {
        font-family: Font;
        src: url('font.ttf');
    }
    body {
        font-family: Font;
        font-size: 15px;
    }
</style>

# Dots and Boxes Game

This is a Python implementation of the classic Dots and Boxes game.  
The game is played on a rectangular grid of dots, where two players take turns connecting adjacent dots with horizontal or vertical lines.  
When a player completes a box, they score a point and get to make another move. The player with the most points at the end of the game wins.

## Requirements

- `Python 3.x`

## How to Play

1. Run the **dots_and_boxes.py** file in a Python environment.
2. Enter the number of rows and columns for the game board.
3. Enter the names of the two players.
4. The game board will be displayed, with each dot numbered.
5. Players take turns entering the number of the dot they want to connect.
6. If a player completes a box, they score a point and get to make another move.
7. The game ends when all boxes have been completed.
8. The player with the most points wins.

## Features

- The game board is dynamically generated based on the user's input for rows and columns.
- The game keeps track of each player's score and displays it after each move.
- The game checks for valid input and prevents players from selecting the same dot twice.
- The game ends automatically when all boxes have been completed.
- The winner is determined by the player with the most points.

## Issues and Feedback

If you encounter any issues while playing the game or have any feedback to share, please feel free to open an issue on this repository.  
We welcome all contributions and suggestions for improving the game.

## Credits

This game was created by [Mahdi Mohamadiha](https://github.com/0-Behnam-0/).
