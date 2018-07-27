# Uses python3


def fast_count_segments(segments, points):
    starts = [(x[0], 'l') for x in segments]
    ends = [(x[1], 'r') for x in segments]
    pointers = [(x, 'p') for x in points]
    combined = sorted(starts + ends + pointers)
    result_dict = {}
    open_segment_count = 0
    for point in combined:
        if point[1] == 'p':
            result_dict[point[0]] = open_segment_count
        elif point[1] == 'l':
            open_segment_count += 1
        else:
            open_segment_count -= 1
    result = []
    for point in points:
        result.append(result_dict[point])
    return result


n, m = [int(x) for x in input().split()]
segments = []
for i in range(n):
    start, end = [int(x) for x in input().split()]
    segments.append((start, end))
points = [int(x) for x in input().split()]
print(' '.join([str(x) for x in fast_count_segments(segments, points)]))
