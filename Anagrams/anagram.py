def parse_input():
    a = list(input())
    b = list(input())
    return [a, b]


def anagram():
    # Initialize count of removed letters
    count = 0
    params = parse_input()
    s = params[0]
    t = params[1]
    while s != t:
        for letter in s:
            if s.count(letter) > t.count(letter):
                for i in range(s.count(letter)-t.count(letter)):
                    s.remove(letter)
                    count += 1
        for letter in t:
            if t.count(letter) > s.count(letter):
                for i in range(t.count(letter)-s.count(letter)):
                    t.remove(letter)
                    count += 1
    print(count)


if __name__ == '__main__':
    anagram()