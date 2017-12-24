def max_pairwise_product(n, a):
    max1 = -1
    max2 = -1
    for i in range(0, n):
        if (a[i] > a[max1]):
            max1 = i

    for i in range(0, n):
        if (i != max1 and a[i] > a[max2]):
            max2 = i
    return (a[max1]*a[max2])

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    print(max_pairwise_product(n,a))