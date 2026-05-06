def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# ---- INPUT ----
print("Enter the number of intervals followed by the intervals (space separated):")
n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]

# ---- OUTPUT ----
print(merge(intervals))