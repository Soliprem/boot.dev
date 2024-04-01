def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")


def subtract(a, b):
    result = a-b
    return result

# Assignment


def triple_damage_combo(attack1, attack2, attack3):
    damage = attack1 + attack2 + attack3
    return damage


triple_damage_combo(200, 150, 100)


def to_celsius(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    return celsius


to_celsius(70)


def hours_to_seconds(hours):
    seconds = hours*3600
    return seconds

# TITLE: Multiple Return Values


def get_user():
    return "name@domain.com@", 21, "active"


email, age, status = get_user()
print(email, age, status)

# Assignment


def become_warrior(first_name, last_name, power):
    full_name = first_name + " " + last_name
    title = full_name + " the warrior"
    full_power = power+1
    return title, full_power


title, full_power = become_warrior("Aang", "Airbender", 100)
print(f"{title} has a power level of {full_power}")

# NOTE: first_name, last_name, power are PARAMETERS
# NOTE: "Aang", "Airbender", 100, are ARGUMENTS

# Default values for Function Aruments


def get_greeting(email, name="there"):
    print(f"Hello {name}, welcome! You've registered your email: {email}")

# Assignment


def get_punched(health, armor=0):
    punch = 50
    damage = punch - armor
    final_health = health - damage
    return final_health


def get_slashed(health, armor=0):
    slash = 50
    damage = slash - armor
    final_health = health - damage
    return final_health

    # Don't touch below this line


def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=====================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=====================================")


test(400, 5)
test(300, 3)
test(200, 1)

# NOTE: PRINTING VS RETURNING


def get_title(arg1, arg2, arg3):
    title = arg1+arg2+arg3
    return title


get_title('I', 'love', 'pizza')


def curse(weapon_damage):
    lesser_cursed = .5 * weapon_damage
    greater_cursed = .25 * weapon_damage
    return lesser_cursed, greater_cursed


curse(200)

# NOTE: Enchant and Attack


def enchant_and_attack(player_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = player_health - enchanted_damage
    enchanted_weapon = 'enchanted ' + weapon
    return enchanted_weapon, new_health


enchant_and_attack(200, 150, 'necksplitter')
