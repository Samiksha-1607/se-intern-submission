import heapq


def can_attend_all(events):
    if not events:
        return True

    sorted_events = sorted(events, key=lambda x: x[0])

    for i in range(1, len(sorted_events)):
        # overlap only if next starts before previous ends
        if sorted_events[i][0] < sorted_events[i-1][1]:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    sorted_events = sorted(events, key=lambda x: x[0])
    heap = []  # stores end times of ongoing meetings

    for start, end in sorted_events:
        if heap and heap[0] <= start:
            heapq.heappop(heap)   # this room is free now

        heapq.heappush(heap, end)

    return len(heap)   # peak simultaneous rooms needed
