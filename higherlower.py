import random
import os
from higherlower_art import logo, vs
from higherlower_data import data

D = data

def random_pick():
    random.shuffle(D)
    return D.pop()

def format_print(x):
    return f"{x['name']}, a {x['description']}, from {x['country']}."

def is_correct(x, y, z):
    if y > z:
        return x == "a"
    else:
        return x == "b"

def play():
    os.system('cls')
    print(logo)
    i = 0
    b = random_pick()
    while i <= len(D):
        if i == 0:
            a = random_pick()
        a_num = a['follower_count'] 
        b_num = b['follower_count']
        print("Compare A: " + format_print(a))
        print(vs)
        print("Against B: " + format_print(b))
        u = input("Who has more followers?  Type 'A' or 'B': ").lower()
        os.system('cls')
        print(logo)
        if is_correct(u, a_num, b_num):
            i += 1
            print(f"You're right!  Current score: {i}.")
        else:
            print(f"Sorry, that's wrong.  Final Score: {i}")
            return
        if u == 'a':
            a = a
        else:
            a = b
        b = random_pick()

play()


