def highest_average_window(counts, window_size=4):
    if window_size <= 0 or len(counts) < window_size:
        return None
    total = sum(counts[:window_size])
    best_total = total
    best_start = 0
    for end in range(window_size, len(counts)):
        total += counts[end] - counts[end - window_size]
        if total > best_total:
            best_total = total
            best_start = end - window_size + 1
    return best_start, best_start + window_size, best_total / window_size


if __name__ == "__main__":
    counts = [120, 135, 110, 145, 160, 190, 240, 280, 310, 295, 270, 250,
              230, 260, 340, 390, 420, 400, 350, 300, 260, 210, 180, 150]
    result = highest_average_window(counts)
    print("Hourly parcel counts:", counts)
    if result:
        start, end, average = result
        print(f"Highest-average 4-hour window: {start:02d}:00-{end:02d}:00")
        print(f"Average parcels per hour: {average:.2f}")
    else:
        print("No valid window")
