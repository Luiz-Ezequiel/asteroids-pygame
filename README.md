# Simple Asteroids Game

This is a simple Asteroids game made using Python and Pygame. The player controls a spaceship that must avoid and destroy asteroids while surviving for as long as possible.

## Features

- Player movement and rotation
- Shooting projectiles to destroy asteroids
- Asteroid splitting upon collision
- Infinite spawning of asteroids at random edges of the screen

## How to Play

- Rotate Left: `A`
- Rotate Right: `D`
- Move Forward: `W`
- Move Backward: `S`
- Shoot: `SPACE`
  The goal is to avoid colliding with asteroids while shooting them. Each asteroid splits into smaller pieces when hit.

## Instalation

1. Clone the repo:

```bash
git clone https://github.com/Luiz-Ezequiel/asteroids-pygame.git
cd asteroids-pygame
```

2. Install the required packages using 'requirements.txt':

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

## Project Structure

```bash
asteroids-pygame/
│
├── main.py             # Main game loop
├── player.py           # Player class and movement/shooting logic
├── shot.py             # Shot class for projectiles shot by player
├── asteroid.py         # Asteroid class with splitting logic
├── asteroidfield.py     # Manages spawning asteroids
├── circleshape.py      # Base class for base game object with collision logic
├── constants.py        # Game constants (screen size, speeds, etc)
└── requirements.py     # List of required packages
```

## Future Improvements

- Add scoring system
- Implement multiple lives and respawning
- Add explosion effect
- Add acceleration to player movement
- Make more weapon types
- Add power ups
