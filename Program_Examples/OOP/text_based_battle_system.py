# Part 1: The "Blueprint" (The Parent Class)
# Before we make Heroes or Monsters, we need a generic template for "Things that fight." Let's call it the Character class.

# Your Mission: Write a class called Character.

# __init__: It needs 3 attributes:

# name (e.g., "Conan")

# health (e.g., 100)

# power (e.g., 20 - how hard they hit)

# attack(other): This method controls the fight.

# It takes another character (other) as an input.

# The Logic: specific other.health should decrease by self.power.

# The Print: Print something like: "[Name] attacks [Other Name] for [Power] damage!"

class Character:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, other):
        other.health -= self.power
        print(f"{self.name} attacks {other.name} for {self.power} damage")
        print(f"{other.name} now has {other.health} health left")


# hero = Character("farah", 100, 20)
# enemy = Character("rusu", 100, 10)
# hero.attack(enemy)


# Part 2: Special Moves (Inheritance)
# Now that we have the basic "fight" logic working, let's make specific types of characters with special moves.

# Your Mission: Create a Child class called Warrior that inherits from Character.

# Inherit: It should use the parent's __init__ (you don't need to write init again if you aren't adding new attributes!).

# New Method: Add a method called heal().

# It should add 10 to self.health.

# It should print: "[Name] casts a healing spell! Health is now [Health]."

class Warrior(Character):

    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def heal(self):
        self.health += 10
        print(f"{self.name} casts a healing wspell! Health is now {self.health}")


# warrior = Warrior("Farah", 10, 100)
# warrior.heal()


# Part 3: The Final Boss Battle (The Loop) ⚔️
# Now we combine everything. We want the Hero and a Monster to fight automatically until one of them runs out of health.

# Your Mission: Write a script that:

# Creates a Warrior named "Hero" (Health 100, Power 20).

# Creates a generic Character named "Monster" (Health 100, Power 15).

# Uses a while loop to make them fight.

# The Logic for the Loop:

# Condition: Run the loop as long as hero.health > 0 AND monster.health > 0.

# Inside the loop:

# Hero attacks Monster.

# Check: If Monster is still alive, Monster attacks Hero.

# (Optional) If Hero's health gets low (e.g., < 30), make the Hero use heal() instead of attacking.

hero = Warrior("Farah", 100, 20)
monster = Warrior("Rusu", 100, 15)

while hero.health > 0 and monster.health > 0:
    if hero.health < 30:
        hero.heal()
    else:
        hero.attack(monster)

    if monster.health > 0:
        monster.attack(hero)

    print("----------")

if hero.health > 0:
    print(f"{hero.name} the Hero Wins")
else:
    print(f"{hero.name} the Hero has fallen")
