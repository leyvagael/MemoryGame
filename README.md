# 🧠 Memory

A Python implementation of the classic Memory card matching game, built using the `turtle` graphics library and the `freegames` package. By Gael Leyva and Emma Sofía García.

## Overview

Sixteen tiles are arranged in a 4x4 grid, hiding pairs of letters beneath them. The player clicks tiles to reveal their letters and tries to find all eight matching pairs. A tap counter tracks how many clicks the player has used, and a win message is displayed when all pairs have been matched.

## Requirements

- Python 3.x
- [`freegames`](https://pypi.org/project/freegames/) library

Install the dependency with:

```bash
pip install freegames
```

## How to Run

```bash
python3 memory.py
```

## Controls

| Input | Action |
|---|---|
| `Mouse click` | Reveal a tile |

## Changes from the Original

### 1. Tap counter
Every click is counted and displayed in the top-left corner of the screen, letting the player track how many attempts it took them to finish the game.

### 2. 4x4 grid
The board was reduced from the original 8x8 layout to a smaller 4x4 grid with 8 letter pairs, making for a quicker and more approachable game.

### 3. Win detection
The game now detects when all tiles have been revealed. Once the last pair is matched, a "You win!" message is displayed at the center of the screen and the game loop stops.

### 4. Centered tile letters
The letter displayed on a revealed tile is now centered within the tile, using a corrected cursor position.

### 5. Letters instead of numbers
Tiles now show letters (`a` through `h`) instead of numbers, giving the game a different feel and making pairs slightly harder to spot at a glance.
