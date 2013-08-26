__author__ = 'gigi'


RANGE_SIZE = 100
primes = [2, 3, 5, 7]

last_range_start = None


def get_next_range():
    global last_range_start
    if last_range_start is None:
        last_range_start = 10
    else:
        last_range_start += RANGE_SIZE

    return last_range_start, last_range_start + RANGE_SIZE


def check_range(start, end, primes):
    """Use Sieve of Eratosthenes algorithm

    Start with an array of booleans initialized to True
    Set non-primes to False by skipping multiples of each of the input primes
    Return a list of the resulting primes
    """
    candidates = [True] * RANGE_SIZE
    for p in primes:
        first_candidate = (start / p * p)
        if first_candidate < start:
            first_candidate += p

        index = first_candidate - start
        while index < end - start:
            candidates[index] = False
            index += p

    primes = [start + i for i in xrange(len(candidates)) if candidates[i]]
    return primes

def store_new_primes(new_primes):
    global primes
    primes += new_primes


def main():
    while True:
        start, end = get_next_range()
        new_primes = check_range(start, end, primes)
        store_new_primes(new_primes)


def test():
        start, end = get_next_range()
        new_primes = check_range(start, end, primes)
        print new_primes

if __name__ == '__main__':
    test()
