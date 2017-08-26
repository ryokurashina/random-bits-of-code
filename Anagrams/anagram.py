def parse_input():
    a = list(input())
    b = list(input())
    return [a, b]


def anagram():
    # Initialize count of removed letters
    count = 0
    params = parse_input()
    # n is the best case scenario
    # n1 = params[0]
    # n2 = params[1]
    # n = max([len(a), len(b)])
    # Take the bigger one and start stripping off letters.
    len_params = list(map(len, params))
    ind = len_params.index(max(len_params))
    s = params.pop(ind)
    s.sort()
    t = params[0]
    t.sort()
    while s != t:
        for letter in s:
            if letter not in t:
                s.remove(letter)
                count += 1
        for letter in t:
            if letter not in s:
                t.remove(letter)
                count += 1
        # Check for repeats

        params = [s, t]
        len_params = list(map(len, params))
        print(len_params)
        ind = len_params.index(max(len_params))
        s = params.pop(ind)
        s.sort()
        print(s, t)
        t = params[0]
        t.sort()
    print(count)


if __name__ == '__main__':
    anagram()