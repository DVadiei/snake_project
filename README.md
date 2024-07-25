# Snake Game

## Overview

This is a classic Snake game built using Pygame. The game allows you to control a snake, consume food to grow, and avoid rocks as you progress through various levels. The game includes features such as selecting different snake colors and food images, adjusting the game speed, and managing scores and levels.

## Features

- **Snake Movement**: Control the snake using arrow keys. The snake speeds up when a key is pressed.
- **Food and Rocks**: Collect food to increase your score and snake length. Avoid rocks that appear as you advance through levels.
- **Levels**: The game increases in difficulty with more rocks and faster speed as you progress through levels.
- **High Score Tracking**: The game tracks and displays the highest score achieved.
- **Color and Food Selection**: Customize your snake color and food type from a selection menu.
- **Background Music**: Enjoy background music that plays throughout the game.
- **Reset Option**: Option to reset high score and game progress.

## Installation

1. **Install Pygame**: Ensure you have Pygame installed. You can install it using pip:
    ```
    pip install pygame
    ```

2. **Download the Game Files**:
    - `snake_game.py` (The main game script)
    - `background_music.mp3` (Background music file)
    - `red.png` (Snake head image)
    - `black.png` (Snake body color(image))
    - `blue.png` (Snake body color(image))
    - `red.png` (Snake body color(image))
    - `orange.png` (Snake body color(image))

    - `food1.png`, `food2.png`, `food3.png` (Food images)
    - `highscore.txt` (File to store high score, initially empty)
    - `last_level.txt` (File to store the last level, initially set to level 1)


3. **Place the Files**: Ensure all files are in the same directory.

## Usage

1. **Run the Game**:
    ```
    python snake_game.py
    ```

2. **Game Controls**:
    - **Arrow Keys**: Control the snake's direction.
    - **Mouse**: Select snake color and food type from the menu.
    - **'C' Key**: Continue the game after a game over.
    - **'Q' Key**: Quit the game.
    - **'R' Key**: Reset high score and game progress.

3. **Game Menu**:
    - **Select Snake Color**: Choose from various colors displayed as buttons.
    - **Select Food Type**: Choose from different food images.
    - **Start and Quit Game**: Press 'C' to start the game or 'Q' to quit from the menu.
    - **Restart Game**: At the end of the game, press 'R' to restart the game.

4. **In-Game**:
    - **Score**: Your current score is displayed at the top left.
    - **Level**: The current level is shown at the top right.
    - **Color_Menu**: You can change the color of snake's body during while playing.
    - **Game Over**: Displays your score, the highest score, and provides options to restart or quit.

## Customization

- **Snake Colors**: Modify the `SNAKE_COLORS` list to include additional colors.
- **Food Images**: Add more food images by placing them in the directory and updating the `SNAKE_FOODS` list.
- **Background Music**: Change the music file by replacing `background_music.mp3` with another MP3 file.

## Files

- `snake_project_version18.py`: Main game script containing all the logic for gameplay, menu, and display.
- `background_music.mp3`: Music file played in the background during the game.
- `red.png`: Image used for the snake's head.
- `black.png`: Image used for the snake's body.
- `blue.png`: Image used for the snake's body.
- `red.png`: Image used for the snake's body.
- `orange.png`: Image used for the snake's body.
- `food1.png`, `food2.png`, `food3.png`: Images used for food items.
- `highscore.txt`: Stores the highest score achieved.
- `last_level.txt`: Stores the last level played.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
