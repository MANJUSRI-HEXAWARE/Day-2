def longest_claim_spike(daily_counts, threshold=100):
    best_start = 0
    best_length = 0
    start = 0
    for end, count in enumerate(daily_counts):
        if count <= threshold:
            start = end + 1
        elif end - start + 1 > best_length:
            best_start = start
            best_length = end - start + 1
    if best_length == 0:
        return 0, None, None
    return best_length, best_start + 1, best_start + best_length


if __name__ == "__main__":
    counts = [80, 110, 125, 140, 90, 105, 130, 160, 115, 145, 100, 120, 135]
    length, first_day, last_day = longest_claim_spike(counts)
    print("Daily claims:", counts)
    print("Longest run (days):", length)
    print("From day:", first_day)
    print("Through day:", last_day)
    print("Empty input:", longest_claim_spike([]))
