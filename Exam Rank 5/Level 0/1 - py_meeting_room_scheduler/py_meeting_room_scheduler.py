def meeting_room_scheduler(meetings: list[list[int]]) -> dict[str, any]:
    order = sorted(meetings, key=lambda m: m[0])

    rooms = []
    room_end = []

    for start, end in order:
        placed = False
        for i in range(len(room_end)):
            if room_end[i] <= start:
                rooms[i].append([start, end])
                room_end[i] = end
                placed = True
                break
        if not placed:
            rooms.append([[start, end]])
            room_end.append(end)

    return {
        "room_needed": len(rooms),
        "room_assignments": {i: rooms[i] for i in range(len(rooms))},
    }