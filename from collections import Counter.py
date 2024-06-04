data = [
    2.6, 3.0, 3.7, 3.2, 2.2, 4.1, 3.5, 4.5, 3.5, 2.3,
    3.2, 3.4, 3.8, 3.2, 4.6, 3.7, 2.5, 4.4, 3.4, 3.3,
    2.9, 3.0, 4.3, 2.8, 3.5, 3.2, 3.9, 3.2, 3.2, 3.1,
    3.7, 3.4, 4.6, 3.8, 3.2, 2.6, 3.5, 4.2, 2.9, 3.6
]

# Initialize counters for each range
range_2_25 = 0
range_25_3 = 0
range_35_4 = 0
range_45_5 = 0

# Count frequency in each range
for num in data:
    if 2 <= num < 2.5:
        range_2_25 += 1
    elif 2.5 <= num < 3:
        range_25_3 += 1
    elif 3.5 <= num < 4:
        range_35_4 += 1
    elif 4.5 <= num <= 5:
        range_45_5 += 1

# Print the frequency of each range
print(f"Frequency of numbers between 2-2.5: {range_2_25}")
print(f"Frequency of numbers between 2.5-3: {range_25_3}")
print(f"Frequency of numbers between 3.5-4: {range_35_4}")
print(f"Frequency of numbers between 4.5-5: {range_45_5}")
