def find_available_slots(
    working_hours: list[list[int]], appointments: list[list[int]], min_duration: int
) -> list[list[int]]:
    working_hours = merge_intervals(working_hours)
    appointments = merge_intervals(appointments)
    free = find_available_free_slots(working_hours, appointments)
    return [interval for interval in free if interval[1] - interval[0] >= min_duration]


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def find_available_free_slots(
    working_hours: list[list[int]],
    appointments: list[list[int]],
) -> list[list[int]]:
    free = []

    app_idx = 0
    for work_start, work_end in working_hours:
        curr = work_start
        while app_idx < len(appointments):
            app_start, app_end = appointments[app_idx]

            if app_start >= work_end:
                break

            if app_end <= curr:
                app_idx += 1
                continue

            if app_start > curr:
                free.append([curr, app_start])

            curr = max(curr, app_end)

        free.append([curr, work_end])

    return free


"""
# Old implementation with too many conditionals
def find_available_free_slots(
    working_hours: list[list[int]],
    appointments: list[list[int]],
) -> list[list[int]]:
    free = []
    i = j = 0
    while i < len(working_hours) and j < len(appointments):
        w, a = working_hours[i], appointments[j]
        if w[0] < a[0]:
            free.append([w[0], min(w[1], a[0])])
            if w[1] < a[0]:
                # |--|
                #        |----|
                i += 1
            elif w[1] > a[1]:
                # |-------|
                #   |--|
                w[0] = a[1]
                j += 1
            elif w[1] < a[1]:
                # |----|
                #   |------|
                a[0] = w[1]
                i += 1
            else:
                # |----|
                #   |--|
                i += 1
                j += 1
        else:
            if w[0] > a[1]:
                #         |--|
                # |---|
                j += 1
            elif w[1] < a[1]:
                #   |--|
                # |-------|
                a[0] = w[1]
                i += 1
            elif w[1] > a[1]:
                #   |--------|
                # |----|
                w[0] = a[1]
                j += 1
            else:
                #   |--|
                # |----|
                i += 1
                j += 1
    if i < len(working_hours):
        free.append(working_hours[i:])
    return free
"""

if __name__ == "__main__":
    print(
        find_available_slots(
            [[1, 10], [15, 20], [50, 60]], [[3, 8], [12, 16], [19, 22], [100, 120]], 1
        )
    )
    print(
        find_available_slots(
            [[1, 10], [15, 20], [50, 60]], [[3, 8], [12, 16], [19, 22], [100, 120]], 3
        )
    )

"""
Problem 1: The Provider Availability Gap Finder
Domain: Healthcare (e.g., Headway, Zocdoc) Difficulty: Medium Core Concept: Interval Manipulation

Scenario: You are building the scheduling engine for a mental health platform. Providers set their "working hours" (availability), but these hours can be fragmented (e.g., a provider might add "9:00-11:00" and then separately add "10:30-12:00" to extend it).

Simultaneously, patients have already booked appointments during these times. Your task is to calculate the remaining free slots that are long enough for a new patient to book.

Inputs:

working_hours: A list of [start, end] intervals (in minutes from midnight). These may overlap and are unsorted.

Example: [[540, 660], [630, 720]] (9:00-11:00, 10:30-12:00)

appointments: A list of [start, end] intervals representing booked slots. These may also overlap (e.g., double bookings) and are unsorted.

Example: [[560, 600]] (9:20-10:00)

min_duration: An integer representing the minimum duration (in minutes) required for a slot to be valid.

Output:

A sorted list of disjoint [start, end] intervals representing free time where a new appointment of at least min_duration can be scheduled.
"""
