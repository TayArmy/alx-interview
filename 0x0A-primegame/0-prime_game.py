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


def SieveOfAtkin(limit):
    """ Generate all prime numbers upto and including limit """
    # 2 and 3 are known
    # to be prime
    count = 0
    if limit == 2 or limit == 3:
        count += 1
    if limit > 2:
        count += 1
    if limit > 3:
        count += 1

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    """ Mark sieve[n] is True if
        one of the following is True:
        a) n = (4*x*x)+(y*y) has odd
        number of solutions, i.e.,
        there exist odd number of
        distinct pairs (x, y) that
        satisfy the equation and
        n % 12 = 1 or n % 12 = 5.
        b) n = (3*x*x)+(y*y) has
        odd number of solutions
        and n % 12 = 7
        c) n = (3*x*x)-(y*y) has
        odd number of solutions,
        x > y and n % 12 = 11
    """
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False

        r += 1

        # Print primes
    # using sieve[]
    for a in range(5, limit+1):
        if sieve[a]:
            count += 1
    return count


def isWinner(x, nums):
    """ returns the winner of the game
        Args:
            x - the number of rounds the game will be played
            nums - an array of `n`s where:
            n - is the inclusive upper bound of the set of consecutive
                integers from which the prime numbers and their multiples
                are removed (that's the game)
    """
    if x == 0 or not len(nums) or len(nums) != x:
        return None
    # print(f'start at x: {x} and {nums}')
    # for each round (in x rounds), determine winner
    winners = []
    # w2 = []
    for n in nums:
        set_ = [i for i in range(1, n + 1)]
        # compare answers:
        counter = SieveOfAtkin(n)
        # w2.append('M' if counter % 2 else 'B')
        # play (selecting and removing a prime number and its multiples)
        # take turns playing...
        # turns = 0
        # for i in set_:
        #     if isPrime(i):
        #         turns += 1
        turns = counter
        winners.append('M' if turns % 2 else 'B')
        # print(set_)
        # print(f'turns: {turns} -> {winners[-1]} and count: {counter}')
    # print('winners: ', winners)
    if winners.count('M') > winners.count('B'):
        winner = 'Maria'
    elif winners.count('M') == winners.count('B'):
        winner = None
    else:
        winner = 'Ben'
    # if w2.count('M') > w2.count('B'):
    #     w = 'Maria'
    # elif w2.count('M') == w2.count('B'):
    #     w = None
    # else:
    #     w = 'Ben'
    # print('winner v2: ', w)
    return winner