while True:
    lists = []
    n = int(input())

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            lists.append(i)

    if sum(lists) == n:
        a = (str(i) for i in lists)
        print(n, " = ", " + ".join(a), sep="")
    else:
        print(n, "is NOT perfect.")
