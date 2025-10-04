# Importing built-in modules
import math
import random

# Using imported functions
result = math.sqrt(16)
print(f"Square root of 16: {result}")

random_num = random.randint(1, 10)
print(f"Random number: {random_num}")

# Importing specific functions
from math import pi, ceil
print(f"Value of pi: {pi}")
print(f"Ceiling of 3.2: {ceil(3.2)}")

# Importing with alias (shorter name)
import matplotlib.pyplot as plt
import numpy as np

# This is common in ML code:
# import torch
# import torch.nn as nn
# from torch.utils.data import DataLoader

# Writing to a file
filename = "model_config.txt"

# 'w' mode - write (creates new file or overwrites existing)
with open(filename, 'w') as f:
    f.write("Model Configuration\n")
    f.write("-------------------\n")
    f.write("Layers: 12\n")
    f.write("Hidden size: 768\n")
    f.write("Dropout: 0.1\n")

print(f"Written to {filename}")

# Reading from a file
# 'r' mode - read
with open(filename, 'r') as f:
    content = f.read()
    print(f"\nFile contents:\n{content}")

# Reading line by line
print("Reading line by line:")
with open(filename, 'r') as f:
    for line in f:
        print(f"  {line.strip()}")  # strip() removes whitespace

# Appending to a file
# 'a' mode - append (adds to end without overwriting)
with open(filename, 'a') as f:
    f.write("Training epochs: 10\n")

print("\nAfter appending:")
with open(filename, 'r') as f:
    print(f.read())

# Working with paths
from pathlib import Path

# Create a Path object
data_path = Path("data")
model_path = Path("models")

# Check if path exists
if not data_path.exists():
    print(f"\n{data_path} does not exist")

# Joining paths
image_file = data_path / "train" / "image.jpg"
print(f"Image path: {image_file}")

# Reading structured data (common in ML)
# Writing training results to file
results_file = "training_results.txt"
epochs = [1, 2, 3, 4, 5]
losses = [0.5, 0.3, 0.2, 0.15, 0.1]

with open(results_file, 'w') as f:
    f.write("Epoch,Loss\n")
    for epoch, loss in zip(epochs, losses):
        f.write(f"{epoch},{loss}\n")

# Reading it back
print("\nTraining results:")
with open(results_file, 'r') as f:
    for line in f:
        print(f"  {line.strip()}")
