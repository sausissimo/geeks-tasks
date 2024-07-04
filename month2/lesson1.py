def isPrime(n):
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return n > 1


def countTwins(n):
    result = set()
    for i in range(n, 2 * n + 1):
        if isPrime(i) and isPrime(i + 2):
            result.add(i)
            result.add(i + 2)
    return len(result)


def main():
    n = int(input())
    print(countTwins(n))


if __name__ == "__main__":
    main()