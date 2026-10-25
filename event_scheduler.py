import heapq
def can_attend_all(events):
    if not events:
        return True

    events.sort(key=lambda event: event[0])

    for i in range(1, len(events)):
        previous_end = events[i - 1][1]
        current_start = events[i][0]

        if current_start < previous_end:
            return False

    return True

def min_rooms_required(events):
    if not events:
        return 0

    events.sort(key=lambda event: event[0])

    rooms = []

    for start, end in events:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)

    return len(rooms)

if __name__ == "__main__":
    events = [(9, 10), (9, 11), (11, 12), (13, 14)]

    print("Can attend all:", can_attend_all(events))
    print("Minimum rooms required:", min_rooms_required(events))
