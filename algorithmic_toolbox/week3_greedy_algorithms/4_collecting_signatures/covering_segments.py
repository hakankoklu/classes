# Uses python3


def optimal_points(segments):
    points = []
    segments.sort(key=lambda x: x[1])
    points.append(segments[0][1])
    for segment in segments[1:]:
        if segment[0] <= points[-1] <= segment[1]:
            continue
        points.append(segment[1])
    return points


n = int(input())
intervals = []
for i in range(n):
    interval = tuple([int(x) for x in input().split()])
    intervals.append(interval)
points = optimal_points(intervals)
print(len(points))
print(' '.join([str(x) for x in points]))