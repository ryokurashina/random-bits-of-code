def parse_args():
    params = list(map(int, input().split(" ")))
    unshifted = list(map(int, input().split(" ")))
    return [params, unshifted]


def left_rotate():
    [params, unshifted] = parse_args()
    # Define n and d
    n = params[0]
    d = params[1]
    # Create empty list to append shifted integers
    shifted = []
    for i in range(n):
        old_ind = (d + i) % n
        shifted.append(unshifted[old_ind])
    for item in shifted:
        print(item, end=" ")


if __name__ == '__main__':
    left_rotate()