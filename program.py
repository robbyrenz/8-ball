# A program I made in 13/9/2019 on a Friday that simulates the feel of an 8-Ball

import random


def main():
    """The main function of this program"""
    print(random_answer())


def random_answer():
    """Randomly returns an answer from a list"""
    answers = []
    answer = random.choice(answers)
    return answer


# call main
if __name__ == "__main__":
    main()
