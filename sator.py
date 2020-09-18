def main():
    sator = [
        ["s", "a", "t", "o", "r"],  # The sower
        ["a", "r", "e", "p", "o"],  # Arepo
        ["t", "e", "n", "e", "t"],  # with his plough
        ["o", "p", "e", "r", "a"],  # holds the wheels
        ["r", "o", "t", "a", "s"]   # with care
    ]

    for row in sator:
        for char in row:
            print(char.upper(), end=' ')
        print('', sep='\n')

    print('\n')

    for row in sator[::-1]:
        for char in row:
            print(char.upper(), end=' ')
        print('', sep='\n')

    print('\n')

    for row in sator:
        for char in row[::-1]:
            print(char.upper(), end=' ')
        print('', sep='\n')

    print('\n')

    for row in sator[::-1]:
        for char in row[::-1]:
            print(char.upper(), end=' ')
        print('', sep='\n')


if __name__ == "__main__":
    main()
