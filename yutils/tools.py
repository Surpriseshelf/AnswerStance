import random
import copy
random.seed(123456)


def shuffle(lol, seed=123456):
    """
    lol :: list of list as input
    seed :: seed the shuffling

    shuffle inplace each list in the same order
    """
    for l in lol:
        random.seed(seed)
        random.shuffle(l)


if __name__ == "__main__":
    print("------------This is for utility test--------------")
    import numpy as np
    a1 = [1, 2, 3, 4, 5, 6]
    a2 = [7, 8, 9, 10, 11, 12]
    a3 = [a1, a2]
    a4 = np.asarray(a1) + 5
    a5 = np.asarray(a2) + 5
    a6 = [a4, a5]

    shuffle(a3, seed=123456)
    shuffle(a6, seed=123456)
    print(a3)
    print(a6)
