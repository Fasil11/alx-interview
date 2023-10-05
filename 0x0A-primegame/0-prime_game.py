#!/usr/bin/python3
"""
The player that cannot make a move loses the game.
"""

def isWinner(x, nums):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_primes(n):
        return [i for i in range(2, n+1) if is_prime(i)]

    def play_round(n):
        primes = get_primes(n)
        if len(primes) % 2 == 1:
            return "Maria"
        else:
            return "Ben"

    ben_wins = 0
    maria_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Ben":
            ben_wins += 1
        elif winner == "Maria":
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
