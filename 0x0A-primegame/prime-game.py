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
    # print(f'start at x: {x} and {nums}')
    # for each round (in x rounds), determine winner
    winners = []
    for n in nums:
        set_ = [i for i in range(1, n + 1)]
        print(f'{n}: {set_}')
        # play (selecting and removing a prime number and its multiples)
        # take turns playing...
        turns = 0
        # primes = []
        # nonPs = []
        for i in set_:
            if isPrime(i):
                turns += 1
                # primes.append(i)
            # else:
                # nonPs.append(i)
        # print(f'set: {set_} -> ps: {primes} & nonPs: {nonPs}')
        winners.append('M' if turns % 2 else 'B')
        # print(f'turns: {turns} -> {winners[-1]}')
    # print('winners: ', winners)
    if winners.count('M') > winners.count('B'):
        winner = 'Maria'
    elif winners.count('M') == winners.count('B'):
        winner = None
    else:
        winner = 'Ben'
    return winner
