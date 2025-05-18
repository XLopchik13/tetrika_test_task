def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def clip_intervals(intervals, start_clip, end_clip):
    clipped = []
    for start, end in intervals:
        clipped_start = max(start, start_clip)
        clipped_end = min(end, end_clip)
        if clipped_start < clipped_end:
            clipped.append((clipped_start, clipped_end))
    return clipped


def intersect_intervals(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        start_a, end_a = a[i]
        start_b, end_b = b[j]
        start = max(start_a, start_b)
        end = min(end_a, end_b)
        if start < end:
            result.append((start, end))
        if end_a < end_b:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    pupil_intervals = list(zip(intervals['pupil'][::2], intervals['pupil'][1::2]))
    tutor_intervals = list(zip(intervals['tutor'][::2], intervals['tutor'][1::2]))

    pupil_intervals = clip_intervals(pupil_intervals, lesson_start, lesson_end)
    tutor_intervals = clip_intervals(tutor_intervals, lesson_start, lesson_end)

    pupil_merged = merge_intervals(pupil_intervals)
    tutor_merged = merge_intervals(tutor_intervals)

    intersections = intersect_intervals(pupil_merged, tutor_merged)

    total_time = sum(end - start for start, end in intersections)

    return total_time
