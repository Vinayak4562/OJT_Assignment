def parse_ranges(range_str):
    ranges = range_str.split(',')
    numbers = []
    for r in ranges:
        limits = r.split('-')
        start = int(limits[0])
        end = int(limits[-1]) + 1  # add 1 to include the endpoint
        numbers.extend(range(start, end))
    return numbers

print(parse_ranges('1-2,4-4,8-13'))

# Out put: [1, 2, 4, 8, 9, 10, 11, 12, 13]
