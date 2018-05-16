def checkio(data):
    numbers = sorted(data)
    center = len(numbers) / 2
    if len(numbers) % 2 == 0:
        center = int(center)
        return sum(numbers[center - 1:center + 1]) / 2.0
    else:
        return numbers[int(center)]


checkio2 = lambda data: sorted(data)[len(data)//2] if len(data) % 2 == 1 else (sum(sorted(data)[len(data)//2-1:len(data)//2+1])/2)


if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
