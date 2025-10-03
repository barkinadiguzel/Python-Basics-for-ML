# Integer - whole numbers
patch_size = 16
num_layers = 12
print(f"patch_size: {patch_size}, type: {type(patch_size)}")

# Float - decimal numbers
learning_rate = 0.001
dropout = 0.1
print(f"learning_rate: {learning_rate}, type: {type(learning_rate)}")

# String - text data
device = "cuda"
model_name = "vit-base"
print(f"device: {device}, type: {type(device)}")

# Boolean - True or False
is_training = True
use_pretrained = False
print(f"is_training: {is_training}, type: {type(is_training)}")

# Type conversion
height = "224"  # string
height_int = int(height)  # convert to integer
print(f"Original: {height} (type: {type(height)})")
print(f"Converted: {height_int} (type: {type(height_int)})")

# Multiple assignment
img_height, img_width = 224, 224
print(f"Image dimensions: {img_height} x {img_width}")

# Basic arithmetic
total_patches = (img_height * img_width) // (patch_size ** 2)
print(f"Total patches: {total_patches}")

# String formatting
message = f"Model running on {device} with {num_layers} layers"
print(message)
