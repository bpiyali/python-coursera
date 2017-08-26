#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    random_values = []
    for i in range(0, 10):
        random_values.append(30 + 5 * random.random())
    print(random_values)

