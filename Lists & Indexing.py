# Creating lists
class_names = ["pizza", "steak", "sushi"]
layer_sizes = [768, 3072, 768]
print(f"Class names: {class_names}")
print(f"Layer sizes: {layer_sizes}")

# Indexing - accessing elements by position
# Python uses zero-based indexing (first element is at index 0)
first_class = class_names[0]
last_class = class_names[-1]  # negative indexing starts from the end
print(f"First class: {first_class}")
print(f"Last class: {last_class}")

# Slicing - getting a portion of the list
# Format: list[start:end:step]
first_two = class_names[0:2]  # elements at index 0 and 1
print(f"First two classes: {first_two}")

all_classes = class_names[:]  # copy entire list
print(f"All classes: {all_classes}")

# List operations
class_names.append("burger")  # add item to end
print(f"After append: {class_names}")

class_names.remove("burger")  # remove specific item
print(f"After remove: {class_names}")

# Length of list
num_classes = len(class_names)
print(f"Number of classes: {num_classes}")

# Checking if item exists
has_pizza = "pizza" in class_names
print(f"Has pizza: {has_pizza}")

# List comprehension - create lists in one line
squared = [x**2 for x in range(5)]
print(f"Squared numbers: {squared}")

# Unpacking lists
width, height, channels = [224, 224, 3]
print(f"Image shape: {width}x{height}x{channels}")
