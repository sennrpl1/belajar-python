#
def statitik(data):
    total   = sum(data)
    rata    = total / len(data)
    minimum = min(data)
    maksimum= max(data)
    return total, rata, minimum, maksimum

nilai = [75, 82, 90, 68, 95]
tot, avg, mn, mx = statitik(nilai)
print(f"total: {tot} | rata: {avg} | min: {mn} | max: {mx}")