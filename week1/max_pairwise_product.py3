# Uses python3


def max_pairwise_product(n, a):
    max1 = 0
    max2 = 0
    for i in range(0, n):
        if (a[i] > max1):
            max1 = a[i]

    for i in range(0, n):
        if (a[i] != max1 and a[i] > max2):
            max2 = a[i]
    return (max1*max2)


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    print(max_pairwise_product(n,a))