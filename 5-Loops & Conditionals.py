# For loop - iterate over a sequence
class_names = ["pizza", "steak", "sushi"]
print("Classes:")
for name in class_names:
    print(f"  - {name}")

# For loop with range() - generate sequence of numbers
print("\nFirst 5 epochs:")
for epoch in range(5):
    print(f"Epoch {epoch}")

# range() with start, stop, step
print("\nEven numbers from 0 to 10:")
for num in range(0, 11, 2):
    print(num, end=" ")
print()

# enumerate() - get index and value together
print("\nIndexed classes:")
for idx, name in enumerate(class_names):
    print(f"Class {idx}: {name}")

# enumerate() with custom start index
print("\nClasses starting from 1:")
for idx, name in enumerate(class_names, start=1):
    print(f"{idx}. {name}")

# While loop - repeat until condition is false
count = 0
print("\nWhile loop countdown:")
while count < 3:
    print(f"Count: {count}")
    count += 1

# If-elif-else statements
accuracy = 0.85
print(f"\nModel accuracy: {accuracy}")

if accuracy >= 0.9:
    print("Excellent performance!")
elif accuracy >= 0.7:
    print("Good performance")
else:
    print("Needs improvement")

# Nested loops - loop inside a loop
print("\nCreating 3x3 grid:")
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()  # new line after each row

# Break and continue
print("\nFinding first value > 5:")
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num > 5:
        print(f"Found: {num}")
        break  # exit the loop

print("\nSkipping even numbers:")
for num in range(10):
    if num % 2 == 0:
        continue  # skip to next iteration
    print(num, end=" ")
print()

# List comprehension with conditional
print("\nFiltering classes:")
filtered = [name for name in class_names if len(name) > 5]
print(f"Classes with more than 5 letters: {filtered}")
