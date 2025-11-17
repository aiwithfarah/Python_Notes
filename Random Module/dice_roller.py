import random

# print("\u25CF \u250F \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┏ ─ ┐ │ └ ┘

"┏─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: (
        "┏─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┏─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┏─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┏─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┏─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┏─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
print(dice)

# display ASCII art
for die in range(num_of_dice):
    for art in dice_art.get(dice[die]):
        print(art)

for die in dice:
    total += die

print(f"Total: {total}")
