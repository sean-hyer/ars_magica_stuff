# So in a combat round, each character makes an attack and a defense roll
# We'll assume they act simultaneously
import random

player_1_attack = 17
player_1_defense = 15
player_1_damage = 8
player_1_soak = 9
player_1_size = 5

player_2_attack = 19
player_2_defense = 27
player_2_damage = 8
player_2_soak = 2
player_2_size = 5


def botch_roll():
    roll = random.randint(1, 10)
    if roll == 10:
        botch = random.randint(1, 10)
        if botch == 10:
            return -1
        else:
            return 0
    elif roll == 1:
        roll = multiply_roll(2)
    return roll


def multiply_roll(multiplier):
    roll = random.randint(1, 10)
    if roll == 1:
        roll = multiply_roll(multiplier*2)
        return (roll)
    else:
        return (roll*multiplier)


def attack_roll(attacker, player_1_wounds, player_2_wounds):
    if attacker == "player_1":
        player_1_roll = botch_roll()
        if player_1_roll == -1:
            player_1_roll = 0
        else:
            player_1_roll = player_1_roll + player_1_attack + player_1_wounds
        player_2_roll = botch_roll()
        if player_2_roll == -1:
            player_2_roll = 0
        else:
            player_2_roll = player_2_roll + player_2_defense + player_2_wounds
        if player_1_roll > player_2_roll:
            return (player_1_roll-player_2_roll)
        else:
            return -100  # this is arbitrary
    elif attacker == "player_2":
        player_2_roll = botch_roll()
        if player_2_roll == -1:
            player_2_roll = 0
        else:
            player_2_roll = player_2_roll + player_2_attack + player_2_wounds
        player_1_roll = botch_roll()
        if player_1_roll == -1:
            player_1_roll = 0
        else:
            player_1_roll = player_1_roll + player_1_defense + player_1_wounds
        if player_2_roll > player_1_roll:
            return (player_2_roll-player_1_roll)
        else:
            return -100
    else:
        print("SOMETHING IS WRONG!!!!")


def wounding(attacker, win_by):
    if attacker == "player_1":
        win_by = win_by + player_1_damage - player_2_soak
        if win_by > 3*player_2_size:
            return "player_2_dead"
        elif win_by > 2*player_2_size:
            return -5
        elif win_by > player_2_size:
            return -3
        elif win_by > 0:
            return -1
        else:
            return 0
    elif attacker == "player_2":
        win_by = win_by + player_2_damage - player_1_soak
        if win_by > 3*player_1_size:
            return "player_1_dead"
        elif win_by > 2*player_1_size:
            return -5
        elif win_by > player_1_size:
            return -3
        elif win_by > 0:
            return -1
        else:
            return 0
    else:
        print("SOMETHING IS WRONG!!!!")


def fight():
    player_1_wounds = 0
    player_2_wounds = 0
    while True:
        p1_attack = attack_roll("player_1", player_1_wounds, player_2_wounds)
        p2_attack = attack_roll("player_2", player_1_wounds, player_2_wounds)
        p2_wound = wounding("player_1", p1_attack)
        p1_wound = wounding("player_2", p2_attack)
        if p2_wound == "player_2_dead":
            if p1_wound == "player_1_dead":
                return "draw"
            else:
                return "player_1_wins"
        elif p1_wound == "player_1_dead":
            return "player_2_wins"
        else:
            player_2_wounds += p2_wound
            player_1_wounds += p1_wound


player_1_wins = 0
player_2_wins = 0
draws = 0

for i in range(1, 10000):
    result = fight()
    if result == "player_2_wins":
        player_2_wins += 1
    elif result == "player_1_wins":
        player_1_wins += 1
    else:
        draws += 1
print("player_1 won ", player_1_wins)
print("player_2 won ", player_2_wins)
print("they drew ", draws)
