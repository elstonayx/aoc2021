def main():
    with open('./day1/input.in') as f:
        lines = f.readlines()

    count = 0
    prev_depth = None
    for line in lines:
        curr_depth = int(line)
        if not prev_depth:
            prev_depth = curr_depth
            continue

        if curr_depth > prev_depth:
            count += 1

        prev_depth = curr_depth
    print(count)


if __name__ == '__main__':
    main()
