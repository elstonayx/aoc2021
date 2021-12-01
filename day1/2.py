def main():
    with open('./day1/input.in') as f:
        lines = f.readlines()

    count = 0
    prev_depth = None
    window_size = 3
    for idx in range(len(lines) - window_size + 1):
        curr_depth = (int(lines[idx]) + int(lines[idx + 1]) +
                      int(lines[idx + 2]))
        if not prev_depth:
            prev_depth = curr_depth
            continue

        if curr_depth > prev_depth:
            count += 1

        prev_depth = curr_depth
    print(count)


if __name__ == '__main__':
    main()
