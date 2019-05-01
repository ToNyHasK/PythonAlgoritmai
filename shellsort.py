def shellSort(arr):
    n = len(arr)
    # nustatom gap dydi
    gap = n // 2
    # pradedam cikla
    while gap > 0:
        for i in range(gap, n):
            # issaugom elemta pagal gap
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:

                arr[j] = arr[j - gap]
                j -= gap
                # jei elementas didesnis uz elementa salia jo, paliekam
                # einam prie kito elemento lyginam su j - gap
            arr[j] = temp
        gap //= 2
        # gap sumazeja 1(n/4)


# driver code

arr = [5, 20, 129, 15, 3]

n = len(arr)
print("Pries shell sorta:")
for i in range(n):
    print(arr[i]),

shellSort(arr)

print("\nPo shell sorto:")
for i in range(n):
    print(arr[i]),
