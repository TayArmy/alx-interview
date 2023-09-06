#!/usr/bin/python3
""" Determines the winner of a 2 player prime game in x rounds of the game """


def isPrime(x):
    """ returns True if x is a prime number and False otherwise """
    if x == 1:
        return False
    i = 2  # 1 is not a prime number (start at 2)
    while i < x:
        if not x % i:
            return False
        i += 1
    return True


def isMultiple(x, y):
    """ returns True if y is a multiple of x and False otherwise """
    return not y % x


def isWinner(x, nums):
    """ returns the winner of the game
        Args:
            x - the number of rounds the game will be played
            nums - an array of `n`s where:
            n - is the inclusive upper bound of the set of consequitive
                integers from which the prime numbers and their multiples
                are removed (that's the game)
    """
    if x == 0 or not len(nums) or len(nums) != x:
        return None
    print(f'start at x: {x} and {nums}')
    # for each round (in x rounds), determine winner
    winners = []
    for n in nums:
        set_ = [i for i in range(1, n + 1)]
        print(f'{n}: {set_}')
        # play (selecting and removing a prime number and its multiples)
        # take turns playing...
        turns = 0
        primes = []
        for idx, i in enumerate(set_):
            if isPrime(i):
                primes.append(i)
                new = set_[:idx] + set_[idx + 1:]
                # remove multiples of i from new
                looper = []
                turns += 1
                for x in new:
                    if not isMultiple(i, x):
                        looper.append(x)
                # reset set_ (to looper -- whatever is left in set)
                set_ = looper
                print(f'new set_: {set_}')
        winners.append('M' if turns % 2 else 'B')
        print(f'turns: {turns} -> {winners[-1]} and primes: {primes}')
    print('winners: ', winners)
    if winners.count('M') > winners.count('B'):
        winner = 'Maria'
    elif winners.count('M') == winners.count('B'):
        winner = None
    else:
        winner = 'Ben'
    return winner
