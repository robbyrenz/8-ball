# A program made in 13/9/2019 on a Friday that simulates the feel of an 8-Ball

import random


def main():
    """The main function of this program"""
    answer = random_answer()
    print_answer(answer)


def random_answer():
    """Randomly returns an answer from a list"""
    # there are 20 answers in the below list (called answers)
    answers = ['It is certain', 'Without a doubt', 'You may rely on it', 'Yes definitely', 'It is decidedly so', 'As I see it, yes', 'Most likely', 'Yes', 'Outlook good', 'Signs point to yes', 'Reply hazy try again', 'Better not tell you now', 'Ask again later', 'Cannot predict now', 'Concentrate and ask again', 'Don’t count on it', 'Outlook not so good', 'My sources say no', 'Very doubtful', 'My reply is no']
    answer = random.choice(answers)
    return answer


def print_answer(answer):
    print()
    print(f"\t\t\t8-Ball says: \"{answer}\"")
    print()


# call main
if __name__ == "__main__":
    main()
