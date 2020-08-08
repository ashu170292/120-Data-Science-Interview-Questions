import random


def roll_die():
    return random.randint(1, 6)


def gen_rand_num_from_dice():
    """
    3) How can you generate a random number between 1 - 7 with only a die?
    """
    while True:
        roll1, roll2 = roll_die(), roll_die()
        num = roll1 * 6 + roll2
        if num == 42:
            continue
        return num % 7
