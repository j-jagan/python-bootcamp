import random

# Coin flip decider using random.randint()
coin_flip_decider = random.randint(0, 1)

if coin_flip_decider == 0:
    print("Heads")
else:
    print("Tails")