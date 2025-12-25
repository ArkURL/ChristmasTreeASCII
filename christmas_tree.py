#!/usr/bin/env python3
"""Christmas Tree Generator - Merry Christmas!"""

import random
import time

# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GOLD = '\033[33m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def generate_tree(height=15):
    """Generate a Christmas tree with ornaments and lights."""
    ornaments = ['@', 'o', '+', '&', '$', '#']
    ornament_colors = [Colors.RED, Colors.YELLOW, Colors.BLUE, Colors.PURPLE, Colors.CYAN, Colors.GOLD]

    lines = []

    # Tree layers
    for i in range(1, height + 1):
        spaces = ' ' * (height - i + 12)
        tree_chars = []

        for j in range(i * 2 - 1):
            rand = random.random()
            if rand < 0.12:
                color = random.choice(ornament_colors)
                tree_chars.append(f'{color}{random.choice(ornaments)}{Colors.RESET}')
            elif rand < 0.20:
                tree_chars.append(f'{Colors.YELLOW}*{Colors.RESET}')
            elif j % 2 == 0:
                shade = Colors.GREEN if random.random() > 0.3 else '\033[32m'
                tree_chars.append(f'{shade}/{Colors.RESET}')
            else:
                shade = Colors.GREEN if random.random() > 0.3 else '\033[32m'
                tree_chars.append(f'{shade}\\{Colors.RESET}')

        lines.append(spaces + ''.join(tree_chars))

    # Trunk - centered under the tree
    # Bottom tree row has (height * 2 - 1) chars starting at 12 spaces
    # Trunk is 3 chars, so center it: 12 + ((height * 2 - 1) - 3) / 2
    trunk_spaces = ' ' * (12 + height - 2)
    for _ in range(3):
        lines.append(f'{trunk_spaces}{Colors.GOLD}|||{Colors.RESET}')

    # Star on top
    star_line = ' ' * (height + 11) + f'{Colors.YELLOW}{Colors.BOLD}*{Colors.RESET}'

    # Print with animation
    print('\n' * 2)
    for line in [star_line] + lines:
        print(line)
        time.sleep(0.03)
    print('\n')

    # Message - centered below trunk
    # Trunk starts at (12 + height - 2), center is at (12 + height - 2 + 1)
    # Message is 28 chars, so start at: (12 + height - 1) - 14 = height - 3
    message = "*  M E R R Y   C H R I S T M A S !  *"
    message_spaces = ' ' * (height - 3)
    print(message_spaces + f'{Colors.RED}{Colors.BOLD}{message}{Colors.RESET}\n')

    # Snow ground
    snow_width = height * 2 + 8
    snow = ' ' * 12 + f'{Colors.WHITE}{Colors.BOLD}' + '.' * snow_width + f'{Colors.RESET}'
    print(snow + '\n')


if __name__ == '__main__':
    print("\n*** Christmas Tree Generator ***\n")
    height = input("Enter tree height (5-30, default 15): ").strip()
    try:
        height = int(height) if height else 15
    except ValueError:
        height = 15

    generate_tree(max(5, min(height, 30)))
