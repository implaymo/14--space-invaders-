# Space Invaders Game

## Overview
Space Invaders is a classic arcade-style game where players control a spaceship to defend against waves of aliens. The objective is to survive as long as possible by destroying incoming aliens while avoiding their projectiles.

## Features
- **Increasing Difficulty**: As the player progresses through levels, the number of aliens and their speed increases, providing a greater challenge.
- **Dynamic Gameplay**: The number of rows in aliens increases by 1 with each level, creating a more complex playing field.
- **Lives System**: The player's spaceship has a limited number of lives. Getting hit by an alien's projectile reduces the number of lives remaining.
- **Scoring**: The game only tracks the highscore, which increases with each successive level achieved.
- **Level Progression**: Upon wiping out all aliens on the screen, the player advances to the next level, where the difficulty increases.

## Controls
- **Arrow Keys**: Move the spaceship left or right.
- **Spacebar**: Shoot bullets to destroy aliens.

## Gameplay Mechanics
- **Aliens**: Aliens move horizontally across the screen and periodically drop projectiles towards the player's spaceship. When hit by a bullet, an alien is destroyed.
- **Spaceship**: The player's spaceship is positioned at the bottom of the screen and can move horizontally to avoid alien projectiles. It can shoot bullets to destroy aliens. When hit by a bullet, a life is lost.
- **Level Progression**: Each level presents an increasing number of aliens and rows, as well as faster-moving projectiles.
- **Game Over**: The game ends when the player's spaceship loses all lives. The final score is displayed along with an option to restart the game.

## Getting Started
To run the game, follow these steps:
1. Clone this repository to your local machine.
2. Open the project in your preferred programming environment.
3. Run the main game file.
4. Use the arrow keys to move the spaceship and the spacebar to shoot bullets.

## Requirements
- This game is built using Python and Pygame library.
- Ensure you have the following installed on your machine:
  - Python 3.12.0
  - Pygame 2.5.2

To install Pygame, use pip:
```bash
pip install pygame
```

## Future Improvements
- Implement power-ups for the spaceship, such as shields or faster bullets.
- Add different types of aliens with unique behaviors.
- Provide options for customization, such as adjusting difficulty levels or spaceship appearance.
## Credits
- Developed by implaymo
