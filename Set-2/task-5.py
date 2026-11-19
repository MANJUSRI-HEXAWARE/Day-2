def merge_sorted_claims(office_a, office_b):
    i = 0
    j = 0
    merged = []
    while i < len(office_a) and j < len(office_b):
        if office_a[i] <= office_b[j]:
            merged.append(office_a[i])
            i += 1
        else:
            merged.append(office_b[j])
            j += 1
    merged.extend(office_a[i:])
    merged.extend(office_b[j:])
    return merged


if __name__ == "__main__":
    north = [1001, 1004, 1008, 1012, 1012]
    south = [1002, 1004, 1009, 1015]
    print("North office:", north)
    print("South office:", south)
    print("Merged claims:", merge_sorted_claims(north, south))
    print("Empty inputs:", merge_sorted_claims([], []))
