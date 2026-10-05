marks = [78, 85, 67, 90, 72]

total = 0

for mark in marks:
    print("Mark:", mark)
    total = total + mark

average = total / len(marks)

print("\nTotal:", total)
print("Average:", average)